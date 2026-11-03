"""
storage.py - Quản lý Danh mục Theo dõi (Watchlist), Bộ nhớ đệm (Local Cache) và Xuất Báo cáo Excel
Dữ liệu được lưu trữ trực tiếp trên máy của người dùng (trong thư mục data/).
"""

import os
import json
import io
import pandas as pd
from datetime import datetime
from typing import Dict, Any, List

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
WATCHLIST_FILE = os.path.join(DATA_DIR, "watchlist.json")

def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(WATCHLIST_FILE):
        with open(WATCHLIST_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)

def get_watchlist() -> List[Dict[str, Any]]:
    ensure_data_dir()
    try:
        with open(WATCHLIST_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def save_to_watchlist(item: Dict[str, Any]) -> bool:
    ensure_data_dir()
    watchlist = get_watchlist()
    
    # Cập nhật nếu mã đã tồn tại, nếu chưa thì thêm mới
    symbol = item.get("symbol", "").upper()
    existing_idx = None
    for idx, w in enumerate(watchlist):
        if w.get("symbol", "").upper() == symbol:
            existing_idx = idx
            break
            
    item["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    if existing_idx is not None:
        watchlist[existing_idx] = item
    else:
        watchlist.insert(0, item)
        
    try:
        with open(WATCHLIST_FILE, "w", encoding="utf-8") as f:
            json.dump(watchlist, f, ensure_ascii=False, indent=2)
        return True
    except Exception:
        return False

def remove_from_watchlist(symbol: str) -> bool:
    ensure_data_dir()
    watchlist = get_watchlist()
    new_wl = [w for w in watchlist if w.get("symbol", "").upper() != symbol.upper()]
    try:
        with open(WATCHLIST_FILE, "w", encoding="utf-8") as f:
            json.dump(new_wl, f, ensure_ascii=False, indent=2)
        return True
    except Exception:
        return False

def export_valuation_to_excel(
    stock_data: Dict[str, Any],
    valuation_summary: List[Dict[str, Any]],
    gatekeepers: Dict[str, Any],
    rule_one_results: Dict[str, Any],
    verdict: Dict[str, Any]
) -> bytes:
    """
    Xuất báo cáo định giá hoàn chỉnh ra file Excel nhiều sheet chuẩn xác.
    """
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        # Sheet 1: Kết quả Định giá & Khuyến nghị
        df_summary = pd.DataFrame(valuation_summary)
        df_summary.to_excel(writer, index=False, sheet_name="Ket_Qua_Dinh_Gia")
        
        # Sheet 2: Sức khỏe & Con hào kinh tế (Moat)
        df_gate = pd.DataFrame({
            "Chỉ số kiểm tra": [
                "Big Five Moat (Con hào kinh tế)",
                "Piotroski F-Score (Chống gian lận BCTC)",
                "Altman Z''-Score (Rủi ro vỡ nợ)",
                "Biên An Toàn Khuyến Nghị (MOS)",
                "Phân Hạng Doanh Nghiệp"
            ],
            "Kết quả": [
                f"{gatekeepers.get('big_five_passed', 0)}/5 tiêu chuẩn đạt",
                f"{gatekeepers.get('f_score', 0)}/9 điểm ({gatekeepers.get('f_assessment', '')})",
                f"Z'' = {gatekeepers.get('z_score', 0)} ({gatekeepers.get('z_zone', '')})",
                f"{gatekeepers.get('mos_pct', 0)}%",
                gatekeepers.get('tier', '')
            ]
        })
        df_gate.to_excel(writer, index=False, sheet_name="Suc_Khoe_Moat")
        
        # Sheet 3: Bộ tứ Phil Town (Rule #1)
        df_r1 = pd.DataFrame({
            "Mô hình Phil Town & Buffett": [
                "1. Sticker Price (Giá niêm yết tương lai)",
                "   Giá mua an toàn MOS (Phil Town)",
                "2. Payback Time (Hoàn vốn 8 năm)",
                "   Số năm hoàn vốn ở thị giá hiện tại",
                "3. Giá 10 Cap (Owner Earnings * 10)",
                "4. Giá Trị Xác Sống (Zombie Value / Net-Net)"
            ],
            "Giá trị tính ra (VNĐ)": [
                f"{int(rule_one_results.get('sticker_price', 0)):,} đ",
                f"{int(rule_one_results.get('mos_price', 0)):,} đ",
                f"{int(rule_one_results.get('payback_price', 0)):,} đ",
                f"{rule_one_results.get('actual_payback_years', 'N/A')} năm",
                f"{int(rule_one_results.get('ten_cap_price', 0)):,} đ",
                f"{int(rule_one_results.get('zombie_price', 0)):,} đ"
            ]
        })
        df_r1.to_excel(writer, index=False, sheet_name="Quy_Tac_So_1_Phil_Town")
        
        # Sheet 4: BCTC 5 Năm
        years = stock_data.get("years", ["2020", "2021", "2022", "2023", "2024"])
        df_fin = pd.DataFrame({
            "Năm": years,
            "Doanh thu thuần (Tỷ)": stock_data.get("revenue", [0]*len(years)),
            "LNST Cty mẹ (Tỷ)": stock_data.get("net_profit", [0]*len(years)),
            "Dòng tiền CFO (Tỷ)": stock_data.get("cfo", [0]*len(years)) if "cfo" in stock_data else [0]*len(years),
            "Chi tiêu Capex (Tỷ)": stock_data.get("capex", [0]*len(years)) if "capex" in stock_data else [0]*len(years)
        })
        df_fin.to_excel(writer, index=False, sheet_name="BCTC_5_Nam")
        
        # Sheet 5: Benjamin Graham & Mục Tiêu Bán (Deep Research 2.0)
        graham = rule_one_results.get("graham", {})
        targets = verdict.get("targets", {})
        df_ext = pd.DataFrame({
            "Chỉ tiêu Nâng cao": [
                "Graham 1 (Tăng trưởng cơ bản)",
                "Graham 2 (Điều chỉnh TPCP VN 10Y)",
                "Con Số Graham (Graham Number)",
                "Giá Mua An Toàn (P_Buy)",
                "Giá Bán Mục Tiêu 1 (Chốt lời hợp lý)",
                "Giá Bán Quá Nhiệt 2 (Chốt lời cao trào)",
                "Tỷ lệ Lợi nhuận/Rủi ro (Win/Loss)"
            ],
            "Giá trị": [
                f"{int(graham.get('graham_1_price', 0)):,} đ",
                f"{int(graham.get('graham_2_price', 0)):,} đ",
                f"{int(graham.get('graham_number', 0)):,} đ",
                f"{int(targets.get('target_buy_price', 0)):,} đ",
                f"{int(targets.get('target_sell_1', 0)):,} đ",
                f"{int(targets.get('target_sell_2', 0)):,} đ",
                f"{targets.get('win_loss_ratio', 0)}x"
            ]
        })
        df_ext.to_excel(writer, index=False, sheet_name="Graham_Va_Gia_Ban")
        
    output.seek(0)
    return output.getvalue()
