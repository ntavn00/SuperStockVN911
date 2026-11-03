"""
valuation_engine.py - Bộ máy tính toán định giá cổ phiếu đa phương pháp
Tự động áp dụng phương pháp định giá phù hợp cho từng nhóm ngành tại Việt Nam:
1. DCF FCFF & FCFE (Sản xuất, Tiêu dùng, Công nghệ, Tiện ích)
2. Residual Income (Thu nhập thặng dư) & Adjusted P/B (Ngân hàng)
3. RNAV - Revalued Net Asset Value (Bất động sản dân dụng)
4. Relative Multiples (P/E chuẩn hóa chu kỳ, P/B, EV/EBITDA)
5. Blended Valuation (Tổng hợp trọng số ngành) & Phân tích độ nhạy (Sensitivity Matrix)
"""

import numpy as np
import pandas as pd
from typing import Dict, Any, List

def calculate_dcf_fcff(
    data: Dict[str, Any],
    wacc: float = 11.5,
    growth_lt: float = 4.0,
    forecast_years: int = 5,
    growth_fcf_rate: float = None
) -> Dict[str, Any]:
    """
    Mô hình Chiết khấu Dòng tiền Thuần Doanh nghiệp (FCFF) Chuẩn Thực Chiến V3.0.
    Đơn vị dòng tiền: Tỷ VNĐ.
    Đơn vị giá trị cổ phiếu: VNĐ/cổ phiếu.
    """
    wacc_dec = wacc / 100.0
    g_dec = growth_lt / 100.0
    
    # Kiểm tra điều kiện WACC > g để mô hình hội tụ
    if wacc_dec <= g_dec + 0.025:
        wacc_dec = g_dec + 0.035
        wacc = wacc_dec * 100.0

    # Tự động nội suy tốc độ tăng trưởng FCF 5 năm tới từ CAGR thực tế của doanh nghiệp (chặn biên 8% - 14%)
    if growth_fcf_rate is None:
        cagr_bvps = float(data.get("cagr_bvps", 11.0))
        growth_fcf_rate = min(14.0, max(8.0, cagr_bvps * 0.80))

    # Định luật Tái Đầu Tư Cơ Bản của Aswath Damodaran:
    # FCFF = NOPAT * (1 - Reinvestment_Rate), trong đó Reinvestment_Rate = g / ROIC
    ebit_series = data.get("ebit", [12000])
    np_latest = float(data.get("net_profit_ttm") or data.get("net_profit", [1000])[-1])
    ebit_latest = max(float(ebit_series[-1]), np_latest * 1.25)
    tax_rate = 0.20
    nopat = ebit_latest * (1.0 - tax_rate)
    
    roic = max(12.0, float(data.get("roic", 15.0)))
    reinv_rate = min(0.42, max(0.22, (growth_fcf_rate * 0.55) / roic))
    normalized_fcff = nopat * (1.0 - reinv_rate)
    
    # Dự phóng FCFF trong N năm tới
    projected_fcff = []
    pv_fcff_list = []
    
    current_fcff = normalized_fcff
    for t in range(1, forecast_years + 1):
        current_fcff *= (1.0 + growth_fcf_rate / 100.0)
        pv = current_fcff / ((1.0 + wacc_dec) ** t)
        projected_fcff.append(round(current_fcff, 1))
        pv_fcff_list.append(round(pv, 1))
        
    sum_pv_forecast = sum(pv_fcff_list)
    
    # Giá trị Terminal Value ở năm cuối
    terminal_value = (projected_fcff[-1] * (1.0 + g_dec)) / (wacc_dec - g_dec)
    pv_terminal_value = terminal_value / ((1.0 + wacc_dec) ** forecast_years)
    
    # Enterprise Value (EV)
    enterprise_value = sum_pv_forecast + pv_terminal_value
    
    # Điều chỉnh Nợ ròng và Tiền mặt để ra Equity Value (Tỷ VNĐ)
    cash = float(data.get("cash_and_investments", 0))
    debt = float(data.get("total_debt", 0))
    net_debt = max(0.0, debt - cash)
    effective_net_debt = min(net_debt, enterprise_value * 0.45)
    equity_value_billion = enterprise_value - effective_net_debt + max(0.0, cash - debt)
    
    shares = data.get("shares_outstanding", 1)
    fair_value_per_share = (equity_value_billion * 1_000_000_000) / shares
    
    return {
        "model_name": "DCF (FCFF)",
        "wacc": round(wacc, 2),
        "growth_lt": round(growth_lt, 2),
        "growth_fcf_rate": round(growth_fcf_rate, 1),
        "base_fcff": round(normalized_fcff, 1),
        "projected_fcff": projected_fcff,
        "pv_forecast": round(sum_pv_forecast, 1),
        "terminal_value": round(terminal_value, 1),
        "pv_terminal_value": round(pv_terminal_value, 1),
        "enterprise_value": round(enterprise_value, 1),
        "cash": cash,
        "debt": debt,
        "equity_value": round(equity_value_billion, 1),
        "fair_value": max(0.0, round(fair_value_per_share, 0))
    }

def calculate_banking_residual_income(
    data: Dict[str, Any],
    cost_of_equity: float = 11.5,
    growth_lt: float = 4.5,
    roe_expected: float = 20.0,
    forecast_years: int = 5
) -> Dict[str, Any]:
    """
    Mô hình Thu nhập thặng dư (Residual Income - RI) chuyên biệt cho Ngân hàng.
    Giá trị = Book Value hiện tại + Tổng PV(RI tương lai) + Terminal RI.
    """
    ke_dec = cost_of_equity / 100.0
    g_dec = growth_lt / 100.0
    roe_dec = roe_expected / 100.0
    
    if ke_dec <= g_dec:
        ke_dec = g_dec + 0.02
        cost_of_equity = ke_dec * 100.0
        
    raw_bvps_0 = data.get("bvps", 25000.0)
    # Khấu trừ nợ xấu chưa trích lập dự phòng đầy đủ (NPL lag haircut):
    # BVPS thực = BVPS báo cáo - max(0, Nợ xấu Nhóm 3-5 - Quỹ DPRR) / CP
    npl_haircut_pct = data.get("npl_haircut_pct", 3.0)
    bvps_0 = raw_bvps_0 * (1.0 - npl_haircut_pct / 100.0)
    current_bvps = bvps_0
    
    pv_ri_list = []
    ri_values = []
    bvps_progression = []
    
    # Giả định tỷ lệ giữ lại lợi nhuận để tái đầu tư (Retention Rate) ~ 75% (trả cổ tức 25%)
    retention_rate = 0.75
    
    for t in range(1, forecast_years + 1):
        eps_t = current_bvps * roe_dec
        charge = current_bvps * ke_dec
        ri_t = eps_t - charge # Thu nhập thặng dư trên mỗi cổ phiếu
        pv_ri = ri_t / ((1.0 + ke_dec) ** t)
        
        ri_values.append(round(ri_t, 0))
        pv_ri_list.append(round(pv_ri, 0))
        
        # Cập nhật BVPS cho kỳ tiếp theo
        current_bvps += eps_t * retention_rate
        bvps_progression.append(round(current_bvps, 0))
        
    sum_pv_ri = sum(pv_ri_list)
    
    # Terminal RI
    terminal_ri = (ri_values[-1] * (1.0 + g_dec)) / (ke_dec - g_dec)
    pv_terminal_ri = terminal_ri / ((1.0 + ke_dec) ** forecast_years)
    
    fair_value = bvps_0 + sum_pv_ri + pv_terminal_ri
    
    return {
        "model_name": "Residual Income (Ngân hàng)",
        "cost_of_equity": round(cost_of_equity, 2),
        "roe_expected": round(roe_expected, 2),
        "growth_lt": round(growth_lt, 2),
        "bvps_0": round(bvps_0, 0),
        "sum_pv_ri": round(sum_pv_ri, 0),
        "pv_terminal_ri": round(pv_terminal_ri, 0),
        "fair_value": max(0.0, round(fair_value, 0))
    }

def calculate_banking_adjusted_pb(
    data: Dict[str, Any],
    target_pb: float = 1.85,
    npl_haircut_pct: float = 5.0
) -> Dict[str, Any]:
    """
    Định giá P/B điều chỉnh chất lượng tài sản (NPL Haircut) cho Ngân hàng.
    """
    raw_bvps = data.get("bvps", 25000.0)
    # Khấu trừ rủi ro nợ xấu tiềm ẩn chưa trích lập
    adjusted_bvps = raw_bvps * (1.0 - npl_haircut_pct / 100.0)
    fair_value = adjusted_bvps * target_pb
    
    return {
        "model_name": "P/B Điều chỉnh Chất lượng Tài sản",
        "raw_bvps": round(raw_bvps, 0),
        "npl_haircut_pct": npl_haircut_pct,
        "adjusted_bvps": round(adjusted_bvps, 0),
        "target_pb": round(target_pb, 2),
        "fair_value": round(fair_value, 0)
    }

def calculate_real_estate_rnav(
    data: Dict[str, Any],
    holding_discount_pct: float = 10.0
) -> Dict[str, Any]:
    """
    Mô hình RNAV (Revalued Net Asset Value) định giá từng dự án BĐS.
    Tích hợp bộ lọc Chống Bẫy "Hàng Tồn Kho Chết":
    Chỉ cộng thặng dư đất nếu Tỷ lệ Người mua trả tiền trước / Hàng tồn kho >= 15%.
    Nếu < 15%, áp thêm mức phạt chiết khấu tồn kho tắc pháp lý (Dead Inventory Penalty).
    """
    projects = data.get("projects_rnav", [])
    inventory = data.get("inventory", 5000) # Tỷ
    unearned_rev = data.get("unearned_revenue", 1000) # Người mua trả tiền trước (Mã 312 + 332)
    
    # Kiểm tra tỷ lệ thanh khoản dự án
    prepayment_ratio = (unearned_rev / inventory) if inventory > 0 else 0.0
    dead_inventory_penalty = 0.0
    if prepayment_ratio < 0.15:
        # Tồn kho lớn nhưng không có người mua trả tiền trước -> Rủi ro pháp lý/tắc nghẽn
        dead_inventory_penalty = 0.15 # Phạt thêm 15% chiết khấu
        
    eff_discount = holding_discount_pct + (dead_inventory_penalty * 100.0)

    if not projects:
        bvps = data.get("bvps", 30000.0)
        markup = 1.6 if prepayment_ratio >= 0.15 else 1.1 # Không nâng hệ số quỹ đất nếu tồn kho chết
        return {
            "model_name": "RNAV Quỹ đất Dự án",
            "fair_value": round(bvps * markup * (1.0 - dead_inventory_penalty), 0),
            "prepayment_ratio": round(prepayment_ratio * 100, 1),
            "is_clean_legal": prepayment_ratio >= 0.15,
            "details": "Ước lượng theo Book Value điều chỉnh quỹ đất"
        }
        
    total_pv_projects = sum(p["pv_cashflow"] for p in projects)
    cash = data.get("cash_and_investments", 0)
    debt = data.get("total_debt", 0)
    
    # Equity RNAV = Tổng PV dự án + Tiền mặt - Nợ vay + 30% Lãi gộp từ Người mua trả tiền trước
    net_rnav_billion = total_pv_projects + cash - debt + (unearned_rev * 0.35)
    
    # Áp dụng mức chiết khấu rủi ro pháp lý & thực thi
    net_rnav_discounted = net_rnav_billion * (1.0 - eff_discount / 100.0)
    
    shares = data.get("shares_outstanding", 1)
    fair_value_per_share = (net_rnav_discounted * 1_000_000_000) / shares
    
    return {
        "model_name": "RNAV Dự án Bất Động Sản",
        "total_pv_projects": total_pv_projects,
        "net_rnav_billion": round(net_rnav_discounted, 1),
        "prepayment_ratio": round(prepayment_ratio * 100, 1),
        "is_clean_legal": prepayment_ratio >= 0.15,
        "holding_discount_pct": eff_discount,
        "fair_value": max(0.0, round(fair_value_per_share, 0)),
        "projects_count": len(projects)
    }

def calculate_relative_multiples(
    data: Dict[str, Any],
    custom_pe: float = None,
    custom_pb: float = None,
    custom_ev_ebitda: float = None,
    growth_rate: float = 12.0
) -> Dict[str, Any]:
    """
    Định giá tương đối chuyên sâu theo Chuẩn Thực Chiến V3.0 (Data-Driven Quant Engine):
    1. P/E Chuẩn hóa & Dải P/E Lịch sử thực nghiệm 5 năm (+/- 1SD, 2SD) độc lập với thanh trượt chủ quan.
    2. P/B Ngành & Điều chỉnh ROE thực tế.
    3. EV/EBITDA chuẩn hóa.
    4. PEG (Price/Earnings to Growth) & Peter Lynch Ratio (R+G)/PE.
    """
    results = {}
    norm_eps = float(data.get("normalized_eps") or data.get("eps_current") or 2500.0)
    hist_pe_median = float(data.get("peer_pe_median", 12.0))
    target_pe = float(custom_pe) if custom_pe is not None else hist_pe_median
    
    # 1. P/E Chuẩn hóa
    results["pe_valuation"] = round(norm_eps * target_pe, 0)
    results["target_pe"] = round(target_pe, 1)
    results["eps_used"] = round(norm_eps, 0)
    
    # Dải P/E Lịch sử thực nghiệm (Neo vào trung vị lịch sử 5 năm và độ lệch chuẩn thực tế pe_sigma_hist)
    mu_pe = hist_pe_median
    sigma_pe = float(data.get("pe_sigma_hist") or max(1.5, round(mu_pe * 0.18, 1)))
    results["pe_mu"] = round(mu_pe, 1)
    results["pe_sigma"] = round(sigma_pe, 2)
    results["pe_band_minus_1sd"] = round(norm_eps * max(5.5, mu_pe - sigma_pe), 0)
    results["pe_band_minus_2sd"] = round(norm_eps * max(4.5, mu_pe - 1.8 * sigma_pe), 0)
    results["pe_band_plus_1sd"] = round(norm_eps * (mu_pe + sigma_pe), 0)
    results["pe_band_plus_2sd"] = round(norm_eps * (mu_pe + 2.0 * sigma_pe), 0)
    results["pe_sell_overheat"] = round(norm_eps * (mu_pe + 1.5 * sigma_pe), 0) # Ngưỡng quá nhiệt
    
    # 2. P/B
    bvps = float(data.get("bvps", 20000.0))
    target_pb = float(custom_pb) if custom_pb is not None else float(data.get("peer_pb_median", 1.5))
    results["pb_valuation"] = round(bvps * target_pb, 0)
    results["target_pb"] = round(target_pb, 2)
    results["bvps_used"] = round(bvps, 0)
    
    # 3. PEG (Peter Lynch)
    g_dec = max(5.0, min(25.0, growth_rate))
    results["peg_fair_value"] = round(norm_eps * g_dec, 0) # P/E = G tương đương PEG = 1.0
    div_yield = float(data.get("dividend_yield", 2.5))
    results["peter_lynch_ratio"] = round((div_yield + g_dec) / target_pe, 2) if target_pe > 0 else 1.0
    results["is_peter_lynch_attractive"] = results["peter_lynch_ratio"] >= 1.5
    
    # 4. EV/EBITDA
    ebit_series = data.get("ebit", [10000])
    np_latest = float(data.get("net_profit_ttm") or data.get("net_profit", [1000])[-1])
    ebit_latest = max(float(ebit_series[-1]), np_latest * 1.25)
    da_latest = float(data.get("da", [3000])[-1])
    ebitda = ebit_latest + da_latest
    target_ev_ebitda = float(custom_ev_ebitda) if custom_ev_ebitda is not None else float(data.get("peer_ev_ebitda_median", 7.5))
    
    ev_val = ebitda * target_ev_ebitda
    cash = float(data.get("cash_and_investments", 0))
    debt = float(data.get("total_debt", 0))
    net_debt = max(0.0, debt - cash)
    effective_net_debt = min(net_debt, ev_val * 0.35)
    equity_val = ev_val - effective_net_debt + max(0.0, cash - debt)
    shares = data.get("shares_outstanding", 1)
    ev_ebitda_per_share = (equity_val * 1_000_000_000) / shares if shares > 0 else 0.0
    
    results["ev_ebitda_valuation"] = max(0.0, round(ev_ebitda_per_share, 0))
    results["target_ev_ebitda"] = round(target_ev_ebitda, 1)
    
    # Hợp nhất Đa Bội Số Tương Đối (60% P/E + 25% EV/EBITDA hoặc P/B + 15% P/B)
    sector = data.get("sector", "")
    if sector in ["BANKING", "SECURITIES", "INSURANCE", "REAL_ESTATE"]:
        results["blended_relative_price"] = round(0.55 * results["pe_valuation"] + 0.45 * results["pb_valuation"], 0)
    else:
        results["blended_relative_price"] = round(
            0.55 * results["pe_valuation"] + 0.30 * results["ev_ebitda_valuation"] + 0.15 * results["pb_valuation"], 0
        )
    
    return results

def calculate_market_regime_and_eys(
    pe_core_market: float = 12.5,
    rf_10y_vgb: float = 4.58
) -> Dict[str, Any]:
    """
    Mô-đun 1 (Deep Research 2.1): Thuật toán Nhận diện Chu kỳ Thị trường Lõi & Chênh lệch Lợi suất Thu nhập (EYS).
    Loại bỏ biến dạng chỉ số bề mặt VN-Index do các mã P/E > 40x gây ra.
    EYS = (1 / PE_Core_Market) - Rf_10Y
    """
    pe_core = max(5.0, pe_core_market)
    earnings_yield = (1.0 / pe_core) * 100.0 # Lợi suất thu nhập E/P (%)
    eys = earnings_yield - rf_10y_vgb # Chênh lệch Lợi suất Thu nhập (%)
    
    if pe_core <= 12.0 or eys >= 3.8:
        regime = "CHEAP_TROUGH"
        regime_name = "Pha Rẻ Lịch Sử / Đáy Chu Kỳ"
        color = "#10B981"
        delta_mos = 5.0
        signal = "Mở rộng hạn mức giải ngân tối đa; giảm MOS cơ sở đi 5%."
    elif pe_core <= 14.9 or eys >= 2.2:
        regime = "FAIR_BASE"
        regime_name = "Pha Hợp Lý / Tăng Trưởng Cơ Sở"
        color = "#3B82F6"
        delta_mos = 0.0
        signal = "Định giá cân bằng quanh mốc 10 năm (14.9x); kích hoạt tích lũy theo dải điều chỉnh hàng năm."
    else:
        regime = "OVERHEATED_PEAK"
        regime_name = "Pha Quá Nhiệt / Đỉnh Chu Kỳ"
        color = "#EF4444"
        delta_mos = -10.0 # Tăng MOS lên
        signal = "Phần bù rủi ro mỏng (EYS < 1.5%); siết chặt MOS tối đa, ưu tiên giữ tiền mặt/trái phiếu."
        
    return {
        "pe_core_market": round(pe_core, 1),
        "earnings_yield": round(earnings_yield, 2),
        "rf_10y_vgb": round(rf_10y_vgb, 2),
        "eys": round(eys, 2),
        "regime": regime,
        "regime_name": regime_name,
        "color": color,
        "delta_mos": delta_mos,
        "signal": signal
    }

def calculate_multi_tranche_buy_zones(
    fair_value: float,
    sticker_price_classic: float,
    sticker_price_ke: float,
    ten_cap_price: float,
    payback_price_8y: float,
    pe_band_minus_1sd: float,
    pe_band_minus_2sd: float,
    zombie_price: float,
    current_price: float,
    tier_code: str = "TIER_1",
    mos_pct: float = 20.0,
    stock_data: Dict[str, Any] = None
) -> Dict[str, Any]:
    """
    Mô-đun 4 (Chuẩn Thực Chiến V3.0): Thuật toán Rải Lệnh Giải Ngân 3 Giai Đoạn (Time & Value Tranching).
    Khắc phục triệt để 2 lỗi toán học:
    1. Chống Đảo Ngược Tranche (Bắt buộc P_Fair > P_Tranche_1 > P_Tranche_2 > P_Tranche_3 nghiêm ngặt).
    2. Kết nối với Phân vị Giao dịch Thực nghiệm 1 năm (p15, p25) & Giá trị Sổ sách Hữu hình (1.0x BVPS)
       để đảm bảo các vùng mua hoàn toàn khả thi trong nhịp chỉnh thông thường hàng năm trên HOSE.
    """
    sdata = stock_data or {}
    bvps = float(sdata.get("bvps", 0.0))
    p_1y_p25 = float(sdata.get("price_1y_p25", 0.0))
    p_1y_p15 = float(sdata.get("price_1y_p15", 0.0))
    p_1y_min = float(sdata.get("price_1y_min", 0.0))
    p_1y_max = float(sdata.get("price_1y_max", 0.0))

    # 1. Tranche 1 (30% Vốn): Điểm Mua Tích Lũy Nhịp Chỉnh Hàng Năm (Chiết khấu nhẹ 10% - 12% từ Fair Value)
    t1_discount = min(0.12, max(0.08, (mos_pct / 100.0) * 0.60))
    t1_intrinsic = fair_value * (1.0 - t1_discount)
    if 0 < p_1y_p25 <= fair_value * 0.94 and p_1y_p25 >= fair_value * 0.84:
        p_t1 = 0.65 * t1_intrinsic + 0.35 * p_1y_p25
    else:
        p_t1 = t1_intrinsic
    p_t1 = min(fair_value * 0.92, max(fair_value * 0.86, p_t1))

    # 2. Tranche 2 (40% Vốn): Điểm Mua Giá Trị Chuẩn Mực / MOS Động (Khớp chuẩn với Giá Mua MOS = Fair Value * (1 - MOS))
    t2_intrinsic = fair_value * (1.0 - mos_pct / 100.0)
    t2_anchors = [t2_intrinsic, t2_intrinsic] # Trọng số chính vào chuẩn MOS Động
    if 0 < pe_band_minus_1sd <= p_t1 * 0.96:
        t2_anchors.append(max(fair_value * 0.75, pe_band_minus_1sd))
    if 0 < p_1y_p15 <= p_t1 * 0.96 and p_1y_p15 >= fair_value * 0.72:
        t2_anchors.append(p_1y_p15)
    p_t2 = float(np.median(t2_anchors))
    # Bắt buộc nghiêm ngặt: P_Tranche_2 <= 93% P_Tranche_1 và >= 75% Fair Value
    p_t2 = min(p_t1 * 0.93, max(fair_value * 0.75, p_t2))

    # 3. Tranche 3 (30% Vốn): Điểm Mua Khủng Hoảng Chu Kỳ / Sàn Tài Sản Thực (Deep Value & Tangible Book Floor)
    t3_candidates = [fair_value * 0.68]
    if pe_band_minus_2sd > 0:
        t3_candidates.append(pe_band_minus_2sd)
    if bvps > 0:
        t3_candidates.append(bvps * 1.02) # Sàn P/B ~ 1.0x BVPS cho doanh nghiệp đầu ngành
    if sticker_price_classic > 0:
        t3_candidates.append(sticker_price_classic * 0.70)
    p_t3 = float(np.median(t3_candidates))
    # Bắt buộc nghiêm ngặt: P_Tranche_3 <= 88% P_Tranche_2 và >= 60% Fair Value (hoặc 0.95x BVPS)
    floor_t3 = max(fair_value * 0.60, bvps * 0.95 if bvps < fair_value * 0.75 else fair_value * 0.60)
    p_t3 = min(p_t2 * 0.88, max(floor_t3, p_t3))

    # Đánh giá tính khả thi thực nghiệm so với biên độ 52 tuần (52-Week Empirical Reachability)
    def eval_reachability(price_lvl: float) -> str:
        if p_1y_min <= 0 or p_1y_max <= 0:
            return "Khả thi trong nhịp chỉnh trung hạn"
        if price_lvl >= current_price:
            return "⚡ Đang khớp ngay tại thị giá hiện tại!"
        elif price_lvl >= p_1y_p25:
            return "✅ Tần suất cao (Xuất hiện 2–3 lần/năm trong nhịp chỉnh 10–15%)"
        elif price_lvl >= p_1y_min * 0.98:
            return "🎯 Khả thi (Nằm trong vùng đáy 52 tuần qua)"
        else:
            diff_min = ((p_1y_min - price_lvl) / p_1y_min) * 100.0
            return f"🛡️ Phòng thủ sâu (Thấp hơn đáy 1 năm {diff_min:.1f}% — Dành cho cú sốc vĩ mô)"

    # Tính Win-Loss Ratio và Worst Case Floor hợp lý (không để Zombie Value âm kéo sập mẫu số)
    p_worst = max(p_t3 * 0.92, bvps * 0.90 if bvps > 0 else p_t3 * 0.90)
    downside_risk = max(current_price * 0.05, current_price - p_worst)
    upside_gain = max(0.0, fair_value - current_price)
    if upside_gain <= 0:
        upside_gain = max(0.0, fair_value * 1.20 - current_price)
    win_loss_ratio = round(upside_gain / downside_risk, 2)
    
    return {
        "tranche_1": {
            "name": "Tranche 1: Điểm Mua Tích Lũy Hàng Năm",
            "capital_weight": "30% Vị thế",
            "trigger_price": round(p_t1, 0),
            "is_in_buy_zone": current_price <= p_t1,
            "reachability": eval_reachability(p_t1),
            "conditions": f"Chiết khấu ~{int(round((1 - p_t1/fair_value)*100))}% từ Fair Value (Neo phân vị p25 1 năm & -1SD P/E).",
            "execution": "Giải ngân 30% vốn đầu tiên trong các nhịp chỉnh thông thường hàng năm khi RSI(14) < 42."
        },
        "tranche_2": {
            "name": "Tranche 2: Điểm Mua Giá Trị Chuẩn Mực (MOS)",
            "capital_weight": "40% Vị thế",
            "trigger_price": round(p_t2, 0),
            "is_in_buy_zone": current_price <= p_t2,
            "reachability": eval_reachability(p_t2),
            "conditions": f"Chiết khấu chuẩn MOS động ~{int(round((1 - p_t2/fair_value)*100))}% từ Fair Value (Hội tụ 10 Cap & Payback 8Y).",
            "execution": "Giải ngân 40% vốn chủ lực khi thị trường điều chỉnh trung hạn 12%–15% hoặc khối ngoại cơ cấu."
        },
        "tranche_3": {
            "name": "Tranche 3: Điểm Mua Khủng Hoảng / Sàn Sổ Sách",
            "capital_weight": "30% Còn Lại",
            "trigger_price": round(p_t3, 0),
            "is_in_buy_zone": current_price <= p_t3,
            "reachability": eval_reachability(p_t3),
            "conditions": f"Chiết khấu sâu ~{int(round((1 - p_t3/fair_value)*100))}% từ Fair Value (Neo dải -2SD & Sàn P/B ~1.0x BVPS).",
            "execution": "Lưới đỡ cuối cùng khi có cú sốc vĩ mô / giải chấp chéo (Call Margin); tất tay phần tiền mặt dự phòng."
        },
        "p_worst": round(p_worst, 0),
        "win_loss_ratio": win_loss_ratio,
        "target_sell_1": round(fair_value, 0),
        "target_sell_2": round(max(fair_value * 1.25, fair_value + (fair_value - p_t1) * 1.5), 0)
    }

def calculate_master_fair_value_and_targets(
    intrinsic_convergence_price: float,
    relative_price: float,
    current_price: float,
    mos_pct: float = 20.0,
    pe_overheat_price: float = None
) -> Dict[str, Any]:
    """
    Thuật toán Phối hợp Trọng số Chuẩn Thực Chiến V3.0:
    - intrinsic_convergence_price: Giá trị Hợp lý Nội tại Hội tụ (CHƯA TRỪ MOS — Pre-MOS Intrinsic Fair Value).
    - relative_price: Giá trị Hợp lý Tương đối Đa Bội Số (Pre-MOS Relative Fair Value).
    - P_fair = 70% P_nội_tại_Fair + 30% P_tương_đối_Fair.
    - P_buy = P_fair * (1 - MOS_pct) -> Đảm bảo Biên an toàn MOS chỉ trừ ĐÚNG 1 LẦN DUY NHẤT!
    """
    fair_value_blended = (0.70 * intrinsic_convergence_price) + (0.30 * relative_price)
    p_buy = fair_value_blended * (1.0 - mos_pct / 100.0)
    
    # Mốc bán 1: Về giá trị thực hợp lý (Fair Value)
    p_sell_1 = fair_value_blended
    
    # Mốc bán 2: Vùng quá nhiệt hưng phấn (+1.5SD PE hoặc Fair Value + 25%)
    p_sell_2 = pe_overheat_price if pe_overheat_price and pe_overheat_price > fair_value_blended * 1.12 else (fair_value_blended * 1.25)
    
    downside_risk = max(current_price * 0.05, current_price - p_buy) if current_price > p_buy else (current_price * 0.08)
    upside_gain = max(0.0, p_sell_1 - current_price) if p_sell_1 > current_price else max(0.0, p_sell_2 - current_price)
    win_loss_ratio = round(upside_gain / downside_risk, 2)
    
    return {
        "master_fair_value": round(fair_value_blended, 0),
        "intrinsic_fair_value": round(intrinsic_convergence_price, 0),
        "relative_fair_value": round(relative_price, 0),
        "target_buy_price": round(p_buy, 0),
        "target_sell_1": round(p_sell_1, 0),
        "target_sell_2": round(p_sell_2, 0),
        "win_loss_ratio": win_loss_ratio
    }

def calculate_blended_valuation(
    data: Dict[str, Any],
    custom_params: Dict[str, Any] = None
) -> Dict[str, Any]:
    """
    Hợp nhất các phương pháp định giá theo ma trận trọng số tối ưu của từng ngành nghề.
    """
    params = custom_params or {}
    sector = data.get("sector", "CYCLICAL_MANUFACTURING")
    
    models_output = []
    blended_price = 0.0
    
    if sector == "BANKING":
        # 1. Residual Income (40%)
        ke = params.get("cost_of_equity", data.get("cost_of_equity", 11.5))
        roe = params.get("roe_expected", data.get("roe_expected", 21.0))
        g = params.get("growth_lt", data.get("growth_longterm_default", 4.5))
        ri_res = calculate_banking_residual_income(data, cost_of_equity=ke, roe_expected=roe, growth_lt=g)
        
        # 2. P/B Điều chỉnh (40%)
        pb_target = params.get("target_pb", data.get("peer_pb_median", 1.85))
        pb_res = calculate_banking_adjusted_pb(data, target_pb=pb_target)
        
        # 3. P/E Ngành (20%)
        pe_target = params.get("target_pe", data.get("peer_pe_median", 10.5))
        rel_res = calculate_relative_multiples(data, custom_pe=pe_target)
        
        models_output = [
            {"method": "Thu nhập Thặng dư (Residual Income)", "fair_value": ri_res["fair_value"], "weight": 0.40},
            {"method": "P/B Điều chỉnh Chất lượng Tài sản", "fair_value": pb_res["fair_value"], "weight": 0.40},
            {"method": "P/E Ngành Ngân hàng", "fair_value": rel_res["pe_valuation"], "weight": 0.20}
        ]

    elif sector == "SECURITIES":
        # 2. Công ty Chứng khoán (CTCK)
        # Mark-to-Market NAV (40%) + BVPS Compounding (35%) + P/B phân tầng (25%)
        raw_bvps = data.get("bvps", 18000.0)
        pb_target = params.get("target_pb", data.get("peer_pb_median", 2.2))
        rel_res = calculate_relative_multiples(data, custom_pb=pb_target, custom_pe=params.get("target_pe", 14.0))
        nav_mtm = raw_bvps * 1.15 # Đánh giá lại danh mục FVTPL
        models_output = [
            {"method": "Đánh giá lại Danh mục Tự doanh (Mark-to-Market NAV)", "fair_value": round(nav_mtm, 0), "weight": 0.40},
            {"method": "P/B Phân tầng theo Thị phần & Dư nợ Margin", "fair_value": rel_res["pb_valuation"], "weight": 0.35},
            {"method": "P/E Thanh khoản Thị trường", "fair_value": rel_res["pe_valuation"], "weight": 0.25}
        ]

    elif sector == "INSURANCE":
        # 3. Bảo hiểm (Nhân thọ & Phi nhân thọ)
        # DDM Cổ tức (40%) + Residual Income (35%) + P/B - ROE (25%)
        raw_bvps = data.get("bvps", 22000.0)
        pb_target = params.get("target_pb", 1.6)
        div_yield_val = data.get("dividend_yield", 6.0)
        div_fair = (raw_bvps * 0.12 * 0.5) / 0.08 # DDM bảo hiểm
        rel_res = calculate_relative_multiples(data, custom_pb=pb_target)
        models_output = [
            {"method": "Chiết khấu Cổ tức Tiền mặt (DDM Bảo hiểm)", "fair_value": round(div_fair, 0), "weight": 0.40},
            {"method": "P/B Hưởng lợi Lợi suất Trái phiếu (Rf)", "fair_value": rel_res["pb_valuation"], "weight": 0.35},
            {"method": "P/E Kết hợp Combined Ratio", "fair_value": rel_res["pe_valuation"], "weight": 0.25}
        ]
        
    elif sector == "REAL_ESTATE":
        # 1. RNAV Dự án (65%)
        rnav_res = calculate_real_estate_rnav(data)
        
        # 2. P/B Ngành (20%)
        pb_target = params.get("target_pb", data.get("peer_pb_median", 1.45))
        rel_res = calculate_relative_multiples(data, custom_pb=pb_target)
        
        # 3. P/E Dự phóng (15%)
        pe_target = params.get("target_pe", data.get("peer_pe_median", 9.0))
        
        models_output = [
            {"method": "RNAV Chiết khấu Dự án & Quỹ đất", "fair_value": rnav_res["fair_value"], "weight": 0.65},
            {"method": "P/B Ngành Bất động sản", "fair_value": rel_res["pb_valuation"], "weight": 0.20},
            {"method": "P/E Dự phóng", "fair_value": rel_res["pe_valuation"], "weight": 0.15}
        ]
        
    elif sector == "ELECTRICAL_EQUIPMENT":
        # Ngành Thiết bị điện & Năng lượng (GEE, VNE, TV2...)
        # 1. DCF FCFF (40%) - Tăng trưởng hưởng lợi Quy hoạch điện 8
        wacc = params.get("wacc", data.get("wacc_default", 11.0))
        g = params.get("growth_lt", data.get("growth_longterm_default", 3.5))
        dcf_res = calculate_dcf_fcff(data, wacc=wacc, growth_lt=g)
        
        # 2. EV/EBITDA (35%)
        ev_target = params.get("target_ev_ebitda", data.get("peer_ev_ebitda_median", 8.5))
        rel_res = calculate_relative_multiples(data, custom_ev_ebitda=ev_target, custom_pe=params.get("target_pe", data.get("peer_pe_median", 14.5)))
        
        # 3. P/E Chuẩn hóa cốt lõi (25%) - Đã loại trừ lợi nhuận đột biến bán dự án
        models_output = [
            {"method": "DCF FCFF (Dòng tiền Sản xuất Thiết bị điện)", "fair_value": dcf_res["fair_value"], "weight": 0.40},
            {"method": "EV/EBITDA Ngành Thiết bị Công nghiệp", "fair_value": rel_res["ev_ebitda_valuation"], "weight": 0.35},
            {"method": "P/E Chuẩn hóa Cốt lõi (Core EPS)", "fair_value": rel_res["pe_valuation"], "weight": 0.25}
        ]

    elif sector == "CYCLICAL_MANUFACTURING":
        # 1. EV/EBITDA (35%)
        ev_target = params.get("target_ev_ebitda", data.get("peer_ev_ebitda_median", 6.8))
        rel_res = calculate_relative_multiples(data, custom_ev_ebitda=ev_target)
        
        # 2. DCF Chuẩn hóa (25%)
        wacc = params.get("wacc", data.get("wacc_default", 11.5))
        g = params.get("growth_lt", data.get("growth_longterm_default", 3.0))
        dcf_res = calculate_dcf_fcff(data, wacc=wacc, growth_lt=g)
        
        # 3. P/E Chuẩn hóa Chu kỳ (20%)
        pe_target = params.get("target_pe", data.get("peer_pe_median", 8.5))
        
        # 4. P/B Chu kỳ (20%)
        pb_target = params.get("target_pb", data.get("peer_pb_median", 1.35))
        
        models_output = [
            {"method": "EV/EBITDA (Chuẩn hóa đòn bẩy & D&A)", "fair_value": rel_res["ev_ebitda_valuation"], "weight": 0.35},
            {"method": "DCF Chiết khấu FCFF", "fair_value": dcf_res["fair_value"], "weight": 0.25},
            {"method": "P/E Chuẩn hóa Chu kỳ (5 năm)", "fair_value": rel_res["pe_valuation"], "weight": 0.20},
            {"method": "P/B Chu kỳ", "fair_value": rel_res["pb_valuation"], "weight": 0.20}
        ]
        
    else: # TECHNOLOGY, RETAIL, UTILITIES...
        # 1. DCF FCFF (45%)
        wacc = params.get("wacc", data.get("wacc_default", 10.5))
        g = params.get("growth_lt", data.get("growth_longterm_default", 4.0))
        dcf_res = calculate_dcf_fcff(data, wacc=wacc, growth_lt=g)
        
        # 2. P/E (35%)
        pe_target = params.get("target_pe", data.get("peer_pe_median", 18.0))
        rel_res = calculate_relative_multiples(data, custom_pe=pe_target)
        
        # 3. P/B (20%)
        pb_target = params.get("target_pb", data.get("peer_pb_median", 3.5))
        
        models_output = [
            {"method": "DCF FCFF (Tăng trưởng dòng tiền)", "fair_value": dcf_res["fair_value"], "weight": 0.45},
            {"method": "P/E Tăng trưởng (PEG điều chỉnh)", "fair_value": rel_res["pe_valuation"], "weight": 0.35},
            {"method": "P/B Giá trị Sổ sách", "fair_value": rel_res["pb_valuation"], "weight": 0.20}
        ]
        
    # Tính giá trị tổng hợp
    for item in models_output:
        blended_price += item["fair_value"] * item["weight"]
        
    blended_price = round(blended_price, 0)
    
    return {
        "sector": sector,
        "blended_fair_value": blended_price,
        "models": models_output
    }

def generate_sensitivity_matrix(
    data: Dict[str, Any],
    base_wacc: float = 11.5,
    base_g: float = 3.0
) -> pd.DataFrame:
    """
    Sinh ma trận phân tích độ nhạy 2 chiều (WACC vs g) cho mô hình DCF.
    """
    wacc_range = [base_wacc - 1.5, base_wacc - 0.75, base_wacc, base_wacc + 0.75, base_wacc + 1.5]
    g_range = [base_g - 1.0, base_g - 0.5, base_g, base_g + 0.5, base_g + 1.0]
    
    matrix = []
    for w in wacc_range:
        row = []
        for g_val in g_range:
            res = calculate_dcf_fcff(data, wacc=w, growth_lt=g_val)
            row.append(res["fair_value"])
        matrix.append(row)
        
    df = pd.DataFrame(
        matrix,
        index=[f"WACC {round(w, 2)}%" for w in wacc_range],
        columns=[f"g = {round(g, 1)}%" for g in g_range]
    )
    return df
