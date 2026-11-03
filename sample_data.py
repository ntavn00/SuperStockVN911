"""
sample_data.py - Dữ liệu mẫu chuẩn xác của các cổ phiếu đại diện các nhóm ngành chính tại Việt Nam
Đơn vị tài chính: Tỷ VNĐ (Billion VND).
Đơn vị cổ phiếu: Cổ phiếu.
Đơn vị thị giá: VNĐ/cổ phiếu.
"""

SAMPLE_STOCKS = {
    "HPG": {
        "name": "CTCP Tập đoàn Hòa Phát",
        "symbol": "HPG",
        "exchange": "HOSE",
        "sector": "CYCLICAL_MANUFACTURING",
        "sector_name": "Sản xuất Chu kỳ & Thâm dụng vốn (Thép)",
        "description": "Tập đoàn sản xuất công nghiệp hàng đầu Việt Nam, chiếm hơn 35% thị phần thép xây dựng, chu kỳ vốn lớn, đang triển khai Dung Quất 2.",
        "shares_outstanding": 8442964520, # Sau các đợt trả cổ tức bằng CP
        "current_price_fallback": 21000.0,
        "beta": 1.25,
        "wacc_default": 11.5,
        "growth_longterm_default": 3.0,
        
        # Báo cáo 5 năm gần nhất (Tỷ VNĐ)
        "years": ["2020", "2021", "2022", "2023", "2024 (Ước)"],
        "revenue": [91279, 150865, 142771, 120355, 140500],
        "gross_profit": [19302, 41400, 16982, 13197, 18500],
        "ebit": [16800, 38500, 11200, 9400, 15200],
        "net_profit": [13506, 34521, 8444, 6800, 12000],
        "da": [5700, 6800, 6900, 6700, 7200], # Khấu hao D&A
        "capex": [8500, 12000, 18500, 22000, 26000], # Đang đầu tư mạnh Dung Quất 2
        "cfo": [14500, 21000, 16800, 18200, 17500],
        
        # Bảng cân đối kế toán năm gần nhất (Tỷ VNĐ)
        "cash_and_investments": 34500, # Tiền mặt + tiền gửi ngân hàng ngắn hạn
        "total_debt": 65000,          # Vay nợ ngắn + dài hạn
        "equity": 108000,             # Vốn chủ sở hữu
        "tangible_equity": 105000,    # Vốn CSH hữu hình (loại bỏ vô hình)
        
        # Tham số định giá theo ngành
        "peer_pe_median": 8.5,
        "peer_pb_median": 1.35,
        "peer_ev_ebitda_median": 6.8,
        "normalized_eps": 2450.0, # EPS chuẩn hóa xuyên chu kỳ (VNĐ)
        "bvps": 12800.0,          # Giá trị sổ sách / cổ phiếu (VNĐ)
    },
    
    "VCB": {
        "name": "Ngân hàng TMCP Ngoại thương Việt Nam (Vietcombank)",
        "symbol": "VCB",
        "exchange": "HOSE",
        "sector": "BANKING",
        "sector_name": "Ngân hàng Thương mại & Định chế Tài chính",
        "description": "Ngân hàng thương mại số 1 Việt Nam về chất lượng tài sản, tỷ lệ CASA dẫn đầu, trích lập dự phòng bao nợ xấu cao nhất hệ thống.",
        "shares_outstanding": 5589140000,
        "current_price_fallback": 56300.0,
        "beta": 0.85, # Phòng thủ, biến động thấp hơn thị trường
        "cost_of_equity": 11.0, # Ke
        "growth_longterm_default": 5.0,
        
        # Báo cáo 5 năm (Tỷ VNĐ)
        "years": ["2020", "2021", "2022", "2023", "2024 (Ước)"],
        "revenue": [49056, 56700, 68000, 74200, 81500], # Tổng thu nhập hoạt động (TOI)
        "net_interest_income": [36285, 42400, 53200, 58000, 64000], # Thu nhập lãi thuần (NII)
        "provision_expense": [9917, 11700, 9400, 6100, 6500], # Chi phí dự phòng rủi ro tín dụng
        "net_profit": [18450, 21900, 29900, 33000, 36500], # Lợi nhuận sau thuế
        
        # Bảng cân đối năm gần nhất
        "equity": 165000,       # Vốn chủ sở hữu (Tỷ VNĐ)
        "deposits": 1420000,    # Tiền gửi khách hàng
        "loans": 1310000,       # Cho vay khách hàng
        "npl_ratio": 0.98,      # Tỷ lệ nợ xấu (%) - Cực thấp
        "llr_ratio": 230.0,     # Tỷ lệ bao phủ nợ xấu (%)
        "nim": 3.25,            # Biên lãi thuần NIM (%)
        "casa": 34.0,           # Tỷ lệ tiền gửi không kỳ hạn (%)
        "car": 11.5,            # Hệ số an toàn vốn CAR (%)
        
        # Tham số định giá ngân hàng
        "roe_expected": 21.5,   # ROE dự phóng (%)
        "peer_pb_median": 1.95, # P/B của nhóm VCB thường cao hơn ngành do uy tín
        "peer_pe_median": 11.0,
        "bvps": 29500.0,        # BVPS hiện tại (VNĐ)
        "eps_current": 6500.0,  # EPS hiện tại (VNĐ)
    },
    
    "VHM": {
        "name": "CTCP Vinhomes",
        "symbol": "VHM",
        "exchange": "HOSE",
        "sector": "REAL_ESTATE",
        "sector_name": "Bất động sản Dân dụng & Quỹ đất",
        "description": "Nhà phát triển bất động sản lớn nhất Việt Nam, quỹ đất hàng nghìn hecta, sở hữu các đại đô thị Ocean Park, Grand Park, Smart City.",
        "shares_outstanding": 4354367488,
        "current_price_fallback": 63000.0,
        "beta": 1.15,
        "wacc_default": 12.0,
        
        # Báo cáo 5 năm (Tỷ VNĐ)
        "years": ["2020", "2021", "2022", "2023", "2024 (Ước)"],
        "revenue": [71547, 85094, 62392, 103334, 115000],
        "gross_profit": [27800, 48500, 30500, 36800, 42000],
        "net_profit": [28200, 39000, 29000, 33500, 34000],
        
        # Bảng cân đối năm gần nhất
        "cash_and_investments": 18500,
        "total_debt": 68000,
        "equity": 182000,
        "unearned_revenue": 38000, # Người mua trả tiền trước (cục lợi nhuận tương lai)
        "inventory": 55000,        # Hàng tồn kho dự án dở dang
        
        # Dữ liệu dự án chính phục vụ định giá RNAV (Tỷ VNĐ)
        "projects_rnav": [
            {"project": "Vinhomes Ocean Park 2 & 3", "pv_cashflow": 42000, "status": "Đang bàn giao & bán tiếp"},
            {"project": "Vinhomes Smart City & Grand Park", "pv_cashflow": 28000, "status": "Bàn giao giai đoạn cuối"},
            {"project": "Vinhomes Cần Giờ (Green Paradise)", "pv_cashflow": 65000, "status": "Dự án tương lai quy mô lớn"},
            {"project": "Vinhomes Hạ Long Xanh", "pv_cashflow": 55000, "status": "Dự án đại đô thị tương lai"},
            {"project": "Quỹ đất khác & BĐS KCN", "pv_cashflow": 35000, "status": "Quỹ đất dự trữ"}
        ],
        
        "peer_pb_median": 1.45,
        "peer_pe_median": 9.0,
        "bvps": 41800.0,
        "eps_current": 7800.0
    },
    
    "FPT": {
        "name": "CTCP FPT",
        "symbol": "FPT",
        "exchange": "HOSE",
        "sector": "TECHNOLOGY",
        "sector_name": "Công nghệ, Chuyển đổi số & Dịch vụ IT",
        "description": "Tập đoàn công nghệ và viễn thông hàng đầu Việt Nam, doanh thu dịch vụ CNTT nước ngoài tăng trưởng mạnh tại Nhật, Mỹ, châu Âu.",
        "shares_outstanding": 1460565000,
        "current_price_fallback": 52700.0,
        "beta": 0.90,
        "wacc_default": 10.5,
        "growth_longterm_default": 4.5,
        
        # Báo cáo 5 năm (Tỷ VNĐ)
        "years": ["2020", "2021", "2022", "2023", "2024 (Ước)"],
        "revenue": [29830, 35657, 44010, 52618, 62500],
        "gross_profit": [11800, 14100, 17200, 20100, 24000],
        "ebit": [4900, 6000, 7300, 8900, 10800],
        "net_profit": [3538, 4337, 5310, 6470, 7850],
        "cfo": [4800, 5600, 6800, 8100, 9500],
        "capex": [2800, 3200, 3800, 4500, 5000],
        
        # Bảng cân đối năm gần nhất
        "cash_and_investments": 28000, # Tiền mặt rất dồi dào
        "total_debt": 14500,
        "equity": 32000,
        
        "peer_pe_median": 20.0,
        "peer_pb_median": 4.5,
        "peg_benchmark": 1.1,
        "growth_rate_3y": 20.5, # Tăng trưởng LNST bình quân 20%/năm
        "bvps": 21900.0,
        "eps_current": 5370.0
    },

    "MSR": {
        "name": "CTCP Masan High-Tech Materials",
        "symbol": "MSR",
        "exchange": "UPCoM",
        "sector": "CYCLICAL_MANUFACTURING",
        "sector_name": "Khai khoáng & Vật liệu Công nghệ cao (Vonfram)",
        "description": "Nhà cung cấp vật liệu vonfram chế biến sâu hàng đầu thế giới ngoài Trung Quốc, sở hữu mỏ đa kim Núi Pháo và nền tảng vonfram H.C. Starck.",
        "shares_outstanding": 1099155420,
        "current_price_fallback": 16500.0,
        "beta": 1.30,
        "wacc_default": 12.0,
        "growth_longterm_default": 2.5,
        
        # Báo cáo tài chính (Tỷ VNĐ)
        "years": ["2020", "2021", "2022", "2023", "2024 (Ước)"],
        "revenue": [7291, 13564, 15550, 14090, 14800],
        "gross_profit": [1050, 2250, 2400, 1500, 1850],
        "ebit": [450, 1450, 1350, 420, 680],
        "net_profit": [43, 196, 105, -1530, -350], # 2023 lỗ do chi phí lãi vay cao & giá vonfram tạo đáy
        "da": [1600, 2100, 2300, 2200, 2250],
        "capex": [1200, 1800, 1950, 1400, 1300],
        "cfo": [1800, 2900, 2600, 1600, 1750],
        
        # Bảng cân đối gần nhất (Tỷ VNĐ)
        "cash_and_investments": 1450,
        "total_debt": 15800, # Nợ vay khá lớn
        "equity": 12500,
        
        "peer_pe_median": 12.0,
        "peer_pb_median": 1.25,
        "peer_ev_ebitda_median": 7.5,
        "normalized_eps": 850.0, # EPS khi giá vonfram hồi phục và giảm bớt nợ vay
        "bvps": 11370.0,
        "eps_current": -318.0
    }
}
