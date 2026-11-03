import os
import sys
import json
import pandas as pd
import numpy as np
from datetime import datetime

# Đảm bảo UTF-8
sys.stdout.reconfigure(encoding='utf-8')

from market_data import fetch_stock_financials_auto, get_live_stock_info
import rule_one_engine as r1
import valuation_engine as ve

symbol = "GEE"
info = get_live_stock_info(symbol)
fin = fetch_stock_financials_auto(symbol)

current_price = info.get("current_price", 66300.0)
shares = fin.get("shares_outstanding", 640499211)
latest_np = fin.get("net_profit", [1000])[-1] # Tỷ VND
tk353_pct = 5.0
tk353_bil = latest_np * (tk353_pct / 100.0)

# 0. Mô-đun 1: Bối cảnh Thị trường Lõi & EYS
market_regime = ve.calculate_market_regime_and_eys(pe_core_market=12.5, rf_10y_vgb=4.58)

# 1. Gatekeepers & ROCE
adj_eps_res = r1.calculate_adjusted_eps(latest_np, tk353_bil, shares)
oe_res = r1.calculate_owner_earnings(fin, tk353_welfare_fund=tk353_bil)
bf_res = r1.calculate_big_five_cagr(fin)
fscore_res = r1.calculate_piotroski_f_score(fin)
zscore_res = r1.calculate_altman_z_score(fin)
roce_val = r1.calculate_roce(fin)

dyn_mos_res = r1.calculate_dynamic_margin_of_safety(
    big_five_passed=bf_res["passed_count"],
    f_score=fscore_res["f_score"],
    z_score=zscore_res["z_score"],
    sector=fin["sector"],
    pe_core_market=12.5
)
active_mos_pct = dyn_mos_res["recommended_mos_pct"]

# 2. Rule #1 Quartet với Decay Model & Ke Thích Ứng
cagr_bvps_val = 15.0
for c in bf_res["criteria"]:
    if "Vốn CSH" in c["name"]:
        cagr_bvps_val = float(c["val"])
        break

sticker_res = r1.calculate_sticker_price_rule_one(
    eps_0=adj_eps_res["adjusted_eps"],
    cagr_bvps=cagr_bvps_val,
    cagr_analysts=15.0,
    historical_pe_5y=fin.get("peer_pe_median", 14.5),
    marr=15.0,
    mos_pct=active_mos_pct,
    use_decay_growth=True,
    beta=1.10,
    rf_rate=4.58,
    erp_rate=7.5
)

max_payback_target = 10 if bf_res["has_strong_moat"] else 8
payback_res = r1.calculate_payback_time(
    fcf_0_per_share=oe_res["oe_per_share"],
    growth_rate=sticker_res["growth_rate_used"],
    current_price=current_price,
    years=8,
    max_acceptable_years=max_payback_target
)

tencap_res = r1.calculate_ten_cap_price(oe_res["oe_per_share"], growth_rate=sticker_res["growth_rate_used"], ke_rate=sticker_res["ke_rate"])
zombie_res = r1.calculate_zombie_value(fin)

# 3. Bộ 3 Benjamin Graham Bản Địa Hóa
graham_res = r1.calculate_benjamin_graham_trio(
    eps_adjusted=adj_eps_res["adjusted_eps"],
    bvps_adjusted=fin.get("bvps", 13500.0),
    growth_rate=sticker_res["growth_rate_used"],
    rf_10y_bond=4.58
)

# 4. DCF & Relative Multiples
dcf_res = ve.calculate_dcf_fcff(fin, wacc=fin.get("wacc_default", 11.0), growth_lt=fin.get("growth_longterm_default", 4.5))
rel_res = ve.calculate_relative_multiples(fin, growth_rate=sticker_res["growth_rate_used"])

# 5. Vùng Mua Hội Tụ Nội Tại (Pre-MOS Fair Values — Không trừ MOS kép!)
valuation_summary = [
    {"Phương pháp": f"1. Sticker Price Fair Value (Ke {sticker_res['ke_rate']}%)", "Giá trị (VNĐ)": sticker_res["sticker_price_ke"], "Giá Mua MOS": sticker_res["mos_price_ke"], "Trọng số": 0.25},
    {"Phương pháp": "2. Payback Time Sức Mua Thực (Fair 10Y / Buy 8Y)", "Giá trị (VNĐ)": payback_res["payback_price_10y"], "Giá Mua MOS": payback_res["payback_price_8y"], "Trọng số": 0.25},
    {"Phương pháp": f"3. Owner Earnings Buffett (Fair {tencap_res['oe_fair_multiple']}x / 10 Cap)", "Giá trị (VNĐ)": tencap_res["oe_fair_value"], "Giá Mua MOS": tencap_res["ten_cap_price"], "Trọng số": 0.25},
    {"Phương pháp": "4. DCF FCFF Chiết khấu Dòng tiền (Damodaran Reinvestment)", "Giá trị (VNĐ)": dcf_res["fair_value"], "Giá Mua MOS": round(dcf_res["fair_value"] * (1 - active_mos_pct/100), 0), "Trọng số": 0.25}
]

df_conv = pd.DataFrame(valuation_summary)
total_w = df_conv["Trọng số"].sum()
df_conv["Trọng số chuẩn hóa"] = df_conv["Trọng số"] / total_w
df_conv["Đóng góp (VNĐ)"] = df_conv["Giá trị (VNĐ)"] * df_conv["Trọng số chuẩn hóa"]
intrinsic_convergence_price = round(df_conv["Đóng góp (VNĐ)"].sum(), 0)

# 6. Thuật toán Phối hợp 70% Nội tại (Pre-MOS) + 30% Tương đối Đa Bội Số (Pre-MOS) & Trừ MOS 1 Lần Duy Nhất
master_targets = ve.calculate_master_fair_value_and_targets(
    intrinsic_convergence_price=intrinsic_convergence_price,
    relative_price=rel_res.get("blended_relative_price", rel_res["pe_valuation"]),
    current_price=current_price,
    mos_pct=active_mos_pct,
    pe_overheat_price=rel_res.get("pe_sell_overheat")
)

# 7. Ma trận Rải lệnh 3 Giai đoạn (Mô-đun 4 - Time & Value Tranching V3.0)
multi_tranches = ve.calculate_multi_tranche_buy_zones(
    fair_value=master_targets["master_fair_value"],
    sticker_price_classic=sticker_res["sticker_price_classic"],
    sticker_price_ke=sticker_res["sticker_price_ke"],
    ten_cap_price=tencap_res["ten_cap_price"],
    payback_price_8y=payback_res["payback_price_8y"],
    pe_band_minus_1sd=rel_res.get("pe_band_minus_1sd", 0.0),
    pe_band_minus_2sd=rel_res.get("pe_band_minus_2sd", 0.0),
    zombie_price=zombie_res.get("zombie_price", 0.0),
    current_price=current_price,
    tier_code=dyn_mos_res.get("tier_code", "TIER_1"),
    mos_pct=active_mos_pct,
    stock_data=fin
)

print(f"=== KẾT QUẢ ĐỊNH GIÁ NÂNG CẤP DEEP RESEARCH 2.1 CHO {symbol} ===")
print(f"Thị trường Lõi: {market_regime['regime_name']} (P/E Lõi: {market_regime['pe_core_market']}x | EYS: {market_regime['eys']}%)")
print(f"Thị giá hiện tại: {current_price:,.0f} đ")
print(f"ROCE hiệu quả vốn: {roce_val}%")
print(f"Sticker Price Ke: {sticker_res['sticker_price_ke']:,.0f} đ | MOS Adaptive ({active_mos_pct:.0f}%): {sticker_res['mos_price_ke']:,.0f} đ")
print(f"Sticker Phil Town Classic: {sticker_res['sticker_price_classic']:,.0f} đ | MOS 50%: {sticker_res['mos_price_classic']:,.0f} đ")
print(f"Graham 1: {graham_res['graham_1_price']:,.0f} đ | Graham 2 (TPCP VN): {graham_res['graham_2_price']:,.0f} đ | Graham Number: {graham_res['graham_number']:,.0f} đ")
print(f"10 Cap Price: {tencap_res['ten_cap_price']:,.0f} đ | DCF FCFF: {dcf_res['fair_value']:,.0f} đ")
print(f"Master Fair Value: {master_targets['master_fair_value']:,.0f} đ | P_Buy An Toàn: {master_targets['target_buy_price']:,.0f} đ")
print(f"Tranche 1 (30% Vốn): <= {multi_tranches['tranche_1']['trigger_price']:,.0f} đ | Trạng thái: {'TRONG VÙNG MUA' if multi_tranches['tranche_1']['is_in_buy_zone'] else 'CAO HƠN'}")
print(f"Tranche 2 (40% Vốn): <= {multi_tranches['tranche_2']['trigger_price']:,.0f} đ | Trạng thái: {'TRONG VÙNG MUA' if multi_tranches['tranche_2']['is_in_buy_zone'] else 'CAO HƠN'}")
print(f"Tranche 3 (30% Vốn): <= {multi_tranches['tranche_3']['trigger_price']:,.0f} đ | Trạng thái: {'TRONG VÙNG MUA' if multi_tranches['tranche_3']['is_in_buy_zone'] else 'CAO HƠN'}")
print(f"GIÁ BÁN MỤC TIÊU 1 (P_SELL_1): {master_targets['target_sell_1']:,.0f} đ")
print(f"GIÁ BÁN QUÁ NHIỆT 2 (P_SELL_2): {master_targets['target_sell_2']:,.0f} đ")
print(f"Tỷ lệ Win/Loss: {multi_tranches['win_loss_ratio']}x")

# Xuất lại Excel
bctc_dir = r"D:\Mister CO\Antigravity\Super Stock\BCTC"
os.makedirs(bctc_dir, exist_ok=True)
excel_path = os.path.join(bctc_dir, f"{symbol}_Bao_Cao_Dinh_Gia_Chuyen_Nghiep.xlsx")

with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
    # Sheet 1: Tổng quan Khuyến Nghị
    df_exec = pd.DataFrame([
        {"Chỉ tiêu": "Mã Cổ Phiếu", "Giá trị": symbol},
        {"Chỉ tiêu": "Tên Doanh Nghiệp", "Giá trị": fin['name']},
        {"Chỉ tiêu": "Ngành Phân Loại (8 Nhóm)", "Giá trị": fin['sector_name']},
        {"Chỉ tiêu": "Thị Giá Hiện Tại", "Giá trị": f"{current_price:,.0f} đ"},
        {"Chỉ tiêu": "Bối Cảnh Thị Trường Lõi", "Giá trị": f"{market_regime['regime_name']} (P/E {market_regime['pe_core_market']}x, EYS {market_regime['eys']}%)"},
        {"Chỉ tiêu": "GIÁ MUA AN TOÀN (P_BUY)", "Giá trị": f"{master_targets['target_buy_price']:,.0f} đ"},
        {"Chỉ tiêu": "GIÁ BÁN MỤC TIÊU 1 (CHỐT LỜI HỢP LÝ)", "Giá trị": f"{master_targets['target_sell_1']:,.0f} đ"},
        {"Chỉ tiêu": "GIÁ BÁN QUÁ NHIỆT 2 (HƯNG PHẤN)", "Giá trị": f"{master_targets['target_sell_2']:,.0f} đ"},
        {"Chỉ tiêu": "Tỷ Lệ Lợi Nhuận/Rủi Ro (Win/Loss)", "Giá trị": f"{multi_tranches['win_loss_ratio']}x"},
        {"Chỉ tiêu": "ROCE (Hiệu Quả Vốn Dài Hạn)", "Giá trị": f"{roce_val}%"},
        {"Chỉ tiêu": "Khuyến Nghị Tổng Thể", "Giá trị": "QUAN SÁT / CHỜ CHIẾT KHẤU" if current_price > master_targets['target_buy_price'] else "MUA TÍCH LŨY"}
    ])
    df_exec.to_excel(writer, index=False, sheet_name="Tong_Quan_Khuyen_Nghi")
    
    # Sheet 2: Ma Trận Rải Lệnh 3 Tranches
    t1 = multi_tranches["tranche_1"]
    t2 = multi_tranches["tranche_2"]
    t3 = multi_tranches["tranche_3"]
    df_tranches = pd.DataFrame([
        {
            "Vùng Giải Ngân": t1["name"],
            "Tỷ Trọng Vốn": t1["capital_weight"],
            "Ngưỡng Giá Kích Hoạt": f"<= {t1['trigger_price']:,.0f} đ",
            "Trạng Thái Hiện Tại": "ĐANG TRONG VÙNG MUA" if t1["is_in_buy_zone"] else "CAO HƠN VÙNG MUA",
            "Điều Kiện": t1["conditions"],
            "Hướng Dẫn Thực Thi": t1["execution"]
        },
        {
            "Vùng Giải Ngân": t2["name"],
            "Tỷ Trọng Vốn": t2["capital_weight"],
            "Ngưỡng Giá Kích Hoạt": f"<= {t2['trigger_price']:,.0f} đ",
            "Trạng Thái Hiện Tại": "ĐANG TRONG VÙNG MUA" if t2["is_in_buy_zone"] else "CAO HƠN VÙNG MUA",
            "Điều Kiện": t2["conditions"],
            "Hướng Dẫn Thực Thi": t2["execution"]
        },
        {
            "Vùng Giải Ngân": t3["name"],
            "Tỷ Trọng Vốn": t3["capital_weight"],
            "Ngưỡng Giá Kích Hoạt": f"<= {t3['trigger_price']:,.0f} đ",
            "Trạng Thái Hiện Tại": "ĐANG TRONG VÙNG MUA" if t3["is_in_buy_zone"] else "CAO HƠN VÙNG MUA",
            "Điều Kiện": t3["conditions"],
            "Hướng Dẫn Thực Thi": t3["execution"]
        }
    ])
    df_tranches.to_excel(writer, index=False, sheet_name="Ma_Tran_Rai_Lenh_3_Tranches")

    # Sheet 3: Bộ 3 Benjamin Graham
    df_graham = pd.DataFrame([
        {"Mô hình": "Graham 1 (Tăng Trưởng Cơ Bản)", "Giá trị": f"{graham_res['graham_1_price']:,.0f} đ", "Ghi chú": f"IV = EPS * (8.5 + 2*{graham_res['g_used']})"},
        {"Mô hình": "Graham 2 (Điều chỉnh TPCP VN 10Y)", "Giá trị": f"{graham_res['graham_2_price']:,.0f} đ", "Ghi chú": f"Điều chỉnh Rf = {graham_res['rf_used']}%, Y_vn = {graham_res['y_vn_used']}%"},
        {"Mô hình": "Con Số Graham (Graham Number)", "Giá trị": f"{graham_res['graham_number']:,.0f} đ", "Ghi chú": "sqrt(22.5 * EPS * BVPS) - Ngưỡng an toàn P/E <= 15x, P/B <= 1.5x"}
    ])
    df_graham.to_excel(writer, index=False, sheet_name="Bo_3_Benjamin_Graham")

    # Sheet 4: Vùng Mua Hội Tụ
    df_conv_export = df_conv.copy()
    df_conv_export["Giá trị (VNĐ)"] = df_conv_export["Giá trị (VNĐ)"].apply(lambda x: f"{x:,.0f} đ")
    df_conv_export["Trọng số chuẩn hóa"] = df_conv_export["Trọng số chuẩn hóa"].apply(lambda x: f"{x:.1%}")
    df_conv_export["Đóng góp (VNĐ)"] = df_conv_export["Đóng góp (VNĐ)"].apply(lambda x: f"{x:,.0f} đ")
    df_conv_export.to_excel(writer, index=False, sheet_name="Vung_Mua_Hoi_Tu")

    # Sheet 5: Bộ Tứ Rule #1
    df_rule1 = pd.DataFrame([
        {"Mô hình": f"1. Sticker Price Thích Ứng Ke ({sticker_res['ke_rate']}%)", "Giá trị": f"{sticker_res['sticker_price_ke']:,.0f} đ", "Ghi chú": "EPS 10 năm với g Decay chiết khấu theo chi phí vốn CSH thực tế Ke"},
        {"Mô hình": f"1b. Giá Mua MOS Thích Ứng ({active_mos_pct:.0f}%)", "Giá trị": f"{sticker_res['mos_price_ke']:,.0f} đ", "Ghi chú": "Khắc phục bẫy đứng ngoài 10 năm của Rule #1 cổ điển"},
        {"Mô hình": "1c. Benchmark Phil Town Gốc (MARR 15% + MOS 50%)", "Giá trị": f"{sticker_res['mos_price_classic']:,.0f} đ", "Ghi chú": f"Sticker gốc: {sticker_res['sticker_price_classic']:,.0f} đ (Dùng cho Tranche 3 Khủng hoảng)"},
        {"Mô hình": "2. Payback Time (Hoàn Vốn 8-10 Năm)", "Giá trị": f"{payback_res['payback_price_8y']:,.0f} đ", "Ghi chú": f"Số năm hoàn vốn ở thị giá hiện tại: {payback_res['actual_payback_years']:.1f} năm (Mục tiêu <= {payback_res['max_acceptable_years']} năm)"},
        {"Mô hình": "3. Giá 10 Cap (Warren Buffett)", "Giá trị": f"{tencap_res['ten_cap_price']:,.0f} đ", "Ghi chú": "Dựa trên Owner Earnings (Đã trừ TK 353 & Maintenance CapEx)"},
        {"Mô hình": "4. Giá Trị Xác Sống (Zombie Value)", "Giá trị": f"{zombie_res['zombie_price']:,.0f} đ", "Ghi chú": "Net-Net Ben Graham"}
    ])
    df_rule1.to_excel(writer, index=False, sheet_name="Bo_Tu_Rule_One")

print("-> Đã xuất lại file Excel thành công!")
