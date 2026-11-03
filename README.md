# 📈 SUPER STOCK VALUATION ENGINE V3.0 (VIỆT NAM 🇻🇳)

Hệ thống Định giá Cổ phiếu Giá trị Thực chiến (Data-Driven Quant Engine V3.0) dành riêng cho Thị trường Chứng khoán Việt Nam (HOSE, HNX, UPCoM) — Kết hợp trường phái **Warren Buffett**, **Phil Town (Rule #1)**, **Benjamin Graham** và **Aswath Damodaran**, được bản địa hóa theo chuẩn kế toán Việt Nam (**VAS / Thông tư 200 & Thông tư 99/2025/TT-BTC**).

---

## 🌟 TÍNH NĂNG CỐT LÕI (PHIÊN BẢN 3.0)

1. **Tự Động Tải BCTC & Thị Giá Live 100% Miễn Phí (Không Cần API Key)**:
   - Chỉ cần nhập mã cổ phiếu bất kỳ (`HPG`, `GEE`, `FPT`, `VCB`, `MWG`, `DGC`, `SSI`...), hệ thống tự động kết nối Yahoo Finance & SSI iBoard để lấy thị giá thời gian thực, BCTC 5 năm, số liệu TTM khử nhiễu bán niên và phân vị giá 52 tuần.
2. **Bản Địa Hóa Kế Toán Việt Nam (VAS Normalization)**:
   - Tự động khấu trừ **Rò rỉ Quỹ Khen thưởng Phúc lợi (Tài khoản 353)** ra khỏi EPS và Dòng tiền Chủ sở hữu (**Owner Earnings**).
   - Bóc tách lợi nhuận đột biến một lần (bán tài sản/thoái vốn) để tính **Core Normalized EPS**.
3. **Tầng Lọc Con Hào Kinh Tế & Chống Bẫy Giá Trị (Gatekeepers)**:
   - **Big Five Moat CAGR ($\ge 10\%/\text{năm}$)**, **Piotroski F-Score (thang 9 điểm)**, **Altman Z''-Score** (miễn trừ Ngân hàng & khử bẫy vốn lưu động âm ngành Bán lẻ), và **Bảng Thẩm Định Định Tính 5 Tiêu Chí**.
4. **Hội Tụ Định Giá Đa Mô Hình Không Trừ Kép MOS (Single-Pass Elastic MOS)**:
   - Phối hợp **70% Giá trị Nội tại (Pre-MOS Fair Value)**: `Sticker Price Ke (Decay Growth)`, `Payback Time Sức Mua Thực`, `Buffett Owner Earnings Valuation`, và `DCF FCFF (Damodaran Reinvestment) / Residual Income / RNAV`.
   - Phối hợp **30% Đa Bội Số Tương Đối Thực Nghiệm 5 Năm**: `P/E Chuẩn hóa`, `EV/EBITDA`, `P/B điều chỉnh ROE`.
   - Tích hợp **Bộ 3 Công thức Benjamin Graham** bản địa hóa theo Lợi suất Trái phiếu Chính phủ Việt Nam 10 năm ($R_f$).
5. **Ma Trận Rải Lệnh Giải Ngân 3 Giai Đoạn (Time & Value Tranching)**:
   - **Tranche 1 (30% Vốn)**: Điểm mua tích lũy trong nhịp chỉnh hàng năm (neo theo phân vị `p25` 52 tuần & $-1\text{SD}$).
   - **Tranche 2 (40% Vốn)**: Điểm mua giá trị chuẩn mực (khớp `MOS Động` $15\% - 25\%$).
   - **Tranche 3 (30% Vốn)**: Điểm mua khủng hoảng chu kỳ / Sàn giá trị sổ sách hữu hình ($1.0\text{x}\text{ BVPS}$ & $-2\text{SD}$).

---

## 🌐 CÁCH 1: CHIA SẺ QUA LINK WEB MIỄN PHÍ (STREAMLIT CLOUD — KHUYÊN DÙNG)

Khi đẩy code lên GitHub, bạn có thể tạo một đường link Web miễn phí (ví dụ: `https://super-stock-vn.streamlit.app`) để bạn bè mở trực tiếp trên **điện thoại hoặc máy tính** mà **không cần cài đặt Python**:

1. Đăng nhập vào [https://share.streamlit.io](https://share.streamlit.io) bằng tài khoản GitHub của bạn.
2. Bấm **Create app** $\rightarrow$ chọn Repository GitHub chứa dự án này.
3. Chọn Branch: `main` và Main file path: `app.py`.
4. Bấm **Deploy!** $\rightarrow$ Sau 1 phút, bạn sẽ có đường link Web để gửi cho bạn bè cùng sử dụng!

---

## 💻 CÁCH 2: CHẠY TRỰC TIẾP TRÊN MÁY TÍNH CÁ NHÂN

1. Cài đặt Python 3.10+ và tải mã nguồn về máy:
   ```bash
   git clone <link-github-repo-cua-ban>
   cd "Super Stock"
   pip install -r requirements.txt
   ```
2. Khởi chạy ứng dụng:
   - **Trên Windows**: Click đúp vào file `run_app.bat`.
   - **Hoặc qua Terminal**:
     ```bash
     python -m streamlit run app.py
     ```
3. Mở trình duyệt tại `http://localhost:8501`.
