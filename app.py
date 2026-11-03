"""
app.py - Super Stock Valuation Tool (Thị trường Chứng khoán Việt Nam)
Hệ thống Định giá Cổ phiếu Giá trị Chuyên nghiệp:
1. Nhập mã bất kỳ trực tiếp (Tự động tải BCTC & Thị giá) + Tùy chọn Kéo thả Excel Vietstock
2. Quản lý Danh mục Cổ phiếu Theo dõi (Watchlist) & Lưu trữ Cục bộ
3. 3 Kịch bản Định giá Đầu tư: Lạc quan (Bull) - Cơ sở (Base) - Thận trọng (Bear)
4. Trường phái Warren Buffett & Phil Town (Rule #1): Sticker Price, Payback Time, 10 Cap, Zombie Value
5. Tầng lọc Chống Bẫy Giá Trị: Big Five Moat, Piotroski F-Score, Altman Z''-Score
6. Xuất Báo cáo Định giá Toàn diện ra Excel nhiều sheet
"""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

from sample_data import SAMPLE_STOCKS
from market_data import get_live_stock_info, get_price_history, fetch_stock_financials_auto
from valuation_engine import (
    calculate_blended_valuation,
    calculate_dcf_fcff,
    calculate_banking_residual_income,
    calculate_banking_adjusted_pb,
    calculate_real_estate_rnav,
    calculate_relative_multiples,
    calculate_master_fair_value_and_targets,
    generate_sensitivity_matrix,
    calculate_market_regime_and_eys,
    calculate_multi_tranche_buy_zones
)
from rule_one_engine import (
    calculate_adjusted_eps,
    calculate_owner_earnings,
    calculate_sticker_price_rule_one,
    calculate_payback_time,
    calculate_ten_cap_price,
    calculate_zombie_value,
    calculate_benjamin_graham_trio,
    calculate_roce,
    calculate_big_five_cagr,
    calculate_piotroski_f_score,
    calculate_altman_z_score,
    calculate_dynamic_margin_of_safety
)
from storage import (
    get_watchlist,
    save_to_watchlist,
    remove_from_watchlist,
    export_valuation_to_excel
)
from vietstock_parser import parse_vietstock_excel, generate_excel_template

# Thiết lập cấu hình trang
st.set_page_config(
    page_title="Super Stock - Định giá Cổ phiếu Việt Nam",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Helper function để render HTML an toàn, triệt tiêu 100% lỗi thụt dòng bị markdown coi là code block
def render_html(html_str: str):
    """
    Chuẩn hóa HTML: Cắt bỏ mọi khoảng trắng thụt lề đầu dòng để Markdown không coi là thẻ code block (4-space indent).
    Đảm bảo các thẻ <span>, <div>, <b> hiển thị chuẩn CSS và không bao giờ bị lộ raw HTML tag trên giao diện.
    """
    cleaned = "\n".join(line.strip() for line in html_str.strip().split("\n"))
    st.markdown(cleaned, unsafe_allow_html=True)

# Custom CSS cho giao diện hiện đại
st.markdown("""
<style>
    .main-header {
        font-size: 2.1rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0.2rem;
    }
    .regime-banner {
        background: linear-gradient(90deg, #1E293B 0%, #0F172A 100%);
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 12px 18px;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .badge-sector {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 600;
        background-color: #E0E7FF;
        color: #3730A3;
        margin-right: 6px;
    }
    .badge-moat {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 600;
        background-color: #DCFCE7;
        color: #15803D;
        margin-right: 6px;
    }
    .badge-fscore {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 600;
        background-color: #FEF3C7;
        color: #B45309;
    }
    .card-rule1 {
        background-color: #F8FAFC;
        border-radius: 10px;
        padding: 18px 22px;
        border: 1px solid #CBD5E1;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        margin-bottom: 14px;
    }
    .tranche-card {
        background-color: #FFFFFF;
        border-radius: 10px;
        padding: 16px 18px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
        margin-bottom: 10px;
    }
    .rec-box-buy {
        background: linear-gradient(135deg, #10B981 0%, #059669 100%);
        color: white;
        padding: 22px;
        border-radius: 12px;
        text-align: center;
        margin: 15px 0;
    }
    .rec-box-hold {
        background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);
        color: white;
        padding: 22px;
        border-radius: 12px;
        text-align: center;
        margin: 15px 0;
    }
    .rec-box-sell {
        background: linear-gradient(135deg, #EF4444 0%, #DC2626 100%);
        color: white;
        padding: 22px;
        border-radius: 12px;
        text-align: center;
        margin: 15px 0;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SIDEBAR: TÌM KIẾM MÃ TRỰC TIẾP & THAM SỐ
# ---------------------------------------------------------
st.sidebar.image("https://img.icons8.com/fluency/96/bullish.png", width=64)
st.sidebar.title("Super Stock 🇻🇳")
st.sidebar.caption("Hệ thống Định giá Cổ phiếu Giá trị Thực chiến")

# 1. Ô NHẬP MÃ CỔ PHIẾU TRỰC TIẾP (LOẠI BỎ MỤC DỮ LIỆU MẪU)
default_sym = st.session_state.get("selected_stock", "HPG")
target_sym = st.sidebar.text_input(
    "🔍 Nhập mã cổ phiếu (HOSE/HNX/UPCoM):",
    value=default_sym,
    help="Gõ bất kỳ mã nào: HPG, GEE, MSR, FPT, VCB, SSI, VNM, MWG, DGC..."
).upper().strip()

current_symbol = target_sym if target_sym else "HPG"

# 1b. MÔ HÌNH TĂNG TRƯỞNG & PHÒNG CHỐNG BẪY HÀM MŨ g^10
growth_model_choice = st.sidebar.radio(
    "📉 Mô hình Tăng trưởng Dự phóng:",
    ["Tăng trưởng Giảm dần (Decay / Fade - Khuyên dùng)", "Tăng trưởng Tuyến tính (Phil Town Classic)"],
    index=0,
    help="Decay Model giúp giữ g trong 5 năm đầu và giảm dần 12%/năm về mức dài hạn trong 5 năm sau để triệt tiêu hiện tượng phóng đại sai số mũ g^10."
)
use_decay = growth_model_choice.startswith("Tăng trưởng Giảm dần")

# 2. TÙY CHỌN TẢI LÊN FILE EXCEL BCTC VIETSTOCK
with st.sidebar.expander("📁 Tùy chọn: Tải lên Excel BCTC Vietstock"):
    uploaded_file = st.file_uploader(
        "Kéo thả file BCTC Excel từ Vietstock:",
        type=["xlsx", "xls"]
    )
    st.download_button(
        "📥 Tải file Excel mẫu",
        data=generate_excel_template(),
        file_name="BCTC_Mau_Vietstock.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# 3. KỊCH BẢN ĐỊNH GIÁ (BULL / BASE / BEAR)
scenario = st.sidebar.selectbox(
    "📊 Kịch bản Định giá:",
    ["⚪ Kịch bản Cơ sở (Base Case)", "🟢 Kịch bản Lạc quan (Bull Case)", "🔴 Kịch bản Thận trọng (Bear Case)"],
    index=0
)

# Nạp dữ liệu tài chính
active_stock_data = None

if uploaded_file:
    parsed = parse_vietstock_excel(uploaded_file.read(), symbol=current_symbol)
    active_stock_data = SAMPLE_STOCKS.get(current_symbol, SAMPLE_STOCKS["HPG"]).copy()
    active_stock_data["name"] = f"Cổ phiếu {current_symbol} (Tải từ Excel)"
    st.sidebar.success("✅ Đã nạp số liệu từ file Excel Vietstock!")
else:
    # Tự động tải từ Yahoo Finance hoặc dữ liệu tích hợp
    with st.spinner(f"Đang tải BCTC tự động cho mã {current_symbol}..."):
        fetched = fetch_stock_financials_auto(current_symbol)
    if fetched:
        active_stock_data = fetched
        st.sidebar.success(f"✅ Đã tải BCTC thực tế: {fetched['sector_name']}")
    elif current_symbol in SAMPLE_STOCKS:
        active_stock_data = SAMPLE_STOCKS[current_symbol].copy()
        st.sidebar.success(f"✅ Đã tải BCTC chuẩn: {active_stock_data['sector_name']}")
    else:
        active_stock_data = SAMPLE_STOCKS["HPG"].copy()
        active_stock_data["symbol"] = current_symbol
        active_stock_data["name"] = f"Cổ phiếu {current_symbol}"
        st.sidebar.warning(f"⚠️ Mã {current_symbol} chưa có feed trên Yahoo Finance. Bạn có thể kéo thả file Excel từ Vietstock ở mục trên để định giá chính xác 100% nhé!")

# Lấy thị giá Live
with st.spinner("Đang cập nhật thị giá..."):
    live_info = get_live_stock_info(current_symbol)
    
if live_info["status"] == "success" and live_info["current_price"] > 0:
    current_price = live_info["current_price"]
    prev_close = live_info["previous_close"]
    price_change_pct = ((current_price - prev_close) / prev_close) * 100 if prev_close > 0 else 0.0
    if live_info["shares_outstanding"] > 0:
        active_stock_data["shares_outstanding"] = live_info["shares_outstanding"]
else:
    current_price = active_stock_data.get("current_price_fallback", 21000.0)
    prev_close = current_price
    price_change_pct = 0.0

st.sidebar.markdown("---")
st.sidebar.subheader("🌐 Chu Kỳ Vĩ Mô & Thị Trường Lõi")
pe_core_slider = st.sidebar.slider("P/E Thị trường Lõi (Core VN-Index):", 8.0, 20.0, 12.5, 0.5, help="P/E thị trường sau khi loại bỏ cổ phiếu trụ có P/E > 40x như VIC (73x), VPL (56x).")
rf_rate_slider = st.sidebar.slider("Lợi suất TPCP 10 Năm (Rf %):", 3.0, 8.0, 4.58, 0.05, help="Lợi suất trái phiếu chính phủ Việt Nam 10 năm.")
stock_beta = float(active_stock_data.get("beta", 1.10))
beta_slider = st.sidebar.slider("Hệ số Beta Cổ phiếu:", 0.5, 2.2, stock_beta, 0.05, help="Đo lường độ nhạy cảm của cổ phiếu so với thị trường.")

st.sidebar.markdown("---")
st.sidebar.subheader("💎 Tham số Phil Town (Rule #1)")
marr_slider = st.sidebar.slider("Tỷ suất sinh lời tối thiểu (MARR %/năm):", 10.0, 20.0, 15.0, 0.5)
tk353_pct = st.sidebar.slider("Trích Quỹ KTPL (TK 353) % LNST:", 0.0, 15.0, 5.0, 0.5)
mos_mode = st.sidebar.radio("Cơ chế Biên An Toàn (MOS):", ["Biên An Toàn Động (Dynamic Elastic MOS)", "Cố định 50% (Phil Town Cổ Điển)"])

st.sidebar.markdown("---")
st.sidebar.subheader("⚙️ Giả định Theo Ngành")
sector = active_stock_data.get("sector", "CYCLICAL_MANUFACTURING")
custom_params = {}

# Điều chỉnh tham số theo Kịch bản (Scenario Adjustment)
g_scenario_adj = 0.0
wacc_scenario_adj = 0.0
pe_scenario_adj = 0.0

if scenario == "🟢 Kịch bản Lạc quan (Bull Case)":
    g_scenario_adj = 1.5
    wacc_scenario_adj = -0.75
    pe_scenario_adj = 2.0
elif scenario == "🔴 Kịch bản Thận trọng (Bear Case)":
    g_scenario_adj = -1.5
    wacc_scenario_adj = 1.0
    pe_scenario_adj = -2.0

# Lấy trung vị bội số lịch sử thực nghiệm từ chính cổ phiếu (thay vì fix cứng số tĩnh)
emp_pe_def = float(active_stock_data.get("peer_pe_median", 11.5))
emp_pb_def = float(active_stock_data.get("peer_pb_median", 1.50))
emp_ev_def = float(active_stock_data.get("peer_ev_ebitda_median", 7.5))
emp_roe_def = float(active_stock_data.get("roe_expected", 18.0))

if sector == "BANKING":
    st.sidebar.info("🏦 Ngành: **Ngân hàng & Định chế Tài chính**")
    base_ke = 11.5 + wacc_scenario_adj
    base_g = max(2.0, 4.5 + g_scenario_adj)
    custom_params["cost_of_equity"] = st.sidebar.slider("Chi phí vốn CSH (Ke %):", 8.0, 16.0, base_ke, 0.25)
    custom_params["roe_expected"] = st.sidebar.slider("ROE kỳ vọng dài hạn (%):", 10.0, 30.0, max(12.0, min(28.0, emp_roe_def)), 0.5)
    custom_params["growth_lt"] = st.sidebar.slider("Tăng trưởng vĩnh cửu (g %):", 2.0, 6.0, base_g, 0.25)
    custom_params["target_pb"] = st.sidebar.slider("P/B mục tiêu (Lịch sử 5Y):", 0.8, 3.0, max(0.8, min(3.0, round(emp_pb_def, 2))), 0.05)
    custom_params["target_pe"] = st.sidebar.slider("P/E mục tiêu (Lịch sử 5Y):", 6.0, 18.0, max(6.0, min(18.0, round(emp_pe_def + pe_scenario_adj, 1))), 0.5)

elif sector == "REAL_ESTATE":
    st.sidebar.info("🏢 Ngành: **Bất động sản Dân dụng & Quỹ đất**")
    custom_params["holding_discount"] = st.sidebar.slider("Chiết khấu rủi ro pháp lý & thực thi (%):", 0, 30, 10, 5)
    custom_params["target_pb"] = st.sidebar.slider("P/B mục tiêu (Lịch sử 5Y):", 0.8, 2.5, max(0.8, min(2.5, round(emp_pb_def, 2))), 0.05)
    custom_params["target_pe"] = st.sidebar.slider("P/E mục tiêu (Lịch sử 5Y):", 5.0, 18.0, max(5.0, min(18.0, round(emp_pe_def + pe_scenario_adj, 1))), 0.5)

elif sector == "ELECTRICAL_EQUIPMENT":
    st.sidebar.info("⚡ Ngành: **Thiết bị Điện & Năng lượng**")
    base_wacc = 11.0 + wacc_scenario_adj
    base_g = max(2.0, 4.5 + g_scenario_adj)
    custom_params["wacc"] = st.sidebar.slider("Chi phí vốn WACC (%):", 8.0, 15.0, base_wacc, 0.25)
    custom_params["growth_lt"] = st.sidebar.slider("Tăng trưởng vĩnh cửu (g %):", 2.0, 6.0, base_g, 0.25)
    custom_params["target_ev_ebitda"] = st.sidebar.slider("EV/EBITDA mục tiêu:", 5.0, 15.0, max(5.0, min(15.0, round(emp_ev_def, 1))), 0.5)
    custom_params["target_pe"] = st.sidebar.slider("P/E cốt lõi (Lịch sử 5Y):", 8.0, 22.0, max(8.0, min(22.0, round(emp_pe_def + pe_scenario_adj, 1))), 0.5)

elif sector == "CYCLICAL_MANUFACTURING":
    st.sidebar.info("🏭 Ngành: **Sản xuất Chu kỳ / Thâm dụng vốn**")
    base_wacc = 11.25 + wacc_scenario_adj
    base_g = max(2.0, 4.0 + g_scenario_adj)
    custom_params["wacc"] = st.sidebar.slider("Chi phí vốn WACC (%):", 8.0, 16.0, base_wacc, 0.25)
    custom_params["growth_lt"] = st.sidebar.slider("Tăng trưởng vĩnh cửu (g %):", 2.0, 5.5, base_g, 0.25)
    custom_params["target_ev_ebitda"] = st.sidebar.slider("EV/EBITDA mục tiêu:", 4.0, 12.0, max(4.0, min(12.0, round(emp_ev_def, 1))), 0.2)
    custom_params["target_pe"] = st.sidebar.slider("P/E chuẩn hóa chu kỳ (Lịch sử 5Y):", 6.0, 16.0, max(6.0, min(16.0, round(emp_pe_def + pe_scenario_adj, 1))), 0.5)
    custom_params["target_pb"] = st.sidebar.slider("P/B mục tiêu (Lịch sử 5Y):", 0.8, 2.5, max(0.8, min(2.5, round(emp_pb_def, 2))), 0.05)

else:
    st.sidebar.info("💻 Ngành: **Tăng trưởng & Công nghệ / Tiêu dùng**")
    base_wacc = 10.5 + wacc_scenario_adj
    base_g = max(2.5, 4.5 + g_scenario_adj)
    custom_params["wacc"] = st.sidebar.slider("Chi phí vốn WACC (%):", 8.0, 15.0, base_wacc, 0.25)
    custom_params["growth_lt"] = st.sidebar.slider("Tăng trưởng vĩnh cửu (g %):", 2.0, 6.0, base_g, 0.25)
    custom_params["target_pe"] = st.sidebar.slider("P/E mục tiêu (Lịch sử 5Y):", 10.0, 30.0, max(10.0, min(30.0, round(emp_pe_def + pe_scenario_adj, 1))), 0.5)
    custom_params["target_pb"] = st.sidebar.slider("P/B mục tiêu (Lịch sử 5Y):", 1.2, 6.0, max(1.2, min(6.0, round(emp_pb_def, 1))), 0.1)

# ---------------------------------------------------------
# TÍNH TOÁN BỘ MÁY ĐỊNH GIÁ & TẦNG LỌC
# ---------------------------------------------------------
shares = active_stock_data.get("shares_outstanding", 1)
latest_net_profit = float(active_stock_data.get("net_profit_ttm") or active_stock_data.get("net_profit", [1000])[-1])
tk353_bil = latest_net_profit * (tk353_pct / 100.0)

# 0. Mô-đun 1: Chu kỳ Thị trường Lõi & EYS
market_regime = calculate_market_regime_and_eys(pe_core_market=pe_core_slider, rf_10y_vgb=rf_rate_slider)

# 1. Adjusted EPS & Owner Earnings (Đồng bộ với EPS TTM thực tế để chống lệch pha sau chia tách)
adj_eps_res = calculate_adjusted_eps(
    latest_net_profit,
    tk353_bil,
    shares,
    reference_eps=float(active_stock_data.get("eps_current", 0.0))
)
oe_res = calculate_owner_earnings(active_stock_data, tk353_welfare_fund=tk353_bil)

# 2. Gatekeepers: Big Five, F-Score, Z-Score
bf_res = calculate_big_five_cagr(active_stock_data)
fscore_res = calculate_piotroski_f_score(active_stock_data)
zscore_res = calculate_altman_z_score(active_stock_data)

# 3. Dynamic Elastic MOS
if mos_mode.startswith("Biên An Toàn Động"):
    dyn_mos_res = calculate_dynamic_margin_of_safety(
        big_five_passed=bf_res["passed_count"],
        f_score=fscore_res["f_score"],
        z_score=zscore_res["z_score"],
        sector=sector,
        pe_core_market=pe_core_slider
    )
    active_mos_pct = dyn_mos_res["recommended_mos_pct"]
else:
    active_mos_pct = 50.0
    dyn_mos_res = {
        "recommended_mos_pct": 50.0,
        "base_mos_pct": 50.0,
        "delta_mos_cycle": 0.0,
        "tier": "Quy tắc Cổ điển Phil Town (50% Flat MOS)",
        "tier_code": "TIER_3",
        "advice": "Áp dụng mức chiết khấu 50% nguyên bản của Rule #1."
    }

# 4. Phil Town 4 Methods (Chuẩn Định Lượng Thực Chiến V3.0)
cagr_bvps_val = float(active_stock_data.get("cagr_bvps", 12.0))
hist_pe_5y = float(active_stock_data.get("peer_pe_median", 12.0))
div_yield_val = float(active_stock_data.get("dividend_yield", 2.5))
sticker_res = calculate_sticker_price_rule_one(
    eps_0=adj_eps_res["adjusted_eps"],
    cagr_bvps=cagr_bvps_val,
    cagr_analysts=max(12.0, cagr_bvps_val * 1.05) + g_scenario_adj,
    historical_pe_5y=hist_pe_5y,
    marr=marr_slider,
    mos_pct=active_mos_pct,
    use_decay_growth=use_decay,
    beta=beta_slider,
    rf_rate=rf_rate_slider,
    erp_rate=7.5,
    dividend_yield=div_yield_val
)

max_payback_target = 10 if bf_res["has_strong_moat"] else 8
payback_res = calculate_payback_time(
    fcf_0_per_share=oe_res["oe_per_share"],
    growth_rate=sticker_res["growth_rate_used"],
    current_price=current_price,
    years=8,
    max_acceptable_years=max_payback_target
)

tencap_res = calculate_ten_cap_price(
    oe_res["oe_per_share"],
    growth_rate=sticker_res["growth_rate_used"],
    ke_rate=sticker_res["ke_rate"]
)
zombie_res = calculate_zombie_value(active_stock_data)

# 5. Bộ 3 Công Thức Benjamin Graham Bản Địa Hóa
graham_res = calculate_benjamin_graham_trio(
    eps_adjusted=adj_eps_res["adjusted_eps"],
    bvps_adjusted=active_stock_data.get("bvps", 15000.0),
    growth_rate=sticker_res["growth_rate_used"],
    rf_10y_bond=rf_rate_slider
)
roce_val = calculate_roce(active_stock_data)

# ---------------------------------------------------------
# MAIN PANEL: HEADER & ACTIONS
# ---------------------------------------------------------
col_head1, col_head2 = st.columns([3, 1])

with col_head1:
    render_html(f"<div class='main-header'>{active_stock_data['name']} ({current_symbol})</div>")
    moat_label = "🏆 Con Hào Vững (Moat)" if bf_res["has_strong_moat"] else "⚠️ Moat Trung Bình"
    f_color = fscore_res['color']
    f_num = fscore_res['f_score']
    render_html(f"""
        <span class='badge-sector'>🏷️ {active_stock_data.get('sector_name', 'Cổ phiếu')}</span>
        <span class='badge-moat'>{moat_label} ({bf_res['passed_count']}/5 Big Five)</span>
        <span class='badge-fscore' style='color:{f_color};'>F-Score: {f_num}/9</span>
        <span class='badge-sector' style='background-color:#F1F5F9; color:#475569;'>MOS Động: {active_mos_pct:.0f}%</span>
    """)
    st.caption(active_stock_data.get("description", ""))

with col_head2:
    st.metric(
        label="Thị giá hiện tại (VND)",
        value=f"{int(current_price):,} đ",
        delta=f"{price_change_pct:+.2f}%"
    )

# Banner Bối Cảnh Thị Trường Lõi & EYS (Mô-đun 1 - Deep Research 2.1)
render_html(f"""
<div class='regime-banner'>
    <div>
        <span style='color:#94A3B8; font-size:0.85rem; font-weight:600;'>🌐 THỊ TRƯỜNG LÕI (CORE MARKET):</span>
        <span style='color:{market_regime["color"]}; font-weight:700; font-size:0.95rem; margin-left:6px;'>{market_regime["regime_name"]}</span>
        <span style='color:#E2E8F0; font-size:0.85rem; margin-left:10px;'>P/E Lõi: <b>{market_regime["pe_core_market"]}x</b> | EYS: <b>{market_regime["eys"]}%</b> | TPCP 10Y: <b>{market_regime["rf_10y_vgb"]}%</b></span>
    </div>
    <div style='color:#CBD5E1; font-size:0.82rem;'>💡 <em>{market_regime["signal"]}</em></div>
</div>
""")

st.markdown("---")

# Metrics Summary Cards
m1, m2, m3, m4 = st.columns(4)
market_cap_bil = (current_price * shares) / 1_000_000_000

with m1:
    st.metric("Vốn hóa Thị trường", f"{int(market_cap_bil):,} Tỷ")
with m2:
    st.metric("Adjusted EPS (TTM - TK 353)", f"{int(adj_eps_res['adjusted_eps']):,} đ", delta=f"-{adj_eps_res['leakage_pct']}% rò rỉ KTPL", delta_color="inverse")
with m3:
    st.metric("Owner Earnings / CP", f"{int(oe_res['oe_per_share']):,} đ")
with m4:
    st.metric("Biên An Toàn Khuyến Nghị", f"{active_mos_pct:.0f}%", help=dyn_mos_res["tier"])

# ---------------------------------------------------------
# TABS SETUP
# ---------------------------------------------------------
tab_verdict, tab_gatekeeper, tab_rule1, tab_models, tab_bctc, tab_watchlist, tab_chart = st.tabs([
    "🎯 Vùng Mua Hội Tụ & Khuyến Nghị (Convergence Buy Zone)",
    "🛡️ Tầng Lọc Moat & Sức Khỏe (Big Five & F-Score)",
    "💎 Bộ Tứ Quy Tắc Số 1 (Phil Town & Buffett)",
    "⚙️ Chi tiết Mô hình Ngành (DCF, RNAV, Multiples)",
    "📊 Báo cáo BCTC 5 Năm",
    "📋 Danh Mục Theo Dõi (My Watchlist)",
    "📈 Lịch sử Biến động Giá"
])

# ---------------------------------------------------------
# TAB 1: VÙNG MUA HỘI TỤ & KHUYẾN NGHỊ (ƯU TIÊN LÊN ĐẦU TIÊN)
# ---------------------------------------------------------
with tab_verdict:
    st.subheader(f"🎯 Vùng Mua Hội Tụ & Định Giá {current_symbol} — {scenario}")
    
    # Khắc phục triệt để Bẫy Trừ MOS Kép (Double MOS Subtraction Fix):
    # Hội tụ trên GIÁ TRỊ HỢP LÝ NỘI TẠI (Fair Value Pre-MOS), sau đó mới trừ MOS ĐÚNG 1 LẦN DUY NHẤT!
    valuation_summary = [
        {
            "Phương pháp": f"1. Rule #1 Sticker Fair Value (Ke = {sticker_res['ke_rate']}%)",
            "Giá Trị Hợp Lý (Pre-MOS)": sticker_res["sticker_price_ke"],
            "Giá Mua An Toàn (Sau MOS)": sticker_res["mos_price_ke"],
            "Giá trị (VNĐ)": sticker_res["sticker_price_ke"],
            "Trọng số": 0.25
        },
        {
            "Phương pháp": "2. Dòng Tiền Tích Lũy Payback (Fair 10Y / Buy 8Y)",
            "Giá Trị Hợp Lý (Pre-MOS)": payback_res["payback_price_10y"],
            "Giá Mua An Toàn (Sau MOS)": payback_res["payback_price_8y"],
            "Giá trị (VNĐ)": payback_res["payback_price_10y"],
            "Trọng số": 0.25
        },
        {
            "Phương pháp": f"3. Dòng Tiền Chủ Sở Hữu Buffett (Fair {tencap_res['oe_fair_multiple']}x / 10 Cap)",
            "Giá Trị Hợp Lý (Pre-MOS)": tencap_res["oe_fair_value"],
            "Giá Mua An Toàn (Sau MOS)": tencap_res["ten_cap_price"],
            "Giá trị (VNĐ)": tencap_res["oe_fair_value"],
            "Trọng số": 0.25
        }
    ]
    
    if sector == "BANKING":
        ri_res = calculate_banking_residual_income(active_stock_data, cost_of_equity=custom_params.get("cost_of_equity", 11.5), roe_expected=custom_params.get("roe_expected", 21.0), growth_lt=custom_params.get("growth_lt", 4.5))
        pb_res = calculate_banking_adjusted_pb(active_stock_data, target_pb=custom_params.get("target_pb", 1.85))
        valuation_summary.append({
            "Phương pháp": "4. Residual Income Model (Thu nhập Thặng dư Ngân hàng)",
            "Giá Trị Hợp Lý (Pre-MOS)": ri_res["fair_value"],
            "Giá Mua An Toàn (Sau MOS)": round(ri_res["fair_value"] * (1.0 - active_mos_pct / 100.0), 0),
            "Giá trị (VNĐ)": ri_res["fair_value"],
            "Trọng số": 0.25
        })
    elif sector == "REAL_ESTATE":
        rnav_res = calculate_real_estate_rnav(active_stock_data, holding_discount_pct=custom_params.get("holding_discount", 10.0))
        valuation_summary.append({
            "Phương pháp": "4. RNAV Quỹ Đất Dự Án Bất Động Sản",
            "Giá Trị Hợp Lý (Pre-MOS)": rnav_res["fair_value"],
            "Giá Mua An Toàn (Sau MOS)": round(rnav_res["fair_value"] * (1.0 - active_mos_pct / 100.0), 0),
            "Giá trị (VNĐ)": rnav_res["fair_value"],
            "Trọng số": 0.25
        })
    else:
        dcf_res = calculate_dcf_fcff(active_stock_data, wacc=custom_params.get("wacc", active_stock_data.get("wacc_default", 11.0)), growth_lt=custom_params.get("growth_lt", active_stock_data.get("growth_longterm_default", 4.0)))
        rel_res = calculate_relative_multiples(active_stock_data, custom_ev_ebitda=custom_params.get("target_ev_ebitda", active_stock_data.get("peer_ev_ebitda_median", 8.5)), custom_pe=custom_params.get("target_pe", active_stock_data.get("peer_pe_median", 14.5)))
        valuation_summary.append({
            "Phương pháp": "4. DCF FCFF Chiết Khấu Dòng Tiền Doanh Nghiệp",
            "Giá Trị Hợp Lý (Pre-MOS)": dcf_res["fair_value"],
            "Giá Mua An Toàn (Sau MOS)": round(dcf_res["fair_value"] * (1.0 - active_mos_pct / 100.0), 0),
            "Giá trị (VNĐ)": dcf_res["fair_value"],
            "Trọng số": 0.25
        })
        
    df_conv = pd.DataFrame(valuation_summary)
    total_w = df_conv["Trọng số"].sum()
    df_conv["Trọng số chuẩn hóa"] = df_conv["Trọng số"] / total_w
    df_conv["Đóng góp Fair Value (VNĐ)"] = df_conv["Giá Trị Hợp Lý (Pre-MOS)"] * df_conv["Trọng số chuẩn hóa"]
    intrinsic_fair_convergence = round(df_conv["Đóng góp Fair Value (VNĐ)"].sum(), 0)
    
    # Tính toán Phối hợp 70% Nội tại (Pre-MOS) + 30% Tương đối Đa Bội Số (Pre-MOS)
    rel_multiples = calculate_relative_multiples(
        active_stock_data,
        custom_pe=custom_params.get("target_pe"),
        custom_pb=custom_params.get("target_pb"),
        custom_ev_ebitda=custom_params.get("target_ev_ebitda"),
        growth_rate=sticker_res["growth_rate_used"]
    )
    master_targets = calculate_master_fair_value_and_targets(
        intrinsic_convergence_price=intrinsic_fair_convergence,
        relative_price=rel_multiples.get("blended_relative_price", rel_multiples["pe_valuation"]),
        current_price=current_price,
        mos_pct=active_mos_pct,
        pe_overheat_price=rel_multiples.get("pe_sell_overheat")
    )
    
    convergence_price = master_targets["target_buy_price"]
    master_fair_val = master_targets["master_fair_value"]
    upside_to_fair_pct = ((master_fair_val - current_price) / current_price) * 100.0 if current_price > 0 else 0.0
    upside_pct = ((convergence_price - current_price) / current_price) * 100.0 if current_price > 0 else 0.0
    
    st.dataframe(
        df_conv[["Phương pháp", "Giá Trị Hợp Lý (Pre-MOS)", "Giá Mua An Toàn (Sau MOS)", "Trọng số chuẩn hóa", "Đóng góp Fair Value (VNĐ)"]].style.format({
            "Giá Trị Hợp Lý (Pre-MOS)": "{:,.0f} đ",
            "Giá Mua An Toàn (Sau MOS)": "{:,.0f} đ",
            "Trọng số chuẩn hóa": "{:.0%}",
            "Đóng góp Fair Value (VNĐ)": "{:,.0f} đ"
        }),
        width="stretch"
    )
    
    st.markdown("---")
    c_res1, c_res2, c_res3, c_res4 = st.columns(4)
    with c_res1:
        st.metric("Thị giá hiện tại", f"{int(current_price):,} VNĐ", help=f"Biên độ 52 tuần: {int(active_stock_data.get('price_1y_min', current_price*0.8)):,} đ - {int(active_stock_data.get('price_1y_max', current_price*1.2)):,} đ")
    with c_res2:
        st.metric("⭐ GIÁ MUA CHUẨN MOS (Tranche 2)", f"{int(master_targets['target_buy_price']):,} VNĐ", delta=f"MOS -{active_mos_pct:.0f}% từ Fair Value", delta_color="normal", help="Trừ Biên an toàn ĐÚNG 1 LẦN DUY NHẤT từ Master Fair Value (Khắc phục bẫy chiết khấu kép)")
    with c_res3:
        st.metric("🎯 GIÁ TRỊ HỢP LÝ (BÁN MỤC TIÊU 1)", f"{int(master_targets['target_sell_1']):,} VNĐ", delta=f"{upside_to_fair_pct:+.1f}% Upside về Fair Value")
    with c_res4:
        st.metric("🔥 GIÁ BÁN QUÁ NHIỆT 2 (+1.5SD)", f"{int(master_targets['target_sell_2']):,} VNĐ", delta=f"Win/Loss: {master_targets['win_loss_ratio']}x")
        
    # Recommendation Box dựa trên vị trí thị giá so với Fair Value và Vùng Mua Tranche 1/2
    rec_type = "HOLD"
    if current_price <= master_targets["target_buy_price"]:
        rec_title = "🚀 KHUYẾN NGHỊ: MUA MẠNH GIÁ TRỊ (STRONG VALUE BUY)"
        rec_desc = f"Thị giá ({int(current_price):,} đ) đã chiết khấu vượt mức Biên an toàn {active_mos_pct:.0f}% so với Giá trị hợp lý ({int(master_fair_val):,} đ, Upside +{upside_to_fair_pct:.1f}%). Vùng giải ngân chủ lực Tranche 2!"
        box_class = "rec-box-buy"
        rec_type = "MUA MẠNH"
    elif upside_to_fair_pct >= 12.0:
        rec_title = "🟢 KHUYẾN NGHỊ: MUA TÍCH LŨY (ACCUMULATE — TRANCHE 1)"
        rec_desc = f"Thị giá đang thấp hơn Giá trị hợp lý {upside_to_fair_pct:.1f}% ({int(master_fair_val):,} đ). Nằm trong vùng giải ngân thăm dò 30% vốn (Tranche 1) và chờ nhịp chỉnh để gia tăng tỷ trọng!"
        box_class = "rec-box-buy"
        rec_type = "TÍCH LŨY"
    elif upside_to_fair_pct >= -8.0:
        rec_title = "🟡 KHUYẾN NGHỊ: THEO DÕI / NẮM GIỮ CHỜ NHỊP CHỈNH (HOLD)"
        rec_desc = f"Thị giá đang giao dịch quanh Giá trị hợp lý ({int(master_fair_val):,} đ). Kiên nhẫn đặt sẵn lệnh chờ tại Tranche 1 và Tranche 2 bên dưới."
        box_class = "rec-box-hold"
        rec_type = "NẮM GIỮ"
    else:
        rec_title = "🔴 KHUYẾN NGHỊ: TẠM NGƯNG MUA MỚI / CHỐT LỜI DẦN (REDUCE)"
        rec_desc = f"Thị giá hiện tại đang cao hơn Giá trị hợp lý cơ sở {abs(upside_to_fair_pct):.1f}%. Không FOMO mua đuổi, ưu tiên canh chốt lời khi tiến về vùng Quá nhiệt ({int(master_targets['target_sell_2']):,} đ)."
        box_class = "rec-box-sell"
        rec_type = "GIẢM TỶ TRỌNG"
        
    render_html(f"""
    <div class='{box_class}'>
        <h2 style='margin:0; color:white;'>{rec_title}</h2>
        <p style='font-size:1.1rem; margin-top:10px; color:#F0FDF4;'>{rec_desc}</p>
    </div>
    """)

    # Tính toán Ma trận Rải lệnh Giải ngân 3 Giai đoạn (Mô-đun 4 - Time & Value Tranching V3.0)
    multi_tranche_res = calculate_multi_tranche_buy_zones(
        fair_value=master_targets["master_fair_value"],
        sticker_price_classic=sticker_res["sticker_price_classic"],
        sticker_price_ke=sticker_res["sticker_price_ke"],
        ten_cap_price=tencap_res["ten_cap_price"],
        payback_price_8y=payback_res["payback_price_8y"],
        pe_band_minus_1sd=rel_multiples.get("pe_band_minus_1sd", 0.0),
        pe_band_minus_2sd=rel_multiples.get("pe_band_minus_2sd", 0.0),
        zombie_price=zombie_res.get("zombie_price", 0.0),
        current_price=current_price,
        tier_code=dyn_mos_res.get("tier_code", "TIER_1"),
        mos_pct=active_mos_pct,
        stock_data=active_stock_data
    )

    st.markdown("### 🧭 Ma Trận Rải Lệnh Giải Ngân 3 Giai Đoạn (Time & Value Tranching 6–9 Tháng)")
    st.caption(f"Chuẩn Định Lượng V3.0: Đảm bảo thứ tự nghiêm ngặt (Fair Value {int(master_fair_val):,} đ > Tranche 1 > Tranche 2 > Tranche 3) và đối chiếu trực tiếp với vùng giá giao dịch thực tế 52 tuần ({int(active_stock_data.get('price_1y_min', 0)):,} đ – {int(active_stock_data.get('price_1y_max', 0)):,} đ).")
    
    t1_data = multi_tranche_res["tranche_1"]
    t2_data = multi_tranche_res["tranche_2"]
    t3_data = multi_tranche_res["tranche_3"]
    
    dca1, dca2, dca3 = st.columns(3)
    with dca1:
        t1_badge = "🟢 ĐANG TRONG VÙNG MUA" if t1_data["is_in_buy_zone"] else "🔴 CHỜ ĐIỀU CHỈNH VỀ VÙNG MUA"
        t1_color = "#059669" if t1_data["is_in_buy_zone"] else "#D97706"
        render_html(f"""
        <div class='tranche-card'>
            <h4 style='margin:0; color:#1E3A8A;'>{t1_data['name']}</h4>
            <div style='color:#64748B; font-weight:600; font-size:0.85rem; margin:4px 0;'>Tỷ trọng: <b style='color:#0F172A;'>{t1_data['capital_weight']}</b></div>
            <div style='font-size:1.4rem; font-weight:700; color:{t1_color}; margin:8px 0;'>&le; {int(t1_data['trigger_price']):,} đ</div>
            <div style='font-size:0.85rem; font-weight:600; color:{t1_color}; margin-bottom:6px;'>{t1_badge}</div>
            <div style='font-size:0.8rem; color:#0F172A; background:#F1F5F9; padding:4px 8px; border-radius:6px; margin-bottom:6px;'><b>Tính khả thi:</b> {t1_data['reachability']}</div>
            <div style='font-size:0.8rem; color:#475569;'><b>Cơ sở:</b> {t1_data['conditions']}</div>
            <div style='font-size:0.75rem; color:#64748B; margin-top:6px; font-style:italic;'>{t1_data['execution']}</div>
        </div>
        """)
        
    with dca2:
        t2_badge = "🟢 ĐANG TRONG VÙNG MUA" if t2_data["is_in_buy_zone"] else "🔴 CHỜ ĐIỀU CHỈNH VỀ VÙNG MUA"
        t2_color = "#059669" if t2_data["is_in_buy_zone"] else "#DC2626"
        render_html(f"""
        <div class='tranche-card'>
            <h4 style='margin:0; color:#1E3A8A;'>{t2_data['name']}</h4>
            <div style='color:#64748B; font-weight:600; font-size:0.85rem; margin:4px 0;'>Tỷ trọng: <b style='color:#0F172A;'>{t2_data['capital_weight']}</b></div>
            <div style='font-size:1.4rem; font-weight:700; color:{t2_color}; margin:8px 0;'>&le; {int(t2_data['trigger_price']):,} đ</div>
            <div style='font-size:0.85rem; font-weight:600; color:{t2_color}; margin-bottom:6px;'>{t2_badge}</div>
            <div style='font-size:0.8rem; color:#0F172A; background:#F1F5F9; padding:4px 8px; border-radius:6px; margin-bottom:6px;'><b>Tính khả thi:</b> {t2_data['reachability']}</div>
            <div style='font-size:0.8rem; color:#475569;'><b>Cơ sở:</b> {t2_data['conditions']}</div>
            <div style='font-size:0.75rem; color:#64748B; margin-top:6px; font-style:italic;'>{t2_data['execution']}</div>
        </div>
        """)
        
    with dca3:
        t3_badge = "🟢 ĐANG TRONG VÙNG MUA" if t3_data["is_in_buy_zone"] else "🔴 CHỜ ĐIỀU CHỈNH VỀ VÙNG MUA"
        t3_color = "#059669" if t3_data["is_in_buy_zone"] else "#DC2626"
        render_html(f"""
        <div class='tranche-card'>
            <h4 style='margin:0; color:#1E3A8A;'>{t3_data['name']}</h4>
            <div style='color:#64748B; font-weight:600; font-size:0.85rem; margin:4px 0;'>Tỷ trọng: <b style='color:#0F172A;'>{t3_data['capital_weight']}</b></div>
            <div style='font-size:1.4rem; font-weight:700; color:{t3_color}; margin:8px 0;'>&le; {int(t3_data['trigger_price']):,} đ</div>
            <div style='font-size:0.85rem; font-weight:600; color:{t3_color}; margin-bottom:6px;'>{t3_badge}</div>
            <div style='font-size:0.8rem; color:#0F172A; background:#F1F5F9; padding:4px 8px; border-radius:6px; margin-bottom:6px;'><b>Tính khả thi:</b> {t3_data['reachability']}</div>
            <div style='font-size:0.8rem; color:#475569;'><b>Cơ sở:</b> {t3_data['conditions']}</div>
            <div style='font-size:0.75rem; color:#64748B; margin-top:6px; font-style:italic;'>{t3_data['execution']}</div>
        </div>
        """)
        
    st.info(f"🛡️ **Quản Trị Rủi Ro Kịch Bản Xấu Nhất (Worst-Case Floor):** `{int(multi_tranche_res['p_worst']):,} đ` (Neo theo Sàn P/B Sổ sách hữu hình & Dải -2SD). Tỷ lệ Lợi nhuận/Rủi ro hiện tại: **Win/Loss = {multi_tranche_res['win_loss_ratio']}x**.")
    
    # Nút bấm hành động: Lưu vào Watchlist & Xuất Báo Cáo
    col_act1, col_act2 = st.columns(2)
    with col_act1:
        if st.button("⭐ Lưu Cổ Phiếu Này Vào Danh Mục Theo Dõi (Watchlist)", use_container_width=True):
            saved_item = {
                "symbol": current_symbol,
                "name": active_stock_data.get("name", current_symbol),
                "sector": active_stock_data.get("sector_name", ""),
                "current_price": current_price,
                "target_price": convergence_price,
                "upside_pct": round(upside_pct, 1),
                "mos_pct": active_mos_pct,
                "f_score": fscore_res["f_score"],
                "big_five": f"{bf_res['passed_count']}/5",
                "recommendation": rec_type,
                "scenario": scenario
            }
            if save_to_watchlist(saved_item):
                st.success(f"✅ Đã lưu {current_symbol} vào Danh Mục Theo Dõi!")
            else:
                st.error("Không thể lưu danh mục.")
                
    with col_act2:
        gatekeeper_info = {
            "big_five_passed": bf_res["passed_count"],
            "f_score": fscore_res["f_score"],
            "f_assessment": fscore_res["assessment"],
            "z_score": zscore_res["z_score"],
            "z_zone": zscore_res["zone"],
            "mos_pct": active_mos_pct,
            "tier": dyn_mos_res["tier"]
        }
        rule1_info = {
            "sticker_price": sticker_res["sticker_price"],
            "mos_price": sticker_res["mos_price"],
            "payback_price": payback_res["payback_price_8y"],
            "actual_payback_years": payback_res["actual_payback_years"],
            "ten_cap_price": tencap_res["ten_cap_price"],
            "zombie_price": zombie_res["zombie_price"],
            "graham": graham_res
        }
        excel_bytes = export_valuation_to_excel(
            stock_data=active_stock_data,
            valuation_summary=valuation_summary,
            gatekeepers=gatekeeper_info,
            rule_one_results=rule1_info,
            verdict={"target_price": convergence_price, "rec": rec_type, "targets": master_targets}
        )
        st.download_button(
            "📥 Tải Báo Cáo Định Giá Chi Tiết (File Excel Nhiều Sheet)",
            data=excel_bytes,
            file_name=f"Bao_Cao_Dinh_Gia_{current_symbol}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )

# ---------------------------------------------------------
# TAB 2: TẦNG LỌC MOAT & SỨC KHỎE
# ---------------------------------------------------------
with tab_gatekeeper:
    st.subheader("🛡️ Tầng Lọc Sức Khỏe Tài Chính & Chống Bẫy Giá Trị")
    col_bf, col_fz = st.columns([1, 1])
    with col_bf:
        st.markdown("### 1. Bộ 5 Tiêu Chí Con Hào Kinh Tế (Big Five Moat)")
        for crit in bf_res["criteria"]:
            icon = "✅" if crit["pass"] else "❌"
            st.markdown(f"**{icon} {crit['name']}**: `{crit['val']:.1f}%` *(Mục tiêu: >= 10%)*")
        if bf_res["has_strong_moat"]:
            st.success(f"🏆 **Đạt {bf_res['passed_count']}/5 tiêu chuẩn Big Five**: Doanh nghiệp có Con hào kinh tế bền vững!")
        else:
            st.warning(f"⚠️ **Chỉ đạt {bf_res['passed_count']}/5 tiêu chuẩn**: Cần biên an toàn cao hơn.")
            
    with col_fz:
        st.markdown("### 2. Điểm Số Piotroski F-Score (Thang điểm 9)")
        f_color = fscore_res['color']
        f_val = fscore_res['f_score']
        st.markdown(f"<h2 style='color:{f_color}; margin:0;'>{f_val} / 9 ĐIỂM</h2>", unsafe_allow_html=True)
        st.write(f"**Đánh giá**: {fscore_res['assessment']}")
        
        with st.expander("Xem chi tiết 9 tiêu chí kiểm toán F-Score"):
            for title_f, pass_f in fscore_res["details"]:
                icon_f = "🟢 Đạt" if pass_f else "🔴 Không đạt"
                st.write(f"- {title_f}: **{icon_f}**")
                
        st.markdown("---")
        st.markdown("### 3. Chỉ Số Dự Báo Phá Sản Altman Z''-Score")
        if sector != "BANKING":
            z_color = zscore_res['color']
            z_val = zscore_res['z_score']
            st.markdown(f"<h3 style='color:{z_color}; margin:0;'>Z'' = {z_val}</h3>", unsafe_allow_html=True)
            st.write(f"**Trạng thái**: {zscore_res['zone']}")
        else:
            st.info("🏦 Ngân hàng và định chế tài chính được miễn trừ tính Altman Z-Score theo chuẩn quốc tế.")

    st.markdown("---")
    st.markdown("### 🧠 4. Bảng Thẩm Định Định Tính Ban Lãnh Đạo & Moat (Qualitative Checklist)")
    st.caption("Khắc phục điểm mù số liệu quá khứ: 30% trọng số chất lượng đến từ đánh giá thực tế của nhà đầu tư.")
    q_col1, q_col2 = st.columns(2)
    with q_col1:
        q1 = st.checkbox("1. Ban lãnh đạo minh bạch, trung thực, không có lịch sử rút ruột / ESOP pha loãng quá đà.", value=True)
        q2 = st.checkbox("2. Doanh nghiệp sở hữu Sức mạnh định giá (Pricing Power) — có thể tăng giá bán khi lạm phát mà không mất khách.", value=True)
        q3 = st.checkbox("3. Rào cản gia nhập ngành cao (Giấy phép đặc quyền, bằng sáng chế hoặc quy mô độc quyền).", value=True)
    with q_col2:
        q4 = st.checkbox("4. Chi phí chuyển đổi khách hàng cao (Switching Cost) — khách hàng rất khó hoặc tốn kém để chuyển sang đối thủ.", value=True)
        q5 = st.checkbox("5. Ngành nghề đang trong xu hướng phát triển dài hạn, không bị đe dọa bởi suy thoái cấu trúc hoặc thay thế.", value=True)
    
    qual_score = sum([q1, q2, q3, q4, q5])
    qual_pct = (qual_score / 5) * 100
    if qual_score >= 4:
        st.success(f"💎 **Điểm Định Tính Xuất Sắc: {qual_score}/5 ({qual_pct:.0f}%)** — Doanh nghiệp có hào kinh tế thực chất và ban lãnh đạo đứng về phía cổ đông!")
    elif qual_score == 3:
        st.info(f"⚖️ **Điểm Định Tính Trung Bình: {qual_score}/5 ({qual_pct:.0f}%)** — Cần theo dõi thêm về rủi ro cạnh tranh hoặc động thái pha loãng.")
    else:
        st.warning(f"⚠️ **Cảnh Báo Điểm Định Tính Thấp: {qual_score}/5 ({qual_pct:.0f}%)** — Nguy cơ Bẫy Giá Trị (Value Trap). Bắt buộc phải áp Biên An Toàn tối đa!")

# ---------------------------------------------------------
# TAB 3: BỘ TỨ RULE #1 (PHIL TOWN & BUFFETT)
# ---------------------------------------------------------
with tab_rule1:
    st.subheader("💎 Bộ Tứ Phương Pháp Định Giá Hội Tụ (Rule #1 Phil Town & Modern Ke)")
    r1, r2 = st.columns(2)
    with r1:
        render_html(f"""
        <div class='card-rule1'>
            <h3 style='margin:0; color:#1E3A8A;'>1. Giá Niêm Yết (Sticker Price)</h3>
            <p style='color:#64748B; margin-bottom:10px;'>Phóng chiếu EPS 10 năm với g bảo thủ & chiết khấu chi phí vốn Ke thực tế</p>
            <p style='margin:5px 0;'><strong>⭐ Giá Niêm Yết Thích Ứng (Ke = {sticker_res['ke_rate']}%):</strong> <b>{int(sticker_res['sticker_price_ke']):,} đ</b></p>
            <p style='margin:6px 0;'><strong>🎯 Giá Mua An Toàn (MOS {active_mos_pct:.0f}%):</strong> <span style='font-size:1.35rem; font-weight:700; color:#059669;'>{int(sticker_res['mos_price_ke']):,} đ</span></p>
            <p style='margin:5px 0; color:#64748B; font-size:0.9rem;'><strong>🛡️ Benchmark Phil Town Cổ Điển (MARR 15% + MOS 50%):</strong> <b>{int(sticker_res['mos_price_classic']):,} đ</b> <em>(Sticker: {int(sticker_res['sticker_price_classic']):,} đ)</em></p>
            <p style='color:#64748B; font-size:0.82rem; margin-top:8px;'>Tham số: g = {sticker_res['growth_rate_used']}% | Future P/E = {sticker_res['future_pe']}x | Ke = {sticker_res['ke_rate']}% | MARR = {sticker_res['marr']}%</p>
        </div>
        """)

    with r2:
        pb_badge = "🟢 Vùng Mua Tốt" if payback_res['is_buy_zone'] else "🟡 Cần Thêm Thời Gian"
        pb_actual_text = f"Số năm hoàn vốn ở thị giá hiện tại: <b>{payback_res['actual_payback_years']} năm</b> ({pb_badge})" if payback_res['actual_payback_years'] else ""
        render_html(f"""
        <div class='card-rule1'>
            <h3 style='margin:0; color:#1E3A8A;'>2. Thời Gian Hoàn Vốn (Payback Time)</h3>
            <p style='color:#64748B; margin-bottom:10px;'>Tổng dòng tiền tự do FCF tích lũy (Ngưỡng chấp nhận: &le; {payback_res['max_acceptable_years']} năm)</p>
            <p style='margin:5px 0;'><strong>⭐ Giá Mua Hoàn Vốn 8 Năm:</strong> <span style='font-size:1.35rem; font-weight:700; color:#059669;'>{int(payback_res['payback_price_8y']):,} đ</span></p>
            <p style='margin:5px 0;'><strong>⭐ Giá Mua Hoàn Vốn 10 Năm (Tier 1 Moat):</strong> <b style='color:#1E3A8A;'>{int(payback_res['payback_price_10y']):,} đ</b></p>
            <p style='margin:5px 0;'>{pb_actual_text}</p>
            <p style='color:#64748B; font-size:0.82rem; margin-top:8px;'>Owner Earnings/CP: {int(payback_res['fcf_0_per_share']):,} đ | g = {payback_res['growth_rate']}%</p>
        </div>
        """)

    r3, r4 = st.columns(2)
    with r3:
        render_html(f"""
        <div class='card-rule1'>
            <h3 style='margin:0; color:#1E3A8A;'>3. Giá 10 Cap (Warren Buffett)</h3>
            <p style='color:#64748B; margin-bottom:10px;'>Tỷ suất sinh lời dòng tiền chủ sở hữu (Owner Earnings) 10%</p>
            <p style='margin:6px 0;'><strong>⭐ Giá 10 Cap:</strong> <span style='font-size:1.35rem; font-weight:700; color:#059669;'>{int(tencap_res['ten_cap_price']):,} đ</span></p>
            <p style='margin:5px 0;'><strong>Owner Earnings/CP:</strong> <b>{int(oe_res['oe_per_share']):,} đ</b> <em>(Đã trừ Maintenance Capex & TK 353)</em></p>
            <p style='color:#64748B; font-size:0.82rem; margin-top:8px;'>Công thức: Owner Earnings per Share * 10 (Hoàn vốn 100% trong 10 năm)</p>
        </div>
        """)

    with r4:
        render_html(f"""
        <div class='card-rule1'>
            <h3 style='margin:0; color:#1E3A8A;'>4. Giá Trị Xác Sống (Zombie Value)</h3>
            <p style='color:#64748B; margin-bottom:10px;'>Giá trị thanh lý Net-Net của Ben Graham (Kịch bản xấu nhất)</p>
            <p style='margin:6px 0;'><strong>⭐ Giá Trị Xác Sống / CP:</strong> <span style='font-size:1.35rem; font-weight:700; color:#475569;'>{int(zombie_res['zombie_price']):,} đ</span></p>
            <p style='margin:5px 0;'><strong>Giá trị thanh lý ròng:</strong> <b>{int(zombie_res['liquidation_value_bil']):,} Tỷ VNĐ</b></p>
            <p style='color:#64748B; font-size:0.82rem; margin-top:8px;'>Công thức: [Tiền mặt + 0.75*Phải thu + 0.5*Tồn kho - Tổng Nợ phải trả] / Số CP</p>
        </div>
        """)

    st.markdown("---")
    st.markdown("### 🏛️ Bộ 3 Công Thức Định Giá Cổ Điển Benjamin Graham (Thầy Của Warren Buffett)")
    st.caption(f"Bản địa hóa với Lợi suất Trái phiếu Chính phủ Việt Nam 10 năm (Rf = {rf_rate_slider}%) và Giới hạn Kép P/E * P/B <= 22.5:")
    g1, g2, g3 = st.columns(3)
    with g1:
        render_html(f"""
        <div class='card-rule1'>
            <h4 style='margin:0; color:#1E3A8A;'>Graham 1: Tăng Trưởng Cơ Bản</h4>
            <p style='color:#64748B; font-size:0.85rem; margin-bottom:8px;'>IV = EPS * (8.5 + 2g)</p>
            <h3 style='color:#059669; margin:8px 0;'>{int(graham_res['graham_1_price']):,} đ</h3>
            <p style='color:#64748B; font-size:0.8rem;'>P/E cơ sở 8.5x + 2 lần tốc độ tăng trưởng ({graham_res['g_used']}%)</p>
        </div>
        """)
    with g2:
        render_html(f"""
        <div class='card-rule1'>
            <h4 style='margin:0; color:#1E3A8A;'>Graham 2: Điều Chỉnh TPCP VN</h4>
            <p style='color:#64748B; font-size:0.85rem; margin-bottom:8px;'>IV = EPS * (8.5 + 2g) * 4.4 / Y_vn</p>
            <h3 style='color:#059669; margin:8px 0;'>{int(graham_res['graham_2_price']):,} đ</h3>
            <p style='color:#64748B; font-size:0.8rem;'>Điều chỉnh mẫu số Y_vn = Rf ({rf_rate_slider}%) + 0.5% = {graham_res['y_vn_used']}%</p>
        </div>
        """)
    with g3:
        render_html(f"""
        <div class='card-rule1'>
            <h4 style='margin:0; color:#1E3A8A;'>Con Số Graham (Graham Number)</h4>
            <p style='color:#64748B; font-size:0.85rem; margin-bottom:8px;'>P = sqrt(22.5 * EPS * BVPS)</p>
            <h3 style='color:#059669; margin:8px 0;'>{int(graham_res['graham_number']):,} đ</h3>
            <p style='color:#64748B; font-size:0.8rem;'>Chặn kép: P/E &le; 15x và P/B &le; 1.5x cho tài sản thực chất</p>
        </div>
        """)

# ---------------------------------------------------------
# TAB 4: MÔ HÌNH NGÀNH
# ---------------------------------------------------------
with tab_models:
    st.subheader(f"Kết quả Định giá Chuyên sâu theo Ngành: {active_stock_data.get('sector_name')}")
    if sector == "BANKING":
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.markdown("### 1. Thu nhập Thặng dư (Residual Income)")
            st.markdown(f"**Giá trị định giá**: `{int(ri_res['fair_value']):,} VNĐ`")
            st.markdown(f"- BVPS: {int(ri_res['bvps_0']):,} đ | Ke: {ri_res['cost_of_equity']}% | ROE: {ri_res['roe_expected']}%")
        with col_m2:
            st.markdown("### 2. P/B Điều chỉnh Nợ xấu")
            st.markdown(f"**Giá trị định giá**: `{int(pb_res['fair_value']):,} VNĐ`")
            st.markdown(f"- BVPS điều chỉnh: {int(pb_res['adjusted_bvps']):,} đ | P/B: {pb_res['target_pb']}x")
    elif sector == "REAL_ESTATE":
        st.markdown("### 1. Mô hình RNAV Chiết khấu Dự án & Quỹ đất")
        st.markdown(f"**Giá trị định giá**: `{int(rnav_res['fair_value']):,} VNĐ` (Trọng số 65%)")
        projects = active_stock_data.get("projects_rnav", [])
        if projects:
            st.dataframe(pd.DataFrame(projects), width="stretch")
    else:
        c_dcf, c_rel = st.columns(2)
        with c_dcf:
            st.markdown("### 1. Chiết khấu Dòng tiền (DCF FCFF)")
            st.markdown(f"**Giá trị định giá**: `{int(dcf_res['fair_value']):,} VNĐ`")
            st.markdown(f"- WACC: {dcf_res['wacc']}% | g vĩnh cửu: {dcf_res['growth_lt']}%")
            st.markdown(f"- Dòng tiền tự do chuẩn hóa: `{dcf_res['base_fcff']:,.1f} Tỷ VNĐ`")
        with c_rel:
            st.markdown("### 2. Định giá Tương đối Multiples (Deep Research 2.0)")
            st.markdown(f"- **P/E Chuẩn hóa ({rel_multiples['target_pe']}x)**: `{int(rel_multiples['pe_valuation']):,} VNĐ`")
            st.markdown(f"- **P/B ({rel_multiples['target_pb']}x)**: `{int(rel_multiples['pb_valuation']):,} VNĐ`")
            st.markdown(f"- **EV/EBITDA ({rel_multiples['target_ev_ebitda']}x)**: `{int(rel_multiples['ev_ebitda_valuation']):,} VNĐ`")
            st.markdown(f"- **PEG Fair Value (PEG=1.0)**: `{int(rel_multiples['peg_fair_value']):,} VNĐ`")
            st.markdown(f"- **Peter Lynch Ratio (R+G)/PE**: `{rel_multiples['peter_lynch_ratio']}x` {'(🟢 Hấp dẫn > 1.5)' if rel_multiples['is_peter_lynch_attractive'] else '(🟡 Trung bình)'}")
            st.markdown(f"- **Dải P/E Quá Nhiệt (+1.5SD)**: `{int(rel_multiples['pe_sell_overheat']):,} VNĐ`")
            st.markdown(f"- **Hiệu quả Vốn Dài Hạn ROCE**: `{roce_val}%`")

# ---------------------------------------------------------
# TAB 5: BCTC 5 NĂM
# ---------------------------------------------------------
with tab_bctc:
    st.subheader(f"Báo cáo Tài chính 5 Năm Gần Nhất — {current_symbol}")
    years = active_stock_data.get("years", ["2020", "2021", "2022", "2023", "2024"])
    rev = active_stock_data.get("revenue", [0]*len(years))
    np_profit = active_stock_data.get("net_profit", [0]*len(years))
    
    col_chart1, col_chart2 = st.columns(2)
    with col_chart1:
        st.write("##### Doanh thu & Lợi nhuận sau thuế (Tỷ VNĐ)")
        st.bar_chart(pd.DataFrame({"Năm": years, "Doanh thu": rev, "LNST": np_profit}).set_index("Năm"))
    with col_chart2:
        if sector != "BANKING":
            cfo_list = active_stock_data.get("cfo", [0]*len(years))
            capex_list = active_stock_data.get("capex", [0]*len(years))
            st.write("##### Dòng tiền CFO vs Capex (Tỷ VNĐ)")
            st.line_chart(pd.DataFrame({"Năm": years, "CFO": cfo_list, "Capex": capex_list}).set_index("Năm"))
            
    raw_table = {"Chỉ tiêu": ["Doanh thu thuần", "LNST cổ đông cty mẹ", "Vốn chủ sở hữu (Equity)"]}
    for idx, y in enumerate(years):
        raw_table[y] = [
            f"{rev[idx]:,}" if idx < len(rev) else "-",
            f"{np_profit[idx]:,}" if idx < len(np_profit) else "-",
            f"{active_stock_data.get('equity', 0):,}"
        ]
    st.table(pd.DataFrame(raw_table).set_index("Chỉ tiêu"))

# ---------------------------------------------------------
# TAB 6: DANH MỤC THEO DÕI (MY WATCHLIST)
# ---------------------------------------------------------
with tab_watchlist:
    st.subheader("📋 Bảng Danh Mục Cổ Phiếu Đã Định Giá (My Watchlist)")
    watchlist_items = get_watchlist()
    
    if watchlist_items:
        df_wl = pd.DataFrame(watchlist_items)
        cols_show = ["symbol", "name", "sector", "current_price", "target_price", "upside_pct", "recommendation", "f_score", "big_five", "scenario", "updated_at"]
        df_wl_show = df_wl[[c for c in cols_show if c in df_wl.columns]].copy()
        df_wl_show.columns = ["Mã CP", "Tên Doanh Nghiệp", "Ngành", "Thị Giá (đ)", "Giá Mục Tiêu (đ)", "Upside (%)", "Khuyến Nghị", "F-Score", "Big Five", "Kịch Bản", "Cập Nhật"]
        
        st.dataframe(
            df_wl_show.style.format({
                "Thị Giá (đ)": "{:,.0f} đ",
                "Giá Mục Tiêu (đ)": "{:,.0f} đ",
                "Upside (%)": "{:+.1f}%"
            }),
            width="stretch"
        )
        
        col_del1, col_del2 = st.columns([2, 1])
        with col_del1:
            sym_to_del = st.selectbox("Chọn mã để xóa khỏi danh mục:", options=[w["symbol"] for w in watchlist_items])
        with col_del2:
            st.write("")
            st.write("")
            if st.button("🗑️ Xóa Khỏi Danh Mục", use_container_width=True):
                remove_from_watchlist(sym_to_del)
                st.success(f"Đã xóa {sym_to_del}!")
                st.rerun()
    else:
        st.info("Chưa có cổ phiếu nào trong danh mục. Hãy bấm nút **'⭐ Lưu Cổ Phiếu Này Vào Danh Mục'** ở Tab đầu tiên để theo dõi nhé!")

# ---------------------------------------------------------
# TAB 7: LỊCH SỬ GIÁ
# ---------------------------------------------------------
with tab_chart:
    st.subheader(f"Biểu đồ Giá Lịch sử {current_symbol} (1 Năm Gần Nhất)")
    hist_df = get_price_history(current_symbol, period="1y")
    if not hist_df.empty:
        c_price = alt.Chart(hist_df).mark_line(color="#2563EB").encode(
            x=alt.X("Date:T", title="Thời gian"),
            y=alt.Y("Close:Q", title="Giá đóng cửa (VNĐ)", scale=alt.Scale(zero=False)),
            tooltip=["Date", "Close", "Volume"]
        ).properties(height=400)
        st.altair_chart(c_price, width="stretch")
    else:
        st.warning("Chưa có biểu đồ giá cho mã này.")
