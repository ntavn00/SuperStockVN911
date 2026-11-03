"""
rule_one_engine.py - Bộ máy Định giá Giá trị theo Trường phái Warren Buffett & Phil Town (Rule #1)
Bản địa hóa theo Chuẩn mực Kế toán Việt Nam (VAS / Thông tư 200 & Thông tư 99/2025/TT-BTC)
Gồm:
1. Xử lý Trích lập Quỹ Khen thưởng Phúc lợi (TK 353) & Pha loãng cổ phiếu
2. Tính toán Dòng tiền Chủ sở hữu (Owner Earnings) của Warren Buffett
3. Bộ tứ Định giá Hội tụ Phil Town: Sticker Price, Payback Time (8 năm), 10 Cap Price, Zombie Value
4. Tầng lọc Sức khỏe: Big Five (CAGR 5 năm >= 10%), Piotroski F-Score (thang điểm 9), Altman Z-Score
5. Thuật toán Biên An toàn Động (Dynamic Margin of Safety)
"""

import math
import pandas as pd
from typing import Dict, Any, List, Tuple

def calculate_adjusted_eps(
    net_profit_parent: float,
    tk353_welfare_fund: float,
    diluted_shares: int,
    pref_dividends: float = 0.0,
    reference_eps: float = 0.0
) -> Dict[str, Any]:
    """
    Công thức Chuẩn hóa EPS thực nhận của cổ đông theo Thông tư 200/2014 & TT 99/2025/TT-BTC:
    Adjusted EPS = (LNST CĐ Cty Mẹ - Trích Quỹ KTPL TK 353 - Cổ tức CP Ưu đãi) / Diluted Shares
    Đơn vị tiền: Tỷ VNĐ; Đơn vị CP: Cổ phiếu.
    Hỗ trợ đồng bộ với EPS TTM chuẩn hóa (reference_eps) để chống lệch pha khi chia cổ tức cổ phiếu.
    """
    if diluted_shares <= 0:
        return {"adjusted_eps": 0.0, "raw_eps": 0.0, "tk353_deduction": 0.0}
        
    computed_raw_eps = (net_profit_parent * 1e9) / diluted_shares
    raw_eps = max(computed_raw_eps, reference_eps) if reference_eps > 0 else computed_raw_eps
    
    tk353_ratio = (tk353_welfare_fund / net_profit_parent) if net_profit_parent > 0 else 0.05
    tk353_ratio = min(0.25, max(0.0, tk353_ratio))
    pref_per_share = (pref_dividends * 1e9) / diluted_shares
    
    adjusted_eps = max(0.0, raw_eps * (1.0 - tk353_ratio) - pref_per_share)
    leakage_pct = ((raw_eps - adjusted_eps) / raw_eps * 100.0) if raw_eps > 0 else 0.0
    
    return {
        "raw_eps": round(raw_eps, 0),
        "adjusted_eps": round(adjusted_eps, 0),
        "tk353_deduction_bil": round(tk353_welfare_fund, 1),
        "leakage_pct": round(leakage_pct, 1)
    }

def calculate_owner_earnings(
    data: Dict[str, Any],
    tk353_welfare_fund: float = None
) -> Dict[str, Any]:
    """
    Dòng tiền Chủ sở hữu (Owner Earnings) của Warren Buffett:
    OE = LNST TTM + Khấu hao D&A - Maintenance Capex +/- Biến động Vốn lưu động - Trích TK 353
    """
    shares = data.get("shares_outstanding", 1)
    net_profit_series = data.get("net_profit", [1000])
    net_profit = float(data.get("net_profit_ttm") or net_profit_series[-1])
    
    # Đảm bảo đồng bộ với EPS TTM nếu công ty vừa chia tách cổ phiếu
    eps_curr = float(data.get("eps_current", 0.0))
    if eps_curr > 0 and shares > 0:
        implied_np = (eps_curr * shares) / 1e9
        net_profit = max(net_profit, implied_np)
        
    da = float(data.get("da", [300])[-1])
    capex = float(data.get("capex", [400])[-1])
    
    # Ước tính bảo thủ Maintenance Capex (Capex duy trì công suất hiện hữu):
    # Trong giai đoạn mở rộng nhà máy (Capex >> D&A), phần vượt trên D&A là Growth Capex.
    maintenance_capex = min(capex, da * 0.95) if capex > da else (capex * 0.90)
    
    tk353 = tk353_welfare_fund if tk353_welfare_fund is not None else data.get("welfare_fund_tk353", net_profit * 0.05)
    
    owner_earnings_bil = net_profit + da - maintenance_capex - tk353
    owner_earnings_bil = max(net_profit * 0.80, owner_earnings_bil)
    
    oe_per_share = (owner_earnings_bil * 1e9) / shares if shares > 0 else 0.0
    
    return {
        "owner_earnings_bil": round(owner_earnings_bil, 1),
        "oe_per_share": round(oe_per_share, 0),
        "maintenance_capex_bil": round(maintenance_capex, 1),
        "tk353_bil": round(tk353, 1),
        "net_profit_used": round(net_profit, 1),
        "da_used": round(da, 1)
    }

def calculate_sticker_price_rule_one(
    eps_0: float,
    cagr_bvps: float,
    cagr_analysts: float,
    historical_pe_5y: float,
    marr: float = 15.0,
    mos_pct: float = 25.0,
    sector_g_cap: float = 25.0,
    use_decay_growth: bool = True,
    beta: float = 1.0,
    rf_rate: float = 4.58,
    erp_rate: float = 7.5,
    dividend_yield: float = 2.5
) -> Dict[str, Any]:
    """
    Phương pháp Giá Niêm Yết (Sticker Price) và Giá MOS của Phil Town (Rule #1).
    Nâng cấp Chuẩn Định LượngThực Chiến V3.0 (Data-Driven Quant Engine):
    1. Tốc độ Tăng trưởng Giảm dần (Decay / Fade to Vietnam Nominal GDP Growth):
       - 5 năm đầu: Tăng trưởng ở mức g = min(cagr_bvps, cagr_analysts, sector_g_cap)
       - 5 năm tiếp theo: Fade dần mỗi năm 10% về mức tăng trưởng danh nghĩa dài hạn VN (6.5%/năm, thay vì 3.5% của Mỹ).
    2. Khắc phục Bẫy Chiết Khấu Kép & Rò Rỉ Cổ Tức trong giai đoạn Fade:
       - Tính đến tổng lợi suất cổ tức tiền mặt tái đầu tư trong 10 năm (Total Shareholder Return discounting).
       - P/E tương lai kết hợp hài hòa giữa P/E nền tảng tăng trưởng (Graham/Town) và P/E lịch sử 5 năm.
    """
    # 1. Tốc độ tăng trưởng bảo thủ (Chặn trần 16.5%/năm cho chu kỳ 10 năm để chống hàm mũ g^10 thổi phồng)
    g = min(cagr_bvps, cagr_analysts, sector_g_cap, 16.5)
    g = max(5.0, g)
    g_dec = g / 100.0
    
    # 2. Phóng chiếu EPS năm thứ 10 & Khấu trừ cổ tức tiền mặt hợp lý
    ke_rate = max(10.5, min(14.5, rf_rate + (beta * erp_rate)))
    ke_dec = ke_rate / 100.0
    div_credit = min(0.02, max(0.01, (dividend_yield / 100.0) * 0.5))
    ke_net_dec = max(0.095, ke_dec - div_credit)
    
    if use_decay_growth:
        current_eps = eps_0
        # Giai đoạn 1 (Năm 1-5): Tăng trưởng tốc độ g
        for _ in range(5):
            current_eps *= (1.0 + g_dec)
        # Giai đoạn 2 (Năm 6-10): Fade dần mỗi năm 15% về mức tăng trưởng danh nghĩa dài hạn 5.5%
        fade_g = g_dec
        for _ in range(5):
            fade_g = max(0.055, fade_g * 0.85)
            current_eps *= (1.0 + fade_g)
        future_eps_10 = current_eps
    else:
        # Mô hình tuyến tính cổ điển của Phil Town: EPS_0 * (1 + g)^10
        future_eps_10 = eps_0 * ((1.0 + g_dec) ** 10)
    
    # 3. P/E tương lai bảo thủ theo chuẩn Phil Town: min(2*g, P/E lịch sử 5Y, 18.5x)
    default_pe = 2.0 * g
    future_pe = min(default_pe, historical_pe_5y, 18.5)
    future_pe = max(7.5, future_pe)
    
    # 4. Giá tương lai năm 10
    future_price_10 = future_eps_10 * future_pe
    
    # 5. Sticker Price Cổ Điển (Chiết khấu 10 năm với MARR = 15% thuần giá)
    marr_dec = marr / 100.0
    sticker_price_classic = future_price_10 / ((1.0 + marr_dec) ** 10)
    mos_price_classic = sticker_price_classic * 0.50 # Phil Town 50%
    
    # 6. Sticker Price Thích Ứng Chi Phí Vốn Thực Tế Ke (Fair Value Pre-MOS)
    sticker_price_ke = future_price_10 / ((1.0 + ke_net_dec) ** 10)
    mos_price_ke = sticker_price_ke * (1.0 - mos_pct / 100.0)
    
    primary_sticker = sticker_price_ke
    primary_mos = mos_price_ke
    
    return {
        "model_name": "Rule #1 Sticker Price Thích Ứng (Phil Town & Modern Ke V3.0)",
        "eps_0": round(eps_0, 0),
        "growth_rate_used": round(g, 1),
        "use_decay_growth": use_decay_growth,
        "future_eps_10": round(future_eps_10, 0),
        "future_pe": round(future_pe, 1),
        "future_price_10": round(future_price_10, 0),
        "marr": marr,
        "ke_rate": round(ke_rate, 2),
        "sticker_price": max(0.0, round(primary_sticker, 0)),
        "mos_pct": mos_pct,
        "mos_price": max(0.0, round(primary_mos, 0)),
        "sticker_price_classic": max(0.0, round(sticker_price_classic, 0)),
        "mos_price_classic": max(0.0, round(mos_price_classic, 0)),
        "sticker_price_ke": max(0.0, round(sticker_price_ke, 0)),
        "mos_price_ke": max(0.0, round(mos_price_ke, 0))
    }

def calculate_payback_time(
    fcf_0_per_share: float,
    growth_rate: float,
    current_price: float,
    years: int = 8,
    max_acceptable_years: int = 8
) -> Dict[str, Any]:
    """
    Phương pháp Thời Gian Hoàn Vốn Thực Nghiệm (Real Purchasing Power Payback Time V3.0):
    Khắc phục lỗi cộng ngang dòng tiền danh nghĩa không chiết khấu lạm phát (r=0%) khiến cổ phiếu tăng trưởng bị thổi phồng:
    Chiết khấu sức mua thực tế với tỷ lệ trượt giá đồng tiền 5.0%/năm tại Việt Nam:
    g_real = (1 + g) / (1 + 0.05) - 1
    - payback_price_8y: Giá Mua An Toàn (MOS Buy Price) hoàn vốn sức mua thực trong 8 năm.
    - payback_price_10y: Giá Trị Hợp Lý (Fair Value Pre-MOS) hoàn vốn sức mua thực trong 10 năm.
    """
    g_nom = max(0.02, min(0.165, growth_rate / 100.0))
    inflation_erosion = 0.05 # Trượt giá sức mua 5%/năm tại VN
    g_dec = max(0.01, (1.0 + g_nom) / (1.0 + inflation_erosion) - 1.0)
    
    if g_dec > 0:
        payback_price_8y = fcf_0_per_share * (1.0 + g_dec) * (((1.0 + g_dec) ** years - 1.0) / g_dec)
        payback_price_10y = fcf_0_per_share * (1.0 + g_dec) * (((1.0 + g_dec) ** 10 - 1.0) / g_dec)
    else:
        payback_price_8y = fcf_0_per_share * years
        payback_price_10y = fcf_0_per_share * 10
        
    actual_years = None
    if fcf_0_per_share > 0 and current_price > 0:
        try:
            val_inside = 1.0 + (current_price * g_dec) / (fcf_0_per_share * (1.0 + g_dec))
            if val_inside > 0:
                actual_years = math.log(val_inside) / math.log(1.0 + g_dec)
                actual_years = round(actual_years, 1)
        except Exception:
            actual_years = None
            
    is_buy_zone = (actual_years is not None and actual_years <= max_acceptable_years)
    
    return {
        "model_name": f"Payback Time (Thời gian Hoàn vốn {years} năm)",
        "payback_price_8y": max(0.0, round(payback_price_8y, 0)),
        "payback_price_10y": max(0.0, round(payback_price_10y, 0)),
        "fair_payback_value": max(0.0, round(payback_price_10y, 0)),
        "fcf_0_per_share": round(fcf_0_per_share, 0),
        "growth_rate": growth_rate,
        "actual_payback_years": actual_years,
        "target_years": years,
        "max_acceptable_years": max_acceptable_years,
        "is_buy_zone": is_buy_zone
    }

def calculate_ten_cap_price(
    owner_earnings_per_share: float,
    growth_rate: float = 12.0,
    ke_rate: float = 12.0
) -> Dict[str, Any]:
    """
    Phương pháp 10 Cap Price & Định giá Dòng tiền Chủ sở hữu (Warren Buffett & Phil Town):
    - ten_cap_price = Owner Earnings * 10 (Mức Giá Mua An Toàn đòi hỏi lợi suất tiền mặt tức thời 10%/năm).
    - oe_fair_value = Giá trị Hợp lý Nội tại (Fair Value Pre-MOS) của Owner Earnings:
      Multiple hợp lý = min(14.5, max(10.5, 9.0 + 0.30 * g)).
    """
    ten_cap_price = owner_earnings_per_share * 10.0
    g_clean = max(5.0, min(18.0, growth_rate))
    oe_fair_multiple = min(14.5, max(10.5, 9.0 + 0.30 * g_clean))
    oe_fair_value = owner_earnings_per_share * oe_fair_multiple
    
    return {
        "model_name": "10 Cap Price & Owner Earnings Valuation (Buffett)",
        "oe_per_share": round(owner_earnings_per_share, 0),
        "ten_cap_price": max(0.0, round(ten_cap_price, 0)),
        "oe_fair_value": max(0.0, round(oe_fair_value, 0)),
        "oe_fair_multiple": round(oe_fair_multiple, 1)
    }

def calculate_zombie_value(
    data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Giá trị Xác sống / Thanh lý (Zombie Value / Net-Net của Ben Graham):
    Zombie Value = [Tiền mặt + 0.75 * Phải thu + 0.5 * Tồn kho - Tổng Nợ phải trả] / Số CP
    """
    cash = data.get("cash_and_investments", 0) # Tỷ
    receivables = data.get("receivables", cash * 0.8)
    inventory = data.get("inventory", cash * 0.5)
    total_liabilities = data.get("total_debt", 0) * 1.3 # Ước lượng tổng nợ phải trả
    
    liquidation_value_bil = cash + (0.75 * receivables) + (0.5 * inventory) - total_liabilities
    shares = data.get("shares_outstanding", 1)
    
    zombie_val_per_share = (liquidation_value_bil * 1e9) / shares if shares > 0 else 0.0
    
    return {
        "model_name": "Zombie Value (Net-Net Ben Graham)",
        "liquidation_value_bil": round(liquidation_value_bil, 1),
        "zombie_price": max(0.0, round(zombie_val_per_share, 0)),
        "cash_bil": cash,
        "total_liabilities_bil": round(total_liabilities, 1)
    }

# ---------------------------------------------------------
# BỘ 3 CÔNG THỨC ĐỊNH GIÁ BENJAMIN GRAHAM BẢN ĐỊA HÓA (VIETNAM)
# ---------------------------------------------------------

def calculate_benjamin_graham_trio(
    eps_adjusted: float,
    bvps_adjusted: float,
    growth_rate: float,
    rf_10y_bond: float = 4.58
) -> Dict[str, Any]:
    """
    Bộ 3 Công thức Định giá Cổ điển của Benjamin Graham (Bản địa hóa thị trường VN):
    1. Graham 1 (Tăng trưởng cơ bản): IV_1 = EPS * (8.5 + 2*g)
    2. Graham 2 (Điều chỉnh TPCP VN 10Y): IV_2 = EPS * (8.5 + 2*g) * 4.4 / (Rf + 0.5%)
    3. Graham Number (Con số Graham): P_graham = sqrt(22.5 * EPS * BVPS)
    """
    g = max(1.0, min(20.0, growth_rate)) # g tính theo số nguyên (ví dụ 10% -> 10)
    
    # 1. Graham 1
    iv_graham_1 = max(0.0, eps_adjusted * (8.5 + 2.0 * g))
    
    # 2. Graham 2 (Điều chỉnh Lợi suất Trái phiếu Chính phủ Việt Nam 10 năm)
    y_vn = rf_10y_bond + 0.5 # Lãi suất tham chiếu doanh nghiệp chuẩn
    iv_graham_2 = max(0.0, eps_adjusted * (8.5 + 2.0 * g) * 4.4 / y_vn) if y_vn > 0 else iv_graham_1
    
    # 3. Graham Number
    if eps_adjusted > 0 and bvps_adjusted > 0:
        graham_number = math.sqrt(22.5 * eps_adjusted * bvps_adjusted)
    else:
        graham_number = 0.0
        
    return {
        "model_name": "Bộ 3 Công Thức Benjamin Graham",
        "graham_1_price": round(iv_graham_1, 0),
        "graham_2_price": round(iv_graham_2, 0),
        "graham_number": round(graham_number, 0),
        "rf_used": rf_10y_bond,
        "y_vn_used": round(y_vn, 2),
        "g_used": round(g, 1)
    }

def calculate_roce(data: Dict[str, Any]) -> float:
    """
    Tỷ suất Sinh lời trên Vốn Sử dụng (ROCE):
    ROCE = EBIT / (Tổng Tài Sản - Nợ Ngắn Hạn) * 100%
    Đo lường hiệu quả sinh lời của các ngành thâm dụng vốn (Thép, Điện, Hóa chất, Cảng).
    """
    ebit = data.get("ebit", [1000])[-1]
    equity = data.get("equity", 5000)
    debt = data.get("total_debt", 3000)
    total_assets = data.get("total_assets") or (equity + debt * 1.2)
    short_term_debt = data.get("short_term_debt") or (debt * 0.5)
    
    capital_employed = total_assets - short_term_debt
    if capital_employed > 0:
        return round((ebit / capital_employed) * 100.0, 1)
    return 12.0

# ---------------------------------------------------------
# TẦNG LỌC SỨC KHỎE TIỀN ĐỊNH GIÁ (PRE-VALUATION GATEKEEPERS)
# ---------------------------------------------------------

def calculate_big_five_cagr(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Bộ 5 Tiêu chí Con hào Kinh tế (Big Five Moat của Phil Town):
    Yêu cầu CAGR 5 năm >= 10% trên:
    1. Doanh thu thuần
    2. EPS pha loãng
    3. Giá trị sổ sách BVPS / Vốn chủ sở hữu
    4. Dòng tiền kinh doanh CFO / FCF
    5. Tỷ suất ROIC >= 10%
    """
    rev = data.get("revenue", [])
    np_profit = data.get("net_profit", [])
    cfo = data.get("cfo", [])
    
    def calc_cagr(series):
        clean_s = [float(x) for x in series if x and float(x) > 0]
        if len(clean_s) >= 2:
            n = len(clean_s) - 1
            full_cagr = ((clean_s[-1] / clean_s[0]) ** (1.0 / n) - 1.0) * 100.0
            # Nếu năm đầu tiên rơi đúng đỉnh chu kỳ (như 2021-2022 ngành thép/bán lẻ), kiểm tra thêm CAGR phục hồi 3 năm gần nhất
            if len(clean_s) >= 3:
                rec_cagr = ((clean_s[-1] / clean_s[-3]) ** 0.5 - 1.0) * 100.0
                best_cagr = 0.65 * full_cagr + 0.35 * max(full_cagr, min(35.0, rec_cagr))
                return round(best_cagr, 1)
            return round(full_cagr, 1)
        return 10.0 # default
        
    cagr_rev = calc_cagr(rev)
    cagr_eps = calc_cagr(np_profit)
    cagr_cfo = calc_cagr(cfo)
    cagr_bvps = float(data.get("cagr_bvps", 12.0))
    roic = float(data.get("roic", 14.5))
    
    criteria = [
        {"name": "1. Tăng trưởng Doanh thu (Sales CAGR)", "val": cagr_rev, "threshold": 10.0, "pass": cagr_rev >= 10.0},
        {"name": "2. Tăng trưởng EPS (EPS CAGR)", "val": cagr_eps, "threshold": 10.0, "pass": cagr_eps >= 10.0},
        {"name": "3. Tăng trưởng Vốn CSH (BVPS CAGR)", "val": cagr_bvps, "threshold": 10.0, "pass": cagr_bvps >= 10.0},
        {"name": "4. Tăng trưởng Dòng tiền (CFO CAGR)", "val": cagr_cfo, "threshold": 10.0, "pass": cagr_cfo >= 10.0},
        {"name": "5. Tỷ suất ROIC bình quân", "val": roic, "threshold": 10.0, "pass": roic >= 10.0}
    ]
    
    passed_count = sum(1 for c in criteria if c["pass"])
    
    return {
        "criteria": criteria,
        "passed_count": passed_count,
        "total_criteria": 5,
        "has_strong_moat": (passed_count >= 4)
    }

def calculate_piotroski_f_score(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Thang điểm Piotroski F-Score (0 đến 9 điểm):
    Đo lường Khả năng sinh lời, Đòn bẩy/Thanh khoản, và Hiệu quả hoạt động.
    """
    np_profit = data.get("net_profit", [100, 120])
    equity = data.get("equity", 1000)
    debt = data.get("total_debt", 500)
    cfo = data.get("cfo", [120, 150])
    rev = data.get("revenue", [1000, 1200])
    gross_profit = data.get("gross_profit", [200, 260])
    
    latest_np = np_profit[-1] if np_profit else 100
    prev_np = np_profit[-2] if len(np_profit) > 1 else latest_np * 0.9
    latest_cfo = cfo[-1] if cfo else 120
    
    # 9 Tiêu chí:
    f1 = 1 if latest_np > 0 else 0                           # ROA > 0
    f2 = 1 if latest_cfo > 0 else 0                          # CFO > 0
    f3 = 1 if latest_np >= prev_np else 0                    # delta ROA > 0
    f4 = 1 if latest_cfo > latest_np else 0                  # CFO > Net Profit (Chất lượng LN cao, ko xào nấu)
    f5 = 1 if (debt / equity) <= 1.2 else 0                  # Đòn bẩy nợ an toàn
    f6 = 1 if data.get("current_ratio", 1.5) >= 1.2 else 0   # Khả năng thanh toán ngắn hạn
    f7 = 1                                                   # Không pha loãng cổ phiếu bất thường
    f8 = 1 if (gross_profit[-1] / rev[-1] if rev and rev[-1] > 0 else 0.15) >= 0.12 else 0 # Biên lãi gộp
    f9 = 1 if (rev[-1] >= rev[-2] if len(rev) > 1 else True) else 0 # Vòng quay doanh thu
    
    score = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9
    
    if score >= 7:
        assessment = "Xuất sắc (Nền tảng tài chính lành mạnh vượt trội - Winners)"
        color = "#10B981"
    elif score >= 5:
        assessment = "Trung bình Ổn định (Tài chính chấp nhận được)"
        color = "#F59E0B"
    else:
        assessment = "Kém / Cảnh báo Rủi ro cao (Losers / Nguy cơ suy thoái)"
        color = "#EF4444"
        
    return {
        "f_score": score,
        "max_score": 9,
        "assessment": assessment,
        "color": color,
        "details": [
            ("Lợi nhuận ròng dương (ROA > 0)", f1 == 1),
            ("Dòng tiền kinh doanh CFO dương", f2 == 1),
            ("Lợi nhuận cải thiện so với năm trước", f3 == 1),
            ("Dòng tiền CFO lớn hơn LNST (Không xào nấu)", f4 == 1),
            ("Đòn bẩy Nợ/Vốn CSH an toàn", f5 == 1),
            ("Hệ số thanh toán hiện hành tốt", f6 == 1),
            ("Không pha loãng cổ đông bất lợi", f7 == 1),
            ("Biên lợi nhuận gộp vững vàng", f8 == 1),
            ("Doanh thu thuần tăng trưởng", f9 == 1)
        ]
    }

def calculate_altman_z_score(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Altman Z''-Score cho Thị trường Mới nổi (Emerging Markets):
    Z'' = 6.56*X1 + 3.26*X2 + 6.72*X3 + 1.05*X4
    """
    sector = data.get("sector", "")
    if sector == "BANKING":
        return {
            "z_score": 3.5,
            "zone": "Không áp dụng cho Ngân hàng (Miễn trừ chuẩn)",
            "color": "#6B7280"
        }
        
    equity = data.get("equity", 1000)
    debt = data.get("total_debt", 500)
    ebit = data.get("ebit", [200])[-1]
    
    total_assets = equity + debt
    working_capital = data.get("cash_and_investments", 200) + data.get("inventory", 100) - (debt * 0.4)
    retained_earnings = equity * 0.45
    
    # Xử lý đặc thù bán lẻ / tiêu dùng chiếm dụng vốn nhà cung cấp (Negative Working Capital trap):
    # Nếu CFO dương mạnh (>0) và EBIT dương, không phạt x1 âm quá sâu
    cfo_latest = data.get("cfo", [200])[-1] if data.get("cfo") else 200
    if working_capital < 0 and cfo_latest > 0 and ebit > 0:
        working_capital = max(working_capital, 0.0) # Chuẩn hóa về 0 để tránh sai số loại II của Altman Z
        
    x1 = working_capital / total_assets if total_assets > 0 else 0.1
    x2 = retained_earnings / total_assets if total_assets > 0 else 0.2
    x3 = ebit / total_assets if total_assets > 0 else 0.1
    x4 = equity / debt if debt > 0 else 2.0
    
    z_double_prime = 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4
    
    if z_double_prime > 2.60:
        zone = "Vùng An toàn (Safe Zone - Rủi ro phá sản cực thấp)"
        color = "#10B981"
    elif z_double_prime >= 1.10:
        zone = "Vùng Xám (Grey Zone - Cần theo dõi thêm về nợ)"
        color = "#F59E0B"
    else:
        zone = "Vùng Nguy hiểm (Distress Zone - Nguy cơ vỡ nợ cao)"
        color = "#EF4444"
        
    return {
        "z_score": round(z_double_prime, 2),
        "zone": zone,
        "color": color
    }

def calculate_dynamic_margin_of_safety(
    big_five_passed: int,
    f_score: int,
    z_score: float,
    sector: str,
    pe_core_market: float = 12.5
) -> Dict[str, Any]:
    """
    Thuật toán Định cỡ Biên An toàn Co Giãn Động (Dynamic Elastic MOS - Chuẩn Thực Chiến V3.0):
    MOS_Adaptive = MOS_Cơ sở - Delta_MOS_Chu kỳ (chỉ áp dụng 1 lần duy nhất lên Fair Value, tuyệt đối không trừ kép!)
    - Hạng 1 (Quality Compounders / Đầu ngành: Big Five >= 4 hoặc [Big Five >= 3 & F-Score >= 7]):
      MOS_Cơ sở = 20%. Nếu thị trường lõi ở vùng rẻ (PE_Core <= 12.5x), Delta_MOS = 5% => MOS = 15%.
    - Hạng 2 (Solid Value / Chu kỳ Đầu ngành: Big Five >= 2, F-Score >= 5, Z-Score >= 1.1):
      MOS_Cơ sở = 25% (Nếu thị trường lõi rẻ => MOS = 20%).
    - Hạng 3 (Rủi ro cao / Vùng xám: F-Score <= 4 hoặc Z-Score Nguy hiểm):
      MOS_Cơ sở = 35% (Nếu thị trường lõi rẻ => MOS = 30%).
    """
    is_cheap_cycle = (pe_core_market <= 12.5)
    delta_mos_cycle = 5.0 if is_cheap_cycle else 0.0

    is_safe_z = (z_score > 1.8 or sector in ["BANKING", "SECURITIES", "INSURANCE"])
    if (big_five_passed >= 4 or (big_five_passed >= 3 and f_score >= 7)) and f_score >= 6 and is_safe_z:
        tier_code = "TIER_1"
        base_mos = 20.0
        recommended_mos = max(15.0, base_mos - delta_mos_cycle)
        tier = "Hạng 1 (Quality Compounders — Con hào kinh tế độc quyền, Tài chính vượt trội)"
        advice = f"Biên an toàn thực chiến {int(recommended_mos)}% trên Fair Value (Khắc phục triệt để bẫy đứng ngoài thị trường)."
    elif big_five_passed >= 2 and f_score >= 5 and (z_score >= 1.1 or sector in ["BANKING", "SECURITIES", "INSURANCE"]):
        tier_code = "TIER_2"
        base_mos = 25.0
        recommended_mos = max(20.0, base_mos - delta_mos_cycle)
        tier = "Hạng 2 (Solid Value — Doanh nghiệp Đầu ngành / Tài chính lành mạnh)"
        advice = f"Áp dụng Biên an toàn cân bằng {int(recommended_mos)}% phù hợp nhịp điều chỉnh trung hạn hàng năm."
    else:
        tier_code = "TIER_3"
        base_mos = 35.0
        recommended_mos = max(30.0, base_mos - delta_mos_cycle)
        tier = "Hạng 3 (Chu kỳ sâu / Vùng xám — Rủi ro Đòn bẩy hoặc Moat yếu)"
        advice = f"Bắt buộc Biên an toàn phòng thủ {int(recommended_mos)}% để bảo vệ vốn trước biến động chu kỳ."
        
    return {
        "recommended_mos_pct": recommended_mos,
        "base_mos_pct": base_mos,
        "delta_mos_cycle": delta_mos_cycle,
        "tier": tier,
        "tier_code": tier_code,
        "is_cheap_cycle": is_cheap_cycle,
        "advice": advice
    }
