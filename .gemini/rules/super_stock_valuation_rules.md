# BỘ QUY TẮC ĐỊNH GIÁ CỔ PHIẾU SUPER STOCK VIỆT NAM (VALUATION ENGINE RULES)
## PHIÊN BẢN CHUẨN ĐỊNH LƯỢNG 3.0 — HỆ THỐNG ĐỊNH GIÁ THỰC NGHIỆM CHỐNG TRỪ KÉP & KIỂM CHỨNG BIÊN ĐỘ 52 TUẦN (2020–2026)

Bộ quy tắc này là tiêu chuẩn bắt buộc áp dụng cho toàn bộ quá trình thu thập dữ liệu, làm sạch kế toán (Data Normalization), nhận diện chu kỳ thị trường, chạy mô hình định giá, tầng lọc con hào và xuất báo cáo đầu tư cho thị trường chứng khoán Việt Nam (HOSE, HNX, UPCoM).

---

### 0. 6 NGUYÊN TẮC BẤT DI BẤT DỊCH TỪ KẾT QUẢ TỰ KIỂM CHỨNG ĐỊNH LƯỢNG (V3.0 SELF-AUDIT MANDATES)

1. **Cấm Tuyệt Đối Trừ Biên An Toàn Kép (Zero Double-MOS Discounting)**:
   - Hội tụ Nội tại ($P_{\text{Intrinsic Fair}}$) **bắt buộc** phải lấy trung bình có trọng số của các **Giá Trị Hợp Lý Trước MOS (Pre-MOS Fair Values)**: `Sticker_Price_Ke`, `Payback_10Y_Real`, `Owner_Earnings_Fair_Value`, và `DCF_FCFF / Residual_Income / RNAV`.
   - Chỉ được trừ Biên An Toàn ($MOS_{\text{Adaptive}}$) **đúng 1 lần duy nhất** sau khi đã tổng hợp ra `Master Fair Value` ($70\% \text{ Nội tại Pre-MOS} + 30\% \text{ Tương đối Pre-MOS}$).
2. **Bộ Lọc Khử Nhiễu TTM & Chống Cộng Trùng BCTC Bán Niên (Sanitized TTM & Split-Sync)**:
   - Luôn cập nhật lợi nhuận 4 quý gần nhất (TTM) và số lượng cổ phiếu lưu hành mới nhất (MRQ), nhưng nếu lợi nhuận TTM trên Yahoo Finance nhảy vọt $> 22\%$ so với BCTC kiểm toán năm gần nhất (do lỗi cộng trùng BCTC Bán niên 6 tháng của Yahoo `.VN`), tự động chuẩn hóa bằng trung bình $50\%$ năm kiểm toán gần nhất + $50\%$ dự phóng Forward EPS của giới phân tích.
3. **Chấm Dứt Tham Số Cứng Áp Đặt — Thay Bằng Dữ Liệu Thực Nghiệm 5 Năm (Empirical Data-Driven Inputs)**:
   - Toàn bộ $CAGR_{\text{BVPS}}$, $ROIC$, $ROE$, Hệ số $\beta$, Trung vị $P/E$ 5 năm ($\mu_{PE}$), Độ lệch chuẩn $\sigma_{PE}$, và $P/B$ hợp lý theo $ROE$ đều phải trích xuất tự động từ lịch sử BCTC 5 năm và chuỗi giá giao dịch 5 năm của chính doanh nghiệp đó kết hợp chuẩn ngành (`SECTOR_BENCHMARKS`).
4. **Chiết Khấu Sức Mua Thực Trong Payback Time & Định Luật Tái Đầu Tư Damodaran Trong DCF**:
   - Trong `Payback Time`: không cộng ngang dòng tiền danh nghĩa với $r = 0\%$; bắt buộc chiết khấu trượt giá sức mua đồng tiền $5.0\%/\text{năm}$ tại Việt Nam ($g_{\text{real}} = \frac{1+g}{1.05} - 1$).
   - Trong `DCF FCFF`: áp dụng Định luật Tái đầu tư cơ bản của Aswath Damodaran ($\text{Reinvestment Rate} = \frac{g}{\text{ROIC}}$, $\text{FCFF} = \text{NOPAT} \times (1 - \text{Reinvestment Rate})$) để không thổi phồng dòng tiền tự do của các doanh nghiệp thâm dụng vốn.
5. **Bất Đẳng Thức Thứ Bậc Nghiêm Ngặt Cho 3 Tranche Giải Ngân (Strict Monotonic Hierarchy)**:
   - Bắt buộc thỏa mãn tuyệt đối:
     $$P_{\text{Master Fair Value}} > P_{\text{Tranche 1 (Tích lũy)}} > P_{\text{Tranche 2 (Chuẩn MOS)}} > P_{\text{Tranche 3 (Khủng hoảng / Sàn P/B)}}$$
   - Nghiêm cấm hiện tượng đảo ngược $P_{\text{Tranche 2}} > P_{\text{Tranche 1}}$.
6. **Kiểm Chứng Khả Thi Thực Nghiệm 52 Tuần (52-Week Empirical Reachability Check)**:
   - Mọi mức giá mua khuyến nghị (`Tranche 1`, `Tranche 2`, `Tranche 3`) phải được đối chiếu tự động với phân vị giá giao dịch thực tế 1 năm qua (`price_1y_min`, `price_1y_p15`, `price_1y_p25`, `price_1y_max`) và Giá trị sổ sách hữu hình ($1.0\text{x}\text{ BVPS}$).

---

### 1. NGUYÊN TẮC BẢN ĐỊA HÓA KẾ TOÁN VIỆT NAM (VAS & THÔNG TƯ 99/2025/TT-BTC)

1. **Khấu Trừ Rò Rỉ Quỹ Khen Thưởng Phúc Lợi (Tài Khoản 353)**:
   - Theo chuẩn VAS và Thông tư 99/2025/TT-BTC, tiền trích Quỹ KTPL (3531, 3532, 3534) không đi qua chi phí KQKD mà trích thẳng từ LNST chưa phân phối (TK 421).
   - **Bắt buộc** chuẩn hóa:
     $$\text{Adjusted EPS} = \frac{\text{LNST CĐ Cty Mẹ} - \text{Trích Quỹ KTPL (TK 353)} - \text{Cổ tức CP Ưu đãi}}{\text{Số lượng CP Lưu hành Bình quân Pha loãng}}$$
   - Khi cào BCTC theo quý, sử dụng tỷ lệ trích quỹ làm mượt lịch sử $\tau_{\text{KTPL}} = 5.0\%$ (hoặc trung bình 3 năm) để triệt tiêu độ nhiễu giữa các quý.
2. **Chuẩn Hóa Lợi Nhuận Bất Thường (Unusual Items)**:
   - Bóc tách doanh thu tài chính một lần (thoái vốn công ty con, chuyển nhượng dự án) để tính **Core Normalized EPS** trước khi đưa vào mô hình tăng trưởng.

---

### 2. TẦNG LỌC SỨC KHỎE TÀI CHÍNH & CON HÀO KINH TẾ (GATEKEEPERS)

1. **Bộ Ngũ Tăng Trưởng (Big Five Moat CAGR $\ge 10\%/năm$)**:
   - Tăng trưởng 5 năm trên: Doanh thu thuần, EPS pha loãng, Vốn CSH (BVPS), Dòng tiền tự do FCF/CFO, và Tỷ suất $ROIC \ge 10\%$.
   - Quản trị nợ: $\text{Nợ dài hạn (Mã 338)} / \text{FCF} \le 3.0 \text{ năm}$.
2. **Thang Điểm Piotroski F-Score (0 đến 9 điểm)**:
   - $\ge 7$ điểm: Doanh nghiệp xuất sắc (Winners).
   - $5 - 6$ điểm: Doanh nghiệp ổn định.
   - $\le 4$ điểm: Nguy cơ suy thoái, bẫy giá trị (Losers).
3. **Altman Z''-Score (Emerging Markets & Thâm Dụng Vốn)**:
   - $Z'' = 6.56 X_1 + 3.26 X_2 + 6.72 X_3 + 1.05 X_4$.
   - **Quy tắc ngoại lệ**: 
     + Miễn trừ hoàn toàn cho Ngân hàng, Chứng khoán, Bảo hiểm.
     + Doanh nghiệp bán lẻ/tiêu dùng chiếm dụng vốn nhà cung cấp ($X_1 < 0$): nếu $CFO > 0$ và $EBIT > 0$, chuẩn hóa $X_1 = 0$ để tránh báo động phá sản giả.
4. **Bảng Thẩm Định Định Tính (Qualitative Moat Checklist)**:
   - Chiếm 30% trọng số chất lượng: Ban lãnh đạo minh bạch không rút ruột/ESOP quá đà, Sức mạnh định giá (Pricing Power), Rào cản gia nhập ngành, Chi phí chuyển đổi khách hàng.

---

### 3. THUẬT TOÁN NHẬN DIỆN CHU KỲ THỊ TRƯỜNG LÕI & CHÊNH LỆCH LỢI SUẤT THU NHẬP (CORE MARKET & EYS)

Không được dùng $P/E$ bề mặt của VN-Index làm tham chiếu vĩ mô vì bị bóp méo bởi các cổ phiếu vốn hóa lớn đột biến (như VIC $P/E \approx 73\text{x}$, VPL $P/E \approx 56\text{x}$ đẩy $P/E$ phi tài chính bề mặt lên $22.5\text{x}$ trong khi thực tế phần lõi chỉ $12.0\text{x} - 14.7\text{x}$).

1. **Hệ số Định Giá Thị Trường Lõi ($PE_{\text{Core Market}}$)**:
   $$PE_{\text{Core Market}} = \frac{\sum_{i \in \text{VN-Index}, \; PE_i \le 40} \text{Vốn hóa}_i}{\sum_{i \in \text{VN-Index}, \; PE_i \le 40} LNST_{\text{Thực}, i}}$$
   (Hoặc lấy $P/E$ của chỉ số VN100).
2. **Chênh Lệch Lợi Suất Thu Nhập ($EYS_{\text{Market}}$)**:
   $$EYS_{\text{Market}} = \left( \frac{1}{PE_{\text{Core Market}}} \right) - R_{f(10Y\text{ VGB})}$$
   với Lãi suất Trái phiếu Chính phủ Việt Nam 10 năm $R_f \approx 4.5\% - 4.58\%$.
3. **Quy Tắc Phân Loại 3 Pha Chu Kỳ Thị Trường**:
   - **Pha Rẻ Lịch sử / Đáy Chu kỳ ($PE_{\text{Core}} \le 12.0\text{x}$ hoặc $EYS_{\text{Market}} \ge 3.8\%$)**: Kích hoạt hạn mức giải ngân tối đa; giảm yêu cầu MOS cơ sở đi $\Delta MOS_{\text{Chu kỳ}} = 5\%$.
   - **Pha Hợp lý / Tăng trưởng Cơ sở ($12.0\text{x} < PE_{\text{Core}} \le 14.9\text{x}$ hoặc $2.2\% \le EYS < 3.8\%$)**: Định giá cân bằng quanh mốc trung bình 10 năm ($14.9\text{x}$); kích hoạt chiến lược tích lũy theo dải điều chỉnh hàng năm.
   - **Pha Quá nhiệt / Đỉnh Chu kỳ ($PE_{\text{Core}} > 16.5\text{x}$ hoặc $EYS < 1.5\%$)**: Phần bù rủi ro quá mỏng so với lãi suất phi rủi ro; siết chặt MOS lên tối đa, chủ động giữ tiền mặt/trái phiếu ngắn hạn.

---

### 4. THUẬT TOÁN STICKER PRICE THÍCH ỨNG CHI PHÍ VỐN THỰC TẾ & BIÊN AN TOÀN CO GIÃN (ELASTIC MOS)

Để triệt tiêu bẫy **"Cộng dồn Bảo thủ / Đứng ngoài 10 năm"** (vừa dùng chiết khấu MARR 15% vừa cắt MOS 50% ép $P/E$ mua xuống dưới $5.33\text{x} - 9.0\text{x}$), tách quy trình định giá thành 2 bước độc lập:

1. **Bước 1 — Giá Trị Hợp Lý Nội Tại ($P_{\text{Fair Sticker (Adjusted)}}$) bằng Chi Phí Vốn Thực Tế ($K_e$)**:
   $$r_{\text{Discount}} = \max\left(10.0\%, \; R_f(4.5\%) + \beta_{\text{Bottom-up}} \times ERP_{\text{VN}}(7.5\%)\right)$$
   Áp dụng mô hình Tăng trưởng Giảm dần (Decay / Fade Model) 10 năm:
   $$P_{\text{Fair Sticker (Adjusted)}} = \frac{EPS_{\text{Chuẩn hóa}} \times (1 + g_{\text{Decay}})^{10} \times PE_{\text{Future}}}{(1 + r_{\text{Discount}})^{10}}$$
2. **Bước 2 — Biên An Toàn Co Giãn Động ($MOS_{\text{Adaptive}}$)**:
   $$MOS_{\text{Adaptive}} = MOS_{\text{Cơ sở theo Hạng Cổ phiếu}} - \Delta MOS_{\text{Chu kỳ Thị trường}}$$
   - **Hạng 1 (Quality Compounders — Big Five $\ge 10\%$, F-Score 8–9, Z-Score An toàn)**: $MOS_{\text{Cơ sở}} = 25\%$. Trong pha thị trường rẻ ($PE_{\text{Core}} \le 12.5\text{x}$), $\Delta MOS = 5\% \implies MOS_{\text{Adaptive}} = 20\%$.
   - **Hạng 2 (Solid Value — Big Five 4/5, F-Score 6–7)**: $MOS_{\text{Cơ sở}} = 35\%$ (Chuẩn Seth Klarman).
   - **Hạng 3 (Chu kỳ sâu / Vùng xám)**: $MOS_{\text{Cơ sở}} = 50\%$ (Chuẩn Phil Town cổ điển).
3. **Sticker Price Cổ Điển (Phil Town Classic)**:
   Vẫn tính $P_{\text{Sticker (15\%)}} = P_{10} / (1.15)^{10}$ và $P_{\text{Sticker}} \times 0.50$ làm điểm chặn mua Khủng hoảng (Tranche 3).

---

### 5. BẮT NHỊP BIẾN ĐỘNG NỘI NIÊN 50% & TỶ LỆ WIN-LOSS RATIO

1. **Cận Dưới Dải Độ Lệch Chuẩn 5 Năm ($-1\sigma$ và $-2\sigma$)**:
   $$P_{\text{Lịch sử (-1SD)}} = EPS_{\text{Dự phóng}} \times (\mu_{PE(5Y)} - 1.0 \times \sigma_{PE(5Y)})$$
   $$P_{\text{Lịch sử (-2SD)}} = EPS_{\text{Dự phóng}} \times (\mu_{PE(5Y)} - 2.0 \times \sigma_{PE(5Y)})$$
2. **Tỷ Lệ Thắng / Thua (Win-Loss Ratio)**:
   $$\text{Win-Loss Ratio} = \frac{P_{\text{Master Fair Value}} - P_{\text{Market}}}{P_{\text{Market}} - P_{\text{Worst}}} \ge 2.0$$
   với $P_{\text{Worst}} = \min(P_{\text{Lịch sử (-2SD)}}, \; \max(0, P_{\text{Zombie}}))$ hoặc $P_{\text{Lịch sử (-2SD)}}$.
3. **Thời Gian Hoàn Vốn Linh Hoạt (Adjusted Payback Time)**:
   - Với Cổ phiếu Hạng 1 (Dòng tiền ổn định, Moat mạnh): Cho phép ngưỡng $\text{Payback Time} \le 10 \text{ năm}$ (tương đương chuẩn 10 Cap hoàn vốn 100% trong 10 năm).
   - Với Cổ phiếu Hạng 2 & Hạng 3: Giữ nguyên chuẩn $\le 8 \text{ năm}$.

---

### 6. MA TRẬN RẢI LỆNH GIẢI NGÂN 3 GIAI ĐOẠN TRONG 6–9 THÁNG (TIME & VALUE TRANCHING)

Chuyển đổi khuyến nghị từ nhị phân ("Mua / Đứng ngoài") sang hệ thống tích lũy 3 tầng vốn:

| Vùng Giải Ngân | Tỷ Trọng Vốn | Công Thức Định Giá Kích Hoạt | Điều Kiện Tối Thiểu | Bối Cảnh Thị Trường |
| :--- | :---: | :--- | :--- | :--- |
| **Tranche 1: Điểm Mua Tích Lũy Hàng Năm (Entry Zone)** | **30% Vị Thế** | $$P_{\text{Tranche 1}} = \max\left(P_{\text{Fair}} \times 0.80, \; P_{\text{Lịch sử (-1SD)}}\right)$$ | Thị giá chiết khấu 15%–20% so với $P_{\text{Fair}}$ HOẶC chạm $-1\text{SD}$; Win-Loss $\ge 1.8$; Payback $\le 10$ năm. | Nhịp điều chỉnh bình thường hàng năm (RSI < 40 vòng lên). |
| **Tranche 2: Điểm Mua Giá Trị Chuẩn Mực (Core Value Zone)** | **40% Vị Thế** | $$P_{\text{Tranche 2}} = \max\left(P_{\text{Fair}} \times 0.65, \; P_{\text{10Cap}}, \; P_{\text{Payback 8Y}}\right)$$ | Thị giá chiết khấu 30%–35% so với $P_{\text{Fair}}$ HOẶC chạm 10 Cap; Win-Loss $\ge 2.8$; Payback $\le 8$ năm. | $PE_{\text{Core Market}}$ lùi về $11.4\text{x} - 12.5\text{x}$ do khối ngoại bán ròng / chỉnh trung hạn. |
| **Tranche 3: Điểm Mua Khủng Hoảng Chu Kỳ (Deep MOS Zone)** | **30% Còn Lại** | $$P_{\text{Tranche 3}} = \min\left(P_{\text{Sticker (15\%)}} \times 0.50, \; P_{\text{Lịch sử (-2SD)}}\right)$$ | Thị giá chiết khấu 50% theo Rule #1 gốc ($MARR = 15\%$, $MOS = 50\%$) HOẶC chạm $-2\text{SD}$ / Zombie Value; Payback $\le 6$ năm. | Cú sốc thanh khoản toàn sàn / sụp đổ chu kỳ (3–5 năm xuất hiện 1 lần). |

---

### 7. MA TRẬN 8 PHÂN NGÀNH CHUYÊN SÂU & MÔ HÌNH ĐỊNH GIÁ TỐI ƯU

| STT | Phân Ngành | Mô Hình Định Giá Nội Tại (70%) | Mô Hình Định Giá Tương Đối (30%) | Quy Tắc Đặc Thù |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Ngân hàng Thương mại** *(VCB, BID, CTG, ACB, MBB, TCB)* | Residual Income (RI) + BVPS Sticker | $P/B$ hồi quy theo $ROE$ | Khấu trừ nợ xấu chưa trích lập $\max(0, \text{NPL} - \text{LLR})$ vào $BVPS_0$. |
| **2** | **Công ty Chứng khoán** *(SSI, VND, HCM, VCI, MBS, VIX)* | Mark-to-Market NAV + BVPS Compounding | $P/B$ phân tầng theo thị phần | Đánh giá lại danh mục FVTPL theo giá thị trường. |
| **3** | **Bảo hiểm** *(BVH, PVI, MIG, BMI, PTI)* | Chiết khấu Cổ tức (DDM) + Residual Income | $P/B - ROE$ + Dividend Yield | Hưởng lợi khi lợi suất TPCP $R_f$ tăng. |
| **4** | **Bất động sản Dân dụng & KCN** *(VHM, KDH, NLG, KBC, IDC, BCM)* | RNAV / SOTP chiết khấu dự án | $P/B$ và $P/\text{RNAV}$ | Chỉ tính thặng dư đất khi $\text{Người mua trả trước} / \text{Tồn kho} \ge 15\%$. BĐS KCN kết hợp 50% RNAV + 50% 10 Cap. |
| **5** | **Bán lẻ & FMCG** *(VNM, MSN, MWG, PNJ, FRT, SAB)* | Rule #1 + DCF 2 giai đoạn | $P/E$, $PEG$, $P/S$ | Áp dụng $P/S$ cho chuỗi đang mở rộng; theo dõi SSSG. |
| **6** | **Công nghệ & Viễn thông** *(FPT, CMG, CTR, FOX, ELC)* | Sticker Price (MOS 20–25%) + DCF | $PEG$ ($PEG = 1$ là fair value) | Không dùng P/B; dùng PEG và Forward P/E. |
| **7** | **Sản xuất Chu kỳ & Vật liệu** *(HPG, HSG, DGC, DPM, DCM, BSR, PVT)* | DCF + Sticker Mid-Cycle | $EV/EBITDA$, $EV/EBIT$, $P/B$ chu kỳ | Chuẩn hóa EPS/FCF giữa chu kỳ 5–7 năm. |
| **8** | **Điện, Nước, Hạ tầng & Cảng** *(REE, GEE, BWE, NT2, POW, GMD, ACV)* | 10 Cap Owner Earnings + DCF FCFF | $EV/EBITDA$ + $(R+G)/PE > 1.5$ | Tách biệt CapEx bảo trì khỏi CapEx mở rộng. |

---

### 8. CÁC MỐC GIÁ BÁN MỤC TIÊU (EXIT STRATEGY)

1. **$P_{\text{Sell 1}}$ (Chốt Lời Cơ Bản / Tái Cân Bằng)**:
   - Khi thị giá chạm hoặc vượt $P_{\text{Master Fair Value}}$ (hoặc tỷ lệ Win-Loss $< 1.0$). Khuyến nghị hiện thực hóa lợi nhuận một phần (30% - 50% danh mục).
2. **$P_{\text{Sell 2}}$ (Chốt Lời Cao Trào / Vùng Quá Nhiệt)**:
   - Khi thị giá chạm Cận trên Dải P/E lịch sử ($+1.5\text{SD}$ đến $+2.0\text{SD}$) HOẶC vượt $P_{\text{Fair}} + 25\%$ (tỷ lệ Win-Loss $< 0.5$). Khuyến nghị tất toán vị thế và chuyển dịch sang tài sản phòng thủ (tiền gửi / trái phiếu ngắn hạn).
