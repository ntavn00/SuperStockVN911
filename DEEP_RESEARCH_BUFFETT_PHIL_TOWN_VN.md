# KIẾN TRÚC THUẬT TOÁN ĐỊNH GIÁ CỔ PHIẾU ĐA NGÀNH TẠI THỊ TRƯỜNG VIỆT NAM
## BẢN CẬP NHẬT CHUYÊN SÂU TOÀN DIỆN (DEEP RESEARCH 2.0)
> **Nguồn**: Gemini Deep Research (https://share.gemini.google/97G5GybnME7H)
> **Phạm vi**: 8 Nhóm Ngành, Bộ 3 Công thức Benjamin Graham, Dải P/E Lịch sử, Tỷ lệ Win-Loss & Giá Bán Mục Tiêu

---

Kiến trúc Thuật toán Định giá Cổ phiếu Đa Ngành tại Thị trường Việt Nam theo Trường phái Warren Buffett và Phil Town
1. Bản chất Định giá Giá trị và Yêu cầu Bản địa hóa Dữ liệu tại Việt Nam

Việc xây dựng một hệ thống định giá cổ phiếu tự động trên nền tảng Antigravity đòi hỏi sự chuyển hóa các nguyên lý định tính và định lượng của Warren Buffett và Phil Town thành các thuật toán toán học chặt chẽ. Trọng tâm của trường phái đầu tư giá trị hiện đại không nằm ở việc dự báo chính xác tuyệt đối biến động thị trường ngắn hạn, mà nằm ở việc xác định Giá trị Nội tại (Intrinsic Value) của những doanh nghiệp sở hữu lợi thế cạnh tranh bền vững (Moat) và chỉ giải ngân khi thị giá chiết khấu sâu so với giá trị thực nhằm thiết lập Biên An toàn (Margin of Safety - MOS). Trong khi Warren Buffett đặt nền móng với khái niệm Dòng tiền Chủ sở hữu (Owner Earnings) và chiết khấu dòng tiền (DCF), Phil Town đã chuẩn hóa triết lý này thành hệ thống Quy tắc Số 1 (Rule #1 Investing) với bốn phương pháp định giá hội tụ gồm Giá Niêm yết (Sticker Price), Giá 10 Cap (10 Cap Price), Thời gian Hoàn vốn (Payback Time) và Giá trị Xác sống (Zombie Value).   

Tuy nhiên, một sai lầm phổ biến trong các công cụ định giá tự động là áp dụng một công thức chiết khấu dòng tiền hoặc bội số P/E duy nhất cho toàn bộ thị trường. Cấu trúc bảng cân đối kế toán và cơ chế ghi nhận doanh thu của một ngân hàng thương mại, một nhà phát triển bất động sản, một tập đoàn sản xuất thép hay một doanh nghiệp bán lẻ là hoàn toàn khác biệt. Hơn thế nữa, khi áp dụng các công thức của Phố Wall vào thị trường chứng khoán Việt Nam, thuật toán bắt buộc phải xử lý các độ lệch chuẩn mực kế toán theo Chuẩn mực Kế toán Việt Nam (VAS), đặc biệt là sự chuyển dịch pháp lý từ Thông tư 200/2014/TT-BTC sang Thông tư 99/2025/TT-BTC có hiệu lực từ ngày 01/01/2026. Nếu không làm sạch dữ liệu đầu vào (Data Normalization), mọi mô hình định giá tự động sẽ rơi vào trạng thái sai lệch hệ thống, khiến nhà đầu tư mua nhầm các bẫy giá trị (Value Traps) hoặc định giá cao hơn thực tế từ 15% đến 30%.   

Xử lý Rò rỉ Lợi nhuận từ Quỹ Khen thưởng Phúc lợi và Pha loãng Cổ phiếu

Điểm khác biệt cốt lõi nhất giữa báo cáo tài chính (BCTC) theo chuẩn VAS và chuẩn quốc tế (IFRS/US GAAP) ảnh hưởng trực tiếp đến mọi công thức định giá của Buffett và Phil Town là khoản mục Quỹ khen thưởng, phúc lợi thuộc Tài khoản 353 theo Thông tư 200/2014/TT-BTC và tiếp tục được quy định chi tiết tại Thông tư 99/2025/TT-BTC. Theo chuẩn quốc tế, chi phí thưởng cho nhân viên và ban điều hành phải được hạch toán trực tiếp vào chi phí hoạt động trên Báo cáo kết quả kinh doanh trước khi tính Lợi nhuận sau thuế (LNST). Ngược lại, tại Việt Nam, khoản tiền này được trích lập từ Lợi nhuận sau thuế chưa phân phối (Tài khoản 421) sang Tài khoản 353 thuộc nhóm Nợ phải trả, bao gồm bốn tiểu khoản: Quỹ khen thưởng (3531), Quỹ phúc lợi (3532), Quỹ phúc lợi đã hình thành TSCĐ (3533) và Quỹ thưởng ban quản lý điều hành (3534).   

Đây là phần lợi nhuận chảy ra khỏi túi cổ đông nhưng không đi qua báo cáo chi phí. Nếu thuật toán trên Antigravity lấy trực tiếp LNST chia cho số lượng cổ phiếu để tính EPS hoặc lấy Dòng tiền tự do (FCF) mà không trừ đi phần trích lập này, hệ thống sẽ thổi phồng giá trị nội tại của những doanh nghiệp có thói quen trích quỹ khen thưởng phúc lợi lớn hàng năm. Công thức chuẩn hóa EPS thực nhận của cổ đông trên hệ thống phải được lập trình như sau:   

𝐸
𝑃
𝑆
Thực (Adjusted)
=
𝐿
𝑁
𝑆
𝑇
Cổ đ
o
ˆ
ng c
o
ˆ
ng ty mẹ
−
Tr
ı
ˊ
ch Qu
y
˜
 Khen thưởng Ph
u
ˊ
c lợi (TK 353)
−
Cổ tức Cổ phi
e
ˆ
ˊ
u Ưu đ
a
˜
i
S
o
ˆ
ˊ
 lượng Cổ phi
e
ˆ
ˊ
u Lưu h
a
ˋ
nh B
ı
ˋ
nh qu
a
ˆ
n Pha lo
a
˜
ng
EPS
Thực (Adjusted)
	​

=
S
o
ˆ
ˊ
 lượng Cổ phi
e
ˆ
ˊ
u Lưu h
a
ˋ
nh B
ı
ˋ
nh qu
a
ˆ
n Pha lo
a
˜
ng
LNST
Cổ đ
o
ˆ
ng c
o
ˆ
ng ty mẹ
	​

−Tr
ı
ˊ
ch Qu
y
˜
	​

 Khen thưởng Ph
u
ˊ
c lợi (TK 353)−Cổ tức Cổ phi
e
ˆ
ˊ
u Ưu đ
a
˜
i
	​


Trong thực tế vận hành tại Việt Nam, dữ liệu minh họa cho thấy một công ty có LNST đạt 800 tỷ đồng với 200 triệu cổ phiếu lưu hành sẽ có EPS thô là 4.000 đồng/cổ phiếu; nhưng khi đại hội cổ đông quyết định trích 30 tỷ đồng vào quỹ khen thưởng phúc lợi, EPS thực nhận của cổ đông lập tức giảm xuống còn 3.850 đồng/cổ phiếu. Bên cạnh đó, thị trường Việt Nam thường xuyên chứng kiến làn sóng phát hành cổ phiếu thưởng cho nhân viên (ESOP), chào bán riêng lẻ và trái phiếu chuyển đổi trong các chu kỳ nới lỏng tiền tệ. Theo quy định tại VAS 30, thuật toán định giá dài hạn bắt buộc phải sử dụng EPS pha loãng (Diluted EPS) thay vì EPS cơ bản để phản ánh đúng rủi ro chia nhỏ miếng bánh lợi nhuận trong tương lai, ngăn chặn việc hệ thống tự động hạ thấp biên an toàn của danh mục.   

Thiết lập Tham số Chiết khấu Vĩ mô Việt Nam: Kết hợp CAPM (Damodaran) và MARR (Phil Town)

Trong định giá chiết khấu dòng tiền, tỷ suất chiết khấu đóng vai trò là lực hấp dẫn kéo giá trị tương lai về hiện tại. Phil Town sử dụng một mức Tỷ suất Sinh lời Tối thiểu Chấp nhận được (Minimum Acceptable Rate of Return - MARR) cố định ở mức 
15
%
/
n
a
˘
m
15%/n
a
˘
m cho mọi cổ phiếu nhằm đảm bảo quy tắc lãi kép nhân đôi tài sản sau mỗi 5 năm, hoặc nhân 4 lần sau 10 năm do 
(
1
+
0
,
15
)
10
≈
4
,
0456
(1+0,15)
10
≈4,0456. Tuy nhiên, đối với một công cụ định giá chuyên sâu tại thị trường mới nổi như Việt Nam, việc kết hợp cả ngưỡng tuyệt đối 
15
%
15% của Phil Town lẫn Chi phí Vốn Chủ sở hữu (
𝐾
𝑒
K
e
	​

) và Chi phí Vốn Bình quân Gia quyền (
𝑊
𝐴
𝐶
𝐶
WACC) theo mô hình CAPM của Giáo sư Aswath Damodaran sẽ mang lại độ chính xác vượt trội cho từng ngành nghề.   

Dữ liệu thị trường năm 2026 ghi nhận sự hạ nhiệt rõ rệt của mặt bằng rủi ro quốc gia toàn cầu nhưng sự phân hóa giữa các thị trường vẫn duy trì độ dốc lớn. Theo bản cập nhật tháng 7/2026 của Damodaran, phần bù rủi ro vốn cổ phần cơ sở của thị trường phát triển (Mature Market ERP) ở mức 
4
,
17
%
4,17% và của Hoa Kỳ là 
4
,
45
%
4,45%, trong khi chênh lệch vỡ nợ (default spreads) thu hẹp trên diện rộng trong quý 2/2026 khi nhóm xếp hạng A1 giảm từ 67,1 điểm cơ bản xuống 64,7 điểm cơ bản, Baa3 giảm từ 209,1 xuống 201,7 điểm cơ bản, và B3 giảm từ 618,5 xuống 596,4 điểm cơ bản. Đối với Việt Nam, phần bù rủi ro thị trường chứng khoán (ERP) năm 2026 đã giảm về biên độ 
7
,
0
%
−
8
,
0
%
7,0%−8,0% với mức trung vị chuẩn là 
7
,
5
%
7,5%, cải thiện đáng kể so với mức ERP 
9
,
57
%
9,57% và phần bù rủi ro quốc gia 
4
,
57
%
4,57% ở mức xếp hạng tín nhiệm Ba2 vào tháng 7/2023. Kết hợp với lợi suất Trái phiếu Chính phủ Việt Nam kỳ hạn 10 năm (
𝑅
𝑓
R
f
	​

) giao dịch quanh ngưỡng 
4
,
50
%
−
4
,
577
%
4,50%−4,577% (biên độ 52 tuần từ 
3
,
936
%
3,936% đến 
4
,
577
%
4,577%), công thức xác định Chi phí Vốn Chủ sở hữu (
𝐾
𝑒
K
e
	​

) và 
𝑊
𝐴
𝐶
𝐶
WACC trên Antigravity được chuẩn hóa như sau:   

𝐾
𝑒
=
𝑅
𝑓
+
𝛽
Bottom-up
×
𝐸
𝑅
𝑃
VN
=
4
,
5
%
+
𝛽
Bottom-up
×
7
,
5
%
K
e
	​

=R
f
	​

+β
Bottom-up
	​

×ERP
VN
	​

=4,5%+β
Bottom-up
	​

×7,5%
𝑊
𝐴
𝐶
𝐶
=
(
𝐸
𝐸
+
𝐷
×
𝐾
𝑒
)
+
(
𝐷
𝐸
+
𝐷
×
𝐾
𝑑
×
(
1
−
𝑡
)
)
WACC=(
E+D
E
	​

×K
e
	​

)+(
E+D
D
	​

×K
d
	​

×(1−t))

Trong phương trình trên, 
𝛽
Bottom-up
β
Bottom-up
	​

 được tính toán dựa trên rủi ro kinh doanh của ngành và cấu trúc nợ vay trên vốn chủ sở hữu (
𝐷
/
𝐸
D/E) của từng doanh nghiệp thay vì dùng Beta hồi quy lịch sử vốn dễ bị nhiễu bởi tính đầu cơ trên sàn chứng khoán Việt Nam. Đối với một doanh nghiệp có rủi ro trung bình thị trường (
𝛽
=
1
β=1), 
𝐾
𝑒
K
e
	​

 tại Việt Nam năm 2026 rơi vào khoảng 
12
,
0
%
−
12
,
08
%
12,0%−12,08%. Điều này giải thích tại sao việc Phil Town ấn định mức chiết khấu 
𝑀
𝐴
𝑅
𝑅
=
15
%
MARR=15% lại mang tính bảo thủ cực kỳ hiệu quả tại Việt Nam: mức 
15
%
15% cao hơn chi phí vốn cơ sở của thị trường khoảng 
3
%
3%, tự động tích hợp một lớp đệm rủi ro thanh khoản và quản trị trước cả khi áp dụng biên an toàn 50%.   

2. Tầng Lọc Sức khỏe Tài chính và Chống Bẫy Giá trị (Pre-Valuation Gatekeepers)

Cả Warren Buffett và Phil Town đều nhấn mạnh rằng công thức định giá chỉ có ý nghĩa khi được áp dụng cho một doanh nghiệp tuyệt vời (Wonderful Business). Nếu đưa dữ liệu của một doanh nghiệp đang suy thoái cấu trúc hoặc gian lận kế toán vào mô hình P/E hay DCF, thuật toán sẽ nhận diện cổ phiếu đó là rẻ và kích hoạt tín hiệu mua sai lầm — hiện tượng được gọi là Bẫy Giá trị (Value Trap). Do đó, trước khi chạy mô-đun tính giá cổ phiếu, hệ thống Antigravity phải thiết lập một phễu lọc định lượng ba tầng để chấm điểm chất lượng doanh nghiệp và điều chỉnh tự động tỷ lệ Biên An toàn (MOS).   

Tầng 1: Bộ lọc Big Five và Kỷ luật Nợ vay của Phil Town

Để lượng hóa khái niệm Con hào kinh tế (Moat) của Buffett, Phil Town yêu cầu doanh nghiệp phải đạt tốc độ tăng trưởng kép hàng năm (CAGR) tối thiểu 
10
%
/
n
a
˘
m
10%/n
a
˘
m trong suốt 10 năm — hoặc tối thiểu 5 năm liên tiếp đối với dữ liệu thị trường Việt Nam nơi nhiều công ty chưa có lịch sử dữ liệu 10 năm đồng nhất — trên cả năm chỉ số tài chính cốt lõi (Big Five Numbers). Chỉ số đầu tiên và quan trọng nhất là Tỷ suất Sinh lời trên Vốn Đầu tư (
𝑅
𝑂
𝐼
𝐶
ROIC), phản ánh hiệu quả phân bổ vốn của ban lãnh đạo và bắt buộc phải duy trì mức trung bình từ 
10
%
/
n
a
˘
m
10%/n
a
˘
m trở lên:   

𝑅
𝑂
𝐼
𝐶
=
𝐸
𝐵
𝐼
𝑇
×
(
1
−
Thu
e
ˆ
ˊ
 su
a
ˆ
ˊ
t TNDN thực t
e
ˆ
ˊ
)
V
o
ˆ
ˊ
n Chủ sở hữu
+
Nợ vay Ng
a
˘
ˊ
n hạn v
a
ˋ
 D
a
ˋ
i hạn
−
Ti
e
ˆ
ˋ
n v
a
ˋ
 Tương đương ti
e
ˆ
ˋ
n
ROIC=
V
o
ˆ
ˊ
n Chủ sở hữu+Nợ vay Ng
a
˘
ˊ
n hạn v
a
ˋ
 D
a
ˋ
i hạn−Ti
e
ˆ
ˋ
n v
a
ˋ
 Tương đương ti
e
ˆ
ˋ
n
EBIT×(1−Thu
e
ˆ
ˊ
 su
a
ˆ
ˊ
t TNDN thực t
e
ˆ
ˊ
)
	​


Bốn chỉ số tăng trưởng kép còn lại trong bộ Big Five bao gồm tốc độ tăng trưởng Vốn Chủ sở hữu hay Giá trị sổ sách trên mỗi cổ phiếu (Equity / BVPS Growth) phản ánh khả năng tích lũy thặng dư thực chất, tốc độ tăng trưởng EPS pha loãng đã điều chỉnh (Adjusted Diluted EPS Growth), tốc độ tăng trưởng Doanh thu thuần (Sales Growth), và tốc độ tăng trưởng Dòng tiền Tự do (Free Cash Flow Growth); tất cả đều phải đạt ngưỡng 
𝐶
𝐴
𝐺
𝑅
≥
10
%
/
n
a
˘
m
CAGR≥10%/n
a
˘
m. Song song với Big Five, tiêu chí Quản trị Nợ vay (Manageable Debt) đòi hỏi tổng Nợ vay dài hạn (Mã số 338 trên Bảng cân đối kế toán) phải được thanh toán hết trong vòng tối đa 3 năm bằng Dòng tiền tự do hiện tại, tương đương điều kiện 
Long-term Debt
/
𝐹
𝐶
𝐹
≤
3
Long-term Debt/FCF≤3 để đảm bảo doanh nghiệp không bị tổn thương khi chu kỳ tín dụng thắt chặt.   

Tầng 2: Thuật toán Piotroski F-Score (9 Tiêu chí Nhị phân trên BCTC VAS)

Nghiên cứu thực nghiệm chuyên sâu trên mẫu 501 doanh nghiệp niêm yết tại thị trường chứng khoán Việt Nam đã chứng minh rằng việc sử dụng bảng điểm Piotroski F-Score để phân tách doanh nghiệp khỏe mạnh (Winners) và yếu kém (Losers) mang lại tỷ suất sinh lời điều chỉnh theo rủi ro thị trường vượt trội hơn 
30
%
/
n
a
˘
m
30%/n
a
˘
m — một con số có ý nghĩa thống kê rất cao không chỉ ở nhóm cổ phiếu giá trị (P/B thấp) mà cả ở nhóm cổ phiếu tăng trưởng (P/B cao). Trước đó, kiểm nghiệm lịch sử (backtest) gốc của Giáo sư Joseph D. Piotroski trong giai đoạn 20 năm cũng ghi nhận mức gia tăng lợi nhuận bình quân 
+
23
%
/
n
a
˘
m
+23%/n
a
˘
m.   

Trên Antigravity, thuật toán F-Score được lập trình thành hàm tổng của 9 biến nhị phân (nhận giá trị 
1
1 nếu thỏa mãn điều kiện và 
0
0 nếu không thỏa mãn), chia làm ba trụ cột đánh giá khả năng sinh lời, cơ cấu nguồn vốn và hiệu quả hoạt động:   

Nhóm Tiêu chí	Mã Biến	Công thức Toán học và Điều kiện Logic (So sánh Năm 
𝑡
t và Năm 
𝑡
−
1
t−1)	Ý nghĩa Kiểm định Chất lượng BCTC tại Việt Nam
1. Khả năng Sinh lời (4 Điểm)	
𝐹
𝑅
𝑂
𝐴
F
ROA
	​

	
N
e
ˆ
ˊ
u 
𝑅
𝑂
𝐴
𝑡
=
𝐿
𝑁
𝑆
𝑇
Thực
,
𝑡
Tổng T
a
ˋ
i sản
𝑡
>
0
⇒
+
1
 điểm
N
e
ˆ
ˊ
u ROA
t
	​

=
Tổng T
a
ˋ
i sản
t
	​

LNST
Thực,t
	​

	​

>0⇒+1 điểm	

Doanh nghiệp kinh doanh có lãi thực tế sau khi trừ Quỹ KTPL.


	
𝐹
𝐶
𝐹
𝑂
F
CFO
	​

	
N
e
ˆ
ˊ
u 
𝐶
𝐹
𝑂
𝑡
 (Lưu chuyển ti
e
ˆ
ˋ
n thu
a
ˆ
ˋ
n từ HĐKD)
>
0
⇒
+
1
 điểm
N
e
ˆ
ˊ
u CFO
t
	​

 (Lưu chuyển ti
e
ˆ
ˋ
n thu
a
ˆ
ˋ
n từ HĐKD)>0⇒+1 điểm	

Hoạt động cốt lõi tạo ra tiền mặt dương, không phải lợi nhuận trên giấy.


	
𝐹
Δ
𝑅
𝑂
𝐴
F
ΔROA
	​

	
N
e
ˆ
ˊ
u 
𝑅
𝑂
𝐴
𝑡
>
𝑅
𝑂
𝐴
𝑡
−
1
⇒
+
1
 điểm
N
e
ˆ
ˊ
u ROA
t
	​

>ROA
t−1
	​

⇒+1 điểm	

Hiệu suất sinh lời trên tài sản đang trong xu hướng cải thiện.


	
𝐹
Accrual
F
Accrual
	​

	
N
e
ˆ
ˊ
u 
𝐶
𝐹
𝑂
𝑡
>
𝐿
𝑁
𝑆
𝑇
Thực
,
𝑡
⇒
+
1
 điểm
N
e
ˆ
ˊ
u CFO
t
	​

>LNST
Thực,t
	​

⇒+1 điểm	

Chặn đứng thủ thuật kế toán ghi nhận doanh thu ảo qua khoản phải thu.


2. Đòn bẩy & Thanh khoản (3 Điểm)	
𝐹
Δ
Lever
F
ΔLever
	​

	
N
e
ˆ
ˊ
u 
(
Nợ D
a
ˋ
i hạn
Tổng T
a
ˋ
i sản
)
𝑡
<
(
Nợ D
a
ˋ
i hạn
Tổng T
a
ˋ
i sản
)
𝑡
−
1
⇒
+
1
 điểm
N
e
ˆ
ˊ
u (
Tổng T
a
ˋ
i sản
Nợ D
a
ˋ
i hạn
	​

)
t
	​

<(
Tổng T
a
ˋ
i sản
Nợ D
a
ˋ
i hạn
	​

)
t−1
	​

⇒+1 điểm	

Giảm sự phụ thuộc vào đòn bẩy nợ vay dài hạn (Mã 338 / Mã 270).


	
𝐹
Δ
Liquid
F
ΔLiquid
	​

	
N
e
ˆ
ˊ
u 
Current Ratio
𝑡
=
(
TS Ng
a
˘
ˊ
n hạn
Nợ Ng
a
˘
ˊ
n hạn
)
𝑡
>
Current Ratio
𝑡
−
1
⇒
+
1
 điểm
N
e
ˆ
ˊ
u Current Ratio
t
	​

=(
Nợ Ng
a
˘
ˊ
n hạn
TS Ng
a
˘
ˊ
n hạn
	​

)
t
	​

>Current Ratio
t−1
	​

⇒+1 điểm	

Năng lực thanh toán nợ ngắn hạn (Mã 100 / Mã 310) được cải thiện.


	
𝐹
EqOffer
F
EqOffer
	​

	
N
e
ˆ
ˊ
u 
S
o
ˆ
ˊ
 lượng CP Lưu h
a
ˋ
nh
𝑡
≤
S
o
ˆ
ˊ
 lượng CP Lưu h
a
ˋ
nh
𝑡
−
1
 (trừ chia t
a
ˊ
ch/thưởng)
⇒
+
1
 điểm
N
e
ˆ
ˊ
u S
o
ˆ
ˊ
 lượng CP Lưu h
a
ˋ
nh
t
	​

≤S
o
ˆ
ˊ
 lượng CP Lưu h
a
ˋ
nh
t−1
	​

 (trừ chia t
a
ˊ
ch/thưởng)⇒+1 điểm	

Doanh nghiệp tự chủ vốn, không pha loãng cổ đông qua phát hành thêm/ESOP.


3. Hiệu quả Hoạt động (2 Điểm)	
𝐹
Δ
Margin
F
ΔMargin
	​

	
N
e
ˆ
ˊ
u 
Bi
e
ˆ
n Lợi nhuận Gộp
𝑡
>
Bi
e
ˆ
n Lợi nhuận Gộp
𝑡
−
1
⇒
+
1
 điểm
N
e
ˆ
ˊ
u Bi
e
ˆ
n Lợi nhuận Gộp
t
	​

>Bi
e
ˆ
n Lợi nhuận Gộp
t−1
	​

⇒+1 điểm	

Sức mạnh định giá bán (Pricing Power / Moat) tăng lên hoặc giá vốn giảm.


	
𝐹
Δ
Turn
F
ΔTurn
	​

	
N
e
ˆ
ˊ
u 
(
Doanh thu Thu
a
ˆ
ˋ
n
Tổng T
a
ˋ
i sản B
ı
ˋ
nh qu
a
ˆ
n
)
𝑡
>
(
Doanh thu Thu
a
ˆ
ˋ
n
Tổng T
a
ˋ
i sản B
ı
ˋ
nh qu
a
ˆ
n
)
𝑡
−
1
⇒
+
1
 điểm
N
e
ˆ
ˊ
u (
Tổng T
a
ˋ
i sản B
ı
ˋ
nh qu
a
ˆ
n
Doanh thu Thu
a
ˆ
ˋ
n
	​

)
t
	​

>(
Tổng T
a
ˋ
i sản B
ı
ˋ
nh qu
a
ˆ
n
Doanh thu Thu
a
ˆ
ˋ
n
	​

)
t−1
	​

⇒+1 điểm	

Vòng quay tài sản tăng, giải phóng hàng tồn kho và công nợ nhanh hơn.

  

Tổng điểm 
𝐹
-Score
=
∑
𝑖
=
1
9
𝐹
𝑖
F-Score=∑
i=1
9
	​

F
i
	​

 đạt từ 7 đến 9 điểm xác nhận doanh nghiệp có nền tảng tài chính lành mạnh vượt trội; đạt từ 4 đến 6 điểm phản ánh trạng thái tài chính trung bình ổn định; và từ 0 đến 3 điểm là tín hiệu cảnh báo suy thoái nghiêm trọng, như trường hợp thực tế của cổ phiếu QNS năm 2017 khi F-Score tụt xuống 3 điểm trước khi thị giá sụt giảm mạnh từ Quý 2/2017.   

Tầng 3: Mô hình Cảnh báo Phá sản Altman Z-Score Đa Biến thể (Z, Z', và Z'' Thị trường Mới nổi)

Một sai lầm kỹ thuật thường gặp ở các trang tài chính Việt Nam là áp dụng duy nhất công thức Altman Z-Score nguyên bản năm 1968 cho mọi doanh nghiệp. Trong thực tế, Edward Altman đã thiết kế ba phương trình riêng biệt tùy thuộc vào đặc thù ngành nghề và cấu trúc thị trường. Đặc biệt, đối với các doanh nghiệp phi sản xuất (thương mại, dịch vụ, công nghệ, bất động sản) và các doanh nghiệp hoạt động tại Thị trường Mới nổi (Emerging Markets), biến số vòng quay tài sản (
𝑋
5
=
Sales
/
Total Assets
X
5
	​

=Sales/Total Assets) bị loại bỏ hoàn toàn để tránh sự méo mó giữa các ngành, đồng thời phương trình được cộng thêm hằng số chuẩn hóa 
3
,
25
3,25 nhằm tương đương hóa điểm 0 với trái phiếu vỡ nợ hạng D (Default).   

Để lập trình mô-đun này vào Antigravity, hệ thống cần trích xuất năm tỷ số tài chính nền tảng, trong đó mẫu số Tổng Tài sản (
𝑇
𝐴
TA) khuyến nghị loại trừ Tài sản cố định vô hình (Mã 227) để đảm bảo tính bảo thủ. Biến số thứ nhất 
𝑋
1
=
(
T
a
ˋ
i sản Ng
a
˘
ˊ
n hạn M
a
˜
 100
−
Nợ Ng
a
˘
ˊ
n hạn M
a
˜
 310
)
/
𝑇
𝐴
X
1
	​

=(T
a
ˋ
i sản Ng
a
˘
ˊ
n hạn M
a
˜
 100−Nợ Ng
a
˘
ˊ
n hạn M
a
˜
 310)/TA đo lường thanh khoản ròng ngắn hạn; biến số thứ hai 
𝑋
2
=
(
LNST Chưa Ph
a
ˆ
n ph
o
ˆ
ˊ
i M
a
˜
 421
+
Qu
y
˜
 Đ
a
ˆ
ˋ
u tư Ph
a
ˊ
t triển M
a
˜
 418
)
/
𝑇
𝐴
X
2
	​

=(LNST Chưa Ph
a
ˆ
n ph
o
ˆ
ˊ
i M
a
˜
 421+Qu
y
˜
	​

 Đ
a
ˆ
ˋ
u tư Ph
a
ˊ
t triển M
a
˜
 418)/TA đo lường khả năng tích lũy lợi nhuận giữ lại qua thời gian so với nợ vay; và biến số thứ ba 
𝑋
3
=
𝐸
𝐵
𝐼
𝑇
/
𝑇
𝐴
X
3
	​

=EBIT/TA đo lường hiệu suất sinh lời thuần túy của tài sản trước ảnh hưởng của thuế và đòn bẩy tài chính. Biến số thứ tư có hai dạng: 
𝑋
4
𝑀
=
V
o
ˆ
ˊ
n h
o
ˊ
a Thị trường
/
Tổng Nợ Phải trả (M
a
˜
 300)
X
4M
	​

=V
o
ˆ
ˊ
n h
o
ˊ
a Thị trường/Tổng Nợ Phải trả (M
a
˜
 300) áp dụng cho mô hình Z sản xuất niêm yết, hoặc 
𝑋
4
𝐵
=
Gi
a
ˊ
 trị Sổ s
a
ˊ
ch V
o
ˆ
ˊ
n Chủ sở hữu (M
a
˜
 400)
/
Tổng Nợ Phải trả (M
a
˜
 300)
X
4B
	​

=Gi
a
ˊ
 trị Sổ s
a
ˊ
ch V
o
ˆ
ˊ
n Chủ sở hữu (M
a
˜
 400)/Tổng Nợ Phải trả (M
a
˜
 300) áp dụng cho mô hình 
𝑍
′
Z
′
 và 
𝑍
′
′
Z
′′
 nhằm loại bỏ nhiễu biến động giá cổ phiếu đầu cơ. Cuối cùng, biến số thứ năm 
𝑋
5
=
Doanh thu Thu
a
ˆ
ˋ
n
/
𝑇
𝐴
X
5
	​

=Doanh thu Thu
a
ˆ
ˋ
n/TA đo lường vòng quay tài sản và chỉ được sử dụng cho các doanh nghiệp sản xuất. Cấu trúc phân nhánh phương trình và ngưỡng cảnh báo phá sản theo ngành trên Antigravity được chuẩn hóa trong bảng dưới đây:   

Mô hình Altman	Nhóm Ngành Áp dụng tại Việt Nam	Phương trình Toán học Chuẩn hóa	Ngưỡng An toàn (Safe Zone)	Vùng Xám (Grey Zone)	Vùng Nguy hiểm (Distress)
Altman 
𝑍
Z (1968)	

Sản xuất công nghiệp niêm yết (Thép, Xi măng, Hóa chất, Ô tô, Chế biến).

	

𝑍
=
1
,
2
𝑋
1
+
1
,
4
𝑋
2
+
3
,
3
𝑋
3
+
0
,
6
𝑋
4
𝑀
+
1
,
0
𝑋
5
Z=1,2X
1
	​

+1,4X
2
	​

+3,3X
3
	​

+0,6X
4M
	​

+1,0X
5
	​


	

𝑍
>
2
,
99
Z>2,99

	

1
,
81
≤
𝑍
≤
2
,
99
1,81≤Z≤2,99

	

𝑍
<
1
,
81
Z<1,81


Altman 
𝑍
′
Z
′
 (Prime)	

Doanh nghiệp sản xuất chưa niêm yết, SME IPO hoặc thanh khoản rất thấp trên UPCoM.

	

𝑍
′
=
0
,
717
𝑋
1
+
0
,
847
𝑋
2
+
3
,
107
𝑋
3
+
0
,
420
𝑋
4
𝐵
+
0
,
998
𝑋
5
Z
′
=0,717X
1
	​

+0,847X
2
	​

+3,107X
3
	​

+0,420X
4B
	​

+0,998X
5
	​


	

𝑍
′
>
2
,
90
Z
′
>2,90

	

1
,
23
≤
𝑍
′
≤
2
,
90
1,23≤Z
′
≤2,90

	

𝑍
′
<
1
,
23
Z
′
<1,23


Altman 
𝑍
EM
′
′
Z
EM
′′
	​

 (Emerging Markets)	

Phi sản xuất, Bán lẻ, FMCG, Công nghệ (IT), Y tế, Dịch vụ, BĐS tại Thị trường Mới nổi.

	

𝑍
EM
′
′
=
3
,
25
+
6
,
56
𝑋
1
+
3
,
26
𝑋
2
+
6
,
72
𝑋
3
+
1
,
05
𝑋
4
𝐵
Z
EM
′′
	​

=3,25+6,56X
1
	​

+3,26X
2
	​

+6,72X
3
	​

+1,05X
4B
	​


	

𝑍
EM
′
′
>
2
,
60
Z
EM
′′
	​

>2,60

	

1
,
10
≤
𝑍
EM
′
′
≤
2
,
60
1,10≤Z
EM
′′
	​

≤2,60

	

𝑍
EM
′
′
<
1
,
10
Z
EM
′′
	​

<1,10

  

Hệ thống cần thiết lập điều kiện ngoại lệ (Exception Rule): tuyệt đối không chạy Altman Z-Score cho nhóm Ngân hàng, Chứng khoán và Bảo hiểm vì đặc thù đòn bẩy nợ của định chế tài chính hoàn toàn khác với doanh nghiệp phi tài chính.   

3. Hệ thống Công thức Định giá Lõi của Warren Buffett và Phil Town

Khi một cổ phiếu vượt qua các bộ lọc sức khỏe tài chính hoặc được gắn nhãn rủi ro tương ứng, hệ thống Antigravity sẽ kích hoạt bộ tứ công thức định giá hội tụ của Phil Town và Warren Buffett.   

Công thức 1: Giá Hợp lý (Sticker Price) và Giá Mua Biên An toàn (MOS Price)

Phương pháp Sticker Price của Phil Town hoạt động theo cơ chế tính ngược từ giá bán kỳ vọng ở năm thứ 10 về thời điểm hiện tại. Để tránh sự lạc quan thái quá khi phóng chiếu tương lai, thuật toán bắt buộc áp dụng nguyên tắc lấy giá trị thấp hơn (Conservative Minimum Rule) ở cả hai biến số tốc độ tăng trưởng và hệ số P/E. Trước hết, hệ thống xác định tốc độ tăng trưởng bảo thủ (
𝑔
Rule1
g
Rule1
	​

) bằng cách lấy giá trị nhỏ nhất giữa tốc độ tăng trưởng vốn chủ sở hữu lịch sử (
𝐶
𝐴
𝐺
𝑅
BVPS
CAGR
BVPS
	​

) và tốc độ tăng trưởng EPS dự phóng của giới phân tích, đồng thời chặn trần theo ngành:   

𝑔
Rule1
=
min
⁡
(
𝐶
𝐴
𝐺
𝑅
BVPS (Lịch sử 5-10 n
a
˘
m)
,
𝑔
EPS Dự ph
o
ˊ
ng (Analysts)
,
𝑔
Tr
a
ˆ
ˋ
n Ng
a
ˋ
nh
)
g
Rule1
	​

=min(CAGR
BVPS (Lịch sử 5-10 n
a
˘
m)
	​

,g
EPS Dự ph
o
ˊ
ng (Analysts)
	​

,g
Tr
a
ˆ
ˋ
n Ng
a
ˋ
nh
	​

)

Trong kiểm nghiệm mẫu của Phil Town, ngay cả khi tốc độ tăng trưởng vốn chủ sở hữu lịch sử lên tới 
110
,
1
%
/
n
a
˘
m
110,1%/n
a
˘
m nhưng giới phân tích dự báo tăng trưởng EPS tương lai là 
20
,
0
%
/
n
a
˘
m
20,0%/n
a
˘
m, thuật toán sẽ chọn mức thấp hơn là 
20
,
0
%
20,0%. Tại thị trường Việt Nam, để ngăn chặn sai số hàm mũ trong 10 năm, hệ thống Antigravity cần đặt thêm một ngưỡng trần cứng (
𝑔
Tr
a
ˆ
ˋ
n Ng
a
ˋ
nh
≤
25
%
/
n
a
˘
m
g
Tr
a
ˆ
ˋ
n Ng
a
ˋ
nh
	​

≤25%/n
a
˘
m). Tiếp theo, thuật toán phóng chiếu EPS thực nhận vào năm thứ 10 và xác định hệ số P/E tương lai bảo thủ (
𝑃
𝐸
Future
PE
Future
	​

) dựa trên quy tắc P/E mặc định tối đa bằng hai lần tốc độ tăng trưởng (
2
×
𝑔
Rule1
×
100
2×g
Rule1
	​

×100) so sánh với P/E trung bình lịch sử 5 năm của cổ phiếu:   

𝐸
𝑃
𝑆
10
=
𝐸
𝑃
𝑆
Thực (TTM)
×
(
1
+
𝑔
Rule1
)
10
EPS
10
	​

=EPS
Thực (TTM)
	​

×(1+g
Rule1
	​

)
10
𝑃
𝐸
Future
=
min
⁡
(
2
×
(
𝑔
Rule1
×
100
)
,
𝑃
𝐸
Trung b
ı
ˋ
nh Lịch sử 5 n
a
˘
m
,
𝑃
𝐸
Tr
a
ˆ
ˋ
n Thị trường VN
)
PE
Future
	​

=min(2×(g
Rule1
	​

×100),PE
Trung b
ı
ˋ
nh Lịch sử 5 n
a
˘
m
	​

,PE
Tr
a
ˆ
ˋ
n Thị trường VN
	​

)

Sau khi có 
𝐸
𝑃
𝑆
10
EPS
10
	​

 và 
𝑃
𝐸
Future
PE
Future
	​

 (với 
𝑃
𝐸
Tr
a
ˆ
ˋ
n Thị trường VN
PE
Tr
a
ˆ
ˋ
n Thị trường VN
	​

 khuyến nghị giới hạn ở mức 
25
x
−
30
x
25x−30x do mặt bằng lãi suất nội tệ), hệ thống tính Giá Thị trường Tương lai ở năm thứ 10 (
𝑃
10
P
10
	​

), chiết khấu về hiện tại theo mức 
𝑀
𝐴
𝑅
𝑅
=
15
%
/
n
a
˘
m
MARR=15%/n
a
˘
m để thu được Giá Hợp lý (
𝑃
Sticker
P
Sticker
	​

), và chia đôi để xác lập Giá Mua An toàn (
𝑃
MOS
P
MOS
	​

):   

𝑃
10
=
𝐸
𝑃
𝑆
10
×
𝑃
𝐸
Future
P
10
	​

=EPS
10
	​

×PE
Future
	​

𝑃
Sticker
=
𝑃
10
(
1
+
𝑀
𝐴
𝑅
𝑅
)
10
=
𝑃
10
(
1
+
0
,
15
)
10
≈
𝑃
10
4
,
0456
P
Sticker
	​

=
(1+MARR)
10
P
10
	​

	​

=
(1+0,15)
10
P
10
	​

	​

≈
4,0456
P
10
	​

	​

𝑃
MOS
=
𝑃
Sticker
×
(
1
−
𝑀
𝑂
𝑆
)
=
𝑃
Sticker
×
50
%
P
MOS
	​

=P
Sticker
	​

×(1−MOS)=P
Sticker
	​

×50%

Với bộ tham số kiểm thử chuẩn (
𝐸
𝑃
𝑆
0
=
1
,
03
 USD
EPS
0
	​

=1,03 USD, 
𝑔
=
20
%
g=20%, 
𝑃
𝐸
Lịch sử
=
101
PE
Lịch sử
	​

=101), thuật toán cho ra 
𝐸
𝑃
𝑆
10
=
1
,
03
×
(
1
,
20
)
10
=
6
,
38
 USD
EPS
10
	​

=1,03×(1,20)
10
=6,38 USD; hệ số 
𝑃
𝐸
Future
=
min
⁡
(
40
,
101
)
=
40
PE
Future
	​

=min(40,101)=40; giá tương lai 
𝑃
10
=
6
,
38
×
40
=
255
,
20
 USD
P
10
	​

=6,38×40=255,20 USD; suy ra 
𝑃
Sticker
=
255
,
20
/
(
1
,
15
)
10
=
63
,
08
 USD
P
Sticker
	​

=255,20/(1,15)
10
=63,08 USD và 
𝑃
MOS
=
31
,
54
 USD
P
MOS
	​

=31,54 USD. Phân tích toán học sâu hơn cho thấy việc kết hợp chiết khấu 
15
%
/
n
a
˘
m
15%/n
a
˘
m và biên an toàn 
50
%
50% tạo ra một màng lọc cực kỳ khắt khe: nếu quy đổi về mô hình DCF hai giai đoạn, một công ty tăng trưởng 
0
%
0% chỉ xứng đáng được mua ở mức 
𝑃
/
𝐸
=
3
,
33
x
P/E=3,33x; tăng trưởng 
10
%
/
n
a
˘
m
10%/n
a
˘
m trong 5 năm rồi 
2
%
2% vĩnh viễn tương ứng 
𝑃
/
𝐸
=
5
,
33
x
P/E=5,33x; tăng trưởng 
22
%
/
n
a
˘
m
22%/n
a
˘
m trong 5 năm rồi 
5
%
5% vĩnh viễn tương ứng 
𝑃
/
𝐸
=
10
,
0
x
P/E=10,0x; và chỉ những siêu cổ phiếu tăng trưởng 
25
%
/
n
a
˘
m
25%/n
a
˘
m suốt 10 năm rồi 
5
%
5% vĩnh viễn mới có giá mua MOS ở mức 
𝑃
/
𝐸
=
20
,
0
x
P/E=20,0x.   

Công thức 2: Dòng tiền Chủ sở hữu (Owner Earnings) và Giá 10 Cap (10 Cap Price)

Phương pháp 10 Cap xuất phát từ tư duy đầu tư bất động sản cho thuê của Warren Buffett và Phil Town: nếu mua đứt toàn bộ doanh nghiệp và không tính đến yếu tố tăng trưởng, dòng tiền ròng chảy về túi chủ sở hữu mỗi năm phải đạt tối thiểu 
10
%
10% trên tổng vốn bỏ ra, tương đương hoàn vốn trong 10 năm ở trạng thái tĩnh. Thay vì dùng lợi nhuận kế toán, Buffett định nghĩa Dòng tiền Chủ sở hữu (Owner Earnings) là lượng tiền mặt thực sự có thể rút ra khỏi doanh nghiệp mà không làm suy giảm năng lực cạnh tranh hay sản lượng hiện tại.   

Tại Việt Nam, nhiều doanh nghiệp đang trong giai đoạn mở rộng nhà máy (như HPG đầu tư khu liên hợp Dung Quất) sẽ có tổng chi phí đầu tư tài sản cố định (Total CapEx) rất lớn, khiến Free Cash Flow truyền thống bị âm. Do đó, thuật toán trên Antigravity cần tách biệt CapEx Bảo trì (Maintenance CapEx) khỏi CapEx Mở rộng (Growth CapEx) và trừ đi khoản trích Quỹ khen thưởng phúc lợi:   

Owner Earnings
=
𝐶
𝐹
𝑂
−
CapEx
Bảo tr
ı
ˋ
−
Tr
ı
ˊ
ch Qu
y
˜
 KTPL (TK 353)
Owner Earnings=CFO−CapEx
Bảo tr
ı
ˋ
	​

−Tr
ı
ˊ
ch Qu
y
˜
	​

 KTPL (TK 353)

Nếu doanh nghiệp không thuyết minh chi tiết 
CapEx
Bảo tr
ı
ˋ
CapEx
Bảo tr
ı
ˋ
	​

, thuật toán có thể ước lượng biến này thông qua công thức bảo thủ 
CapEx
Bảo tr
ı
ˋ
≈
min
⁡
(
Tổng CapEx
,
Chi ph
ı
ˊ
 Kh
a
ˆ
ˊ
u hao TSCĐ trong k
y
ˋ
)
CapEx
Bảo tr
ı
ˋ
	​

≈min(Tổng CapEx,Chi ph
ı
ˊ
 Kh
a
ˆ
ˊ
u hao TSCĐ trong k
y
ˋ
	​

). Khi đó, công thức định giá 10 Cap trên mỗi cổ phiếu được xác định bằng cách chia Owner Earnings trên mỗi cổ phiếu cho tỷ suất yêu cầu 
10
%
10%:   

𝑃
10Cap
=
Owner Earnings tr
e
ˆ
n m
o
ˆ
˜
i Cổ phi
e
ˆ
ˊ
u
10
%
=
10
×
(
Owner Earnings
S
o
ˆ
ˊ
 CP Pha lo
a
˜
ng
)
P
10Cap
	​

=
10%
Owner Earnings tr
e
ˆ
n m
o
ˆ
˜
i Cổ phi
e
ˆ
ˊ
u
	​

=10×(
S
o
ˆ
ˊ
 CP Pha lo
a
˜
ng
Owner Earnings
	​

)

Ví dụ thực tế từ Phil Town cho thấy một cổ phiếu tạo ra 
8
 USD
8 USD (hoặc 
8.000
 VNĐ
8.000 VNĐ) Owner Earnings trên mỗi cổ phiếu sẽ có giá mua 10 Cap chính xác là 
8
/
10
%
=
80
 USD
8/10%=80 USD (hoặc 
80.000
 VNĐ
80.000 VNĐ).   

Công thức 3: Thời gian Hoàn vốn (Payback Time Price)

Trong khi 10 Cap bỏ qua yếu tố tăng trưởng, phương pháp Payback Time trả lời câu hỏi của quỹ đầu tư tư nhân (Private Equity): nếu mua toàn bộ doanh nghiệp ở mức giá hiện tại và cộng dồn dòng tiền tự do tăng trưởng hàng năm, mất bao nhiêu năm để nhà đầu tư thu hồi đủ 
100
%
100% vốn gốc. Trên thị trường niêm yết đại chúng, nhà đầu tư thường chấp nhận trả mức giá tương đương 16 năm dòng tiền tự do; do đó, để tích hợp biên an toàn 
50
%
50%, Phil Town đặt ngưỡng trần mua tối đa là 8 năm (
𝑁
Max
=
8
N
Max
	​

=8).   

Theo định nghĩa của Rule #1, dòng tiền tự do được phóng chiếu tăng trưởng kép trong 8 năm tiếp theo để xác định tổng giá trị thu hồi vốn. Thay vì dùng vòng lặp tốn tài nguyên tính toán, lập trình viên có thể nhúng trực tiếp công thức tổng cấp số nhân đóng (Closed-Form Geometric Series) vào Antigravity để tính chính xác Giá Mua Payback Time Tối đa (
𝑃
Payback
P
Payback
	​

) tại ngưỡng 
𝑁
=
8
N=8 năm:   

𝑃
Payback (8 n
a
˘
m)
=
∑
𝑛
=
1
8
𝐹
𝐶
𝐹
Thực
,
0
×
(
1
+
𝑔
Rule1
)
𝑛
=
𝐹
𝐶
𝐹
Thực
,
0
×
(
1
+
𝑔
Rule1
)
×
[
(
1
+
𝑔
Rule1
)
8
−
1
𝑔
Rule1
]
P
Payback (8 n
a
˘
m)
	​

=
n=1
∑
8
	​

FCF
Thực,0
	​

×(1+g
Rule1
	​

)
n
=FCF
Thực,0
	​

×(1+g
Rule1
	​

)×[
g
Rule1
	​

(1+g
Rule1
	​

)
8
−1
	​

]

Ngược lại, để tính Số năm Hoàn vốn Thực tế (
𝑁
Payback
N
Payback
	​

) tại mức thị giá hiện tại (
𝑃
Market
P
Market
	​

) nhằm hiển thị lên giao diện người dùng, công thức logarit nghịch đảo là:   

𝑁
Payback
=
ln
⁡
(
1
+
𝑃
Market
×
𝑔
Rule1
𝐹
𝐶
𝐹
Thực
,
0
×
(
1
+
𝑔
Rule1
)
)
ln
⁡
(
1
+
𝑔
Rule1
)
N
Payback
	​

=
ln(1+g
Rule1
	​

)
ln(1+
FCF
Thực,0
	​

×(1+g
Rule1
	​

)
P
Market
	​

×g
Rule1
	​

	​

)
	​


Chẳng hạn, với một công ty có 
𝐹
𝐶
𝐹
0
=
5
 USD
FCF
0
	​

=5 USD, tốc độ tăng trưởng 
𝑔
=
10
%
/
n
a
˘
m
g=10%/n
a
˘
m và đang giao dịch ở mức giá 
𝑃
Market
=
40
 USD
P
Market
	​

=40 USD, tổng dòng tiền thu hồi sẽ khớp hoàn toàn với vốn đầu tư ban đầu sau 6 năm — nằm trọn trong vùng mua lý tưởng (dưới 8 năm) của Rule #1.   

Công thức 4: DCF Hai Giai đoạn của Buffett và Giá trị Xác sống (Zombie Value)

Để hoàn thiện góc nhìn Giá trị Nội tại của Warren Buffett và kiểm chứng chéo với kịch bản xấu nhất của Phil Town, hệ thống cần tính toán đồng thời Giá trị Xác sống (Zombie Value) và Giá trị Nội tại DCF Hai Giai đoạn. Giá trị Xác sống định giá doanh nghiệp trong kịch bản bi quan nhất khi tốc độ tăng trưởng ngừng lại hoàn toàn (
𝑔
=
0
%
g=0%) mãi mãi (tương đương mô hình Tăng trưởng Gordon với tăng trưởng bằng không), cộng với lượng tiền mặt ròng hiện có trên mỗi cổ phiếu:   

𝑃
Zombie
=
Owner Earnings tr
e
ˆ
n m
o
ˆ
˜
i CP
𝐾
𝑒
+
Ti
e
ˆ
ˋ
n mặt R
o
ˋ
ng tr
e
ˆ
n m
o
ˆ
˜
i CP
P
Zombie
	​

=
K
e
	​

Owner Earnings tr
e
ˆ
n m
o
ˆ
˜
i CP
	​

+Ti
e
ˆ
ˋ
n mặt R
o
ˋ
ng tr
e
ˆ
n m
o
ˆ
˜
i CP

Song song đó, mô hình Chiết khấu Dòng tiền Hai Giai đoạn (2-Stage Intrinsic DCF) phóng chiếu dòng tiền tăng trưởng ở tốc độ 
𝑔
Rule1
g
Rule1
	​

 trong 10 năm đầu và tăng trưởng ổn định ở mức 
𝑔
Terminal
=
3
%
−
4
%
g
Terminal
	​

=3%−4% (tương đương lạm phát mục tiêu dài hạn) từ năm thứ 11 trở đi, sau đó chiết khấu về hiện tại theo chi phí vốn 
𝐾
𝑒
K
e
	​

 (hoặc 
𝑊
𝐴
𝐶
𝐶
WACC):   

𝐼
𝑉
DCF
=
∑
𝑡
=
1
10
𝐹
𝐶
𝐹
0
×
(
1
+
𝑔
Rule1
)
𝑡
(
1
+
𝐾
𝑒
)
𝑡
+
𝐹
𝐶
𝐹
10
×
(
1
+
𝑔
Terminal
)
(
𝐾
𝑒
−
𝑔
Terminal
)
×
(
1
+
𝐾
𝑒
)
10
IV
DCF
	​

=
t=1
∑
10
	​

(1+K
e
	​

)
t
FCF
0
	​

×(1+g
Rule1
	​

)
t
	​

+
(K
e
	​

−g
Terminal
	​

)×(1+K
e
	​

)
10
FCF
10
	​

×(1+g
Terminal
	​

)
	​

4. Ma trận Phân hóa Công thức Định giá theo Đặc thù Ngành tại Việt Nam

Một công cụ định giá thông minh trên Antigravity phải hoạt động theo cơ chế định tuyến tự động (Sector Routing Engine): ngay khi người dùng nhập mã cổ phiếu, hệ thống truy xuất mã ngành ICB (Industry Classification Benchmark) và kích hoạt bộ công thức cũng như trọng số riêng biệt cho ngành đó.   

Phân nhóm Ngành (ICB)	Cổ phiếu Đại diện (VN)	Tại sao Công thức Chung Thất bại?	Bộ Công thức Định giá Chuẩn hóa trên Antigravity	Trọng số Hội tụ Khuyến nghị
1. Sản xuất, Bán lẻ, Tiêu dùng, Công nghệ	VNM, FPT, MWG, PNJ, DGC, HPG	

Nhóm chu kỳ (Thép, Hóa chất) có EPS đỉnh chu kỳ rất cao và P/E rất thấp, dễ tạo bẫy giá trị chu kỳ.

	

Sticker Price & MOS (50%); Payback Time (
≤
8
≤8 năm); 10 Cap (Owner Earnings); 2-Stage DCF (chuẩn hóa EPS trung bình 5 năm cho ngành chu kỳ).

	

30% Sticker MOS; 25% Payback Time; 25% 10 Cap; 20% 2-Stage DCF.


2. Bất động sản Dân dụng & KCN	VHM, NLG, KDH, KBC, IDC, SIP	

Doanh thu/EPS ghi nhận dồn cục khi bàn giao nhà; FCF âm nặng khi gom quỹ đất dù giá trị thực tăng.

	

RNAV / SOTP (Đánh giá lại Hàng tồn kho & Chiết khấu dòng tiền từng dự án); P/B Mục tiêu điều chỉnh Người mua trả tiền trước.

	

70% RNAV (Chiết khấu MOS); 30% Justified P/B Dự án.


3. Ngân hàng, Chứng khoán, Bảo hiểm	VCB, ACB, MBB, TCB, SSI, BVH	

Nợ vay là nguyên liệu kinh doanh; không có khái niệm Vốn lưu động hay FCF/CapEx truyền thống.

	

Residual Income (Thu nhập thặng dư); BVPS Compounding Sticker Price (Biến thể Rule #1 theo P/B & ROE); Justified P/B.

	

40% Residual Income; 40% BVPS Sticker MOS; 20% Justified P/B.


4. Hạ tầng, Điện, Nước, Cảng biển	REE, BWE, NT2, GMD, ACV, PHP	

Tài sản cố định cực lớn, khấu hao kế toán làm méo mó EPS trong khi dòng tiền mặt thực rất dồi dào.

	

10 Cap (Owner Earnings); 2-Stage FCFF / EV/EBITDA; Chiết khấu Cổ tức (DDM / GGM).

	

40% 10 Cap Owner Earnings; 35% FCFF DCF; 25% DDM / GGM.

  
Nhóm 1: Ngành Sản xuất, Tiêu dùng, Bán lẻ và Công nghệ (Biến thể Phẳng và Biến thể Chu kỳ)

Đối với các doanh nghiệp tăng trưởng bền vững có con hào thương hiệu hoặc công nghệ rõ nét (như FPT, VNM, PNJ), bộ tứ công thức của Phil Town và Buffett hoạt động với hiệu suất cao nhất. Tuy nhiên, đối với nhóm ngành Sản xuất Chu kỳ (Thép như HPG, HSG; Hóa chất và Phân bón như DGC, DPM; Thủy sản như VHC), nếu thuật toán lấy 
𝐸
𝑃
𝑆
TTM
EPS
TTM
	​

 tại đỉnh chu kỳ giá hàng hóa để chạy Sticker Price trong 10 năm, kết quả định giá sẽ bị thổi phồng nghiêm trọng.   

Để khắc phục hiện tượng này, Antigravity phải thay thế 
𝐸
𝑃
𝑆
TTM
EPS
TTM
	​

 và 
𝐹
𝐶
𝐹
TTM
FCF
TTM
	​

 bằng Lợi nhuận Chuẩn hóa Giữa Chu kỳ (Normalized Mid-Cycle EPS & FCF) trước khi đưa vào công thức Sticker Price và 10 Cap:   

𝐸
𝑃
𝑆
Normalized
=
BVPS
Hiện tại
×
𝑅
𝑂
𝐸
Trung b
ı
ˋ
nh Chu k
y
ˋ
 5–7 n
a
˘
m
EPS
Normalized
	​

=BVPS
Hiện tại
	​

×ROE
Trung b
ı
ˋ
nh Chu k
y
ˋ
	​

 5–7 n
a
˘
m
	​

𝐹
𝐶
𝐹
Normalized
=
Doanh thu
Hiện tại
×
Bi
e
ˆ
n FCF
Trung b
ı
ˋ
nh Chu k
y
ˋ
 5–7 n
a
˘
m
FCF
Normalized
	​

=Doanh thu
Hiện tại
	​

×Bi
e
ˆ
n FCF
Trung b
ı
ˋ
nh Chu k
y
ˋ
	​

 5–7 n
a
˘
m
	​


Cách tiếp cận này giúp hệ thống tự động hạ định giá khi cổ phiếu chu kỳ đang ở đỉnh lợi nhuận và nâng định giá để nhận diện cơ hội mua khi doanh nghiệp đang ở đáy chu kỳ nhưng bảng cân đối kế toán vẫn nằm trong vùng an toàn (
𝑍
-Score
>
2
,
99
Z-Score>2,99).   

Nhóm 2: Ngành Bất động sản (Dân dụng và Khu Công nghiệp) — Mô hình RNAV (Revalued Net Asset Value)

Trong chế độ kế toán Việt Nam, doanh nghiệp phát triển bất động sản chỉ được phép ghi nhận doanh thu và lợi nhuận lên Báo cáo kết quả kinh doanh khi đã bàn giao bất động sản cho khách hàng, bất chấp việc dự án đã bán hết và thu tiền mặt về từ nhiều năm trước. Do đó, định giá cổ phiếu bất động sản bằng P/E hay tăng trưởng EPS ngắn hạn là không phù hợp; phương pháp tiêu chuẩn bắt buộc là Định giá lại Giá trị Tài sản Ròng (RNAV / Sum-of-the-Parts - SOTP).   

Trên Bảng cân đối kế toán bất động sản, hai khoản mục trọng yếu nhất là Hàng tồn kho (Mã số 140) kết hợp Chi phí xây dựng cơ bản dở dang dài hạn (Mã số 242) — nơi ghi nhận quỹ đất theo giá vốn lịch sử — và Người mua trả tiền trước ngắn hạn/dài hạn (Mã số 312 và 332) — nơi phản ánh lượng tiền mặt khách hàng đã thanh toán theo tiến độ dự án. Hệ thống Antigravity định giá từng dự án 
𝑖
i bằng phương pháp chiết khấu dòng tiền dự án (NPV dự án) với tỷ suất chiết khấu là 
𝑊
𝐴
𝐶
𝐶
WACC của doanh nghiệp, sau đó cộng phần chênh lệch đánh giá lại vào Vốn chủ sở hữu sổ sách để thu được tổng RNAV:   

𝑁
𝑃
𝑉
Dự 
a
ˊ
n 
𝑖
=
∑
𝑡
=
1
𝑇
𝑖
D
o
ˋ
ng ti
e
ˆ
ˋ
n Thu
a
ˆ
ˋ
n Dự 
a
ˊ
n
𝑖
,
𝑡
(
1
+
𝑊
𝐴
𝐶
𝐶
)
𝑡
NPV
Dự 
a
ˊ
n i
	​

=
t=1
∑
T
i
	​

	​

(1+WACC)
t
D
o
ˋ
ng ti
e
ˆ
ˋ
n Thu
a
ˆ
ˋ
n Dự 
a
ˊ
n
i,t
	​

	​

RNAV
Tổng
=
V
o
ˆ
ˊ
n Chủ sở hữu Sổ s
a
ˊ
ch (M
a
˜
 400)
+
∑
𝑖
=
1
𝑘
(
𝑁
𝑃
𝑉
Dự 
a
ˊ
n 
𝑖
−
Gi
a
ˊ
 trị Ghi sổ Dự 
a
ˊ
n 
𝑖
)
RNAV
Tổng
	​

=V
o
ˆ
ˊ
n Chủ sở hữu Sổ s
a
ˊ
ch (M
a
˜
 400)+
i=1
∑
k
	​

(NPV
Dự 
a
ˊ
n i
	​

−Gi
a
ˊ
 trị Ghi sổ Dự 
a
ˊ
n i)

Trong trường hợp công cụ chạy tự động hàng loạt (Screening Mode) khi người dùng chưa nhập bảng dòng tiền chi tiết của từng lô đất, Antigravity sử dụng Công thức RNAV Định lượng Nhanh (Automated Proxy RNAV) trích xuất trực tiếp từ BCTC:   

RNAV
Proxy
=
VCSH (M
a
˜
 400)
+
[
Người mua trả ti
e
ˆ
ˋ
n trước (M
a
˜
 312 + 332)
×
Bi
e
ˆ
n LN R
o
ˋ
ng TB 3 n
a
˘
m
]
+
[
(
H
a
ˋ
ng t
o
ˆ
ˋ
n kho (M
a
˜
 140)
−
Người mua trả ti
e
ˆ
ˋ
n trước
)
×
𝜆
]
RNAV
Proxy
	​

=VCSH (M
a
˜
 400)+[Người mua trả ti
e
ˆ
ˋ
n trước (M
a
˜
 312 + 332)×Bi
e
ˆ
n LN R
o
ˋ
ng TB 3 n
a
˘
m]+[(H
a
ˋ
ng t
o
ˆ
ˋ
n kho (M
a
˜
 140)−Người mua trả ti
e
ˆ
ˋ
n trước)×λ]

Trong công thức trên, hệ số thặng dư quỹ đất 
𝜆
λ được thiết lập dựa trên chất lượng pháp lý và lịch sử sinh lời của quỹ đất (mặc định 
𝜆
=
0
,
20
λ=0,20 đến 
0
,
50
0,50 đối với doanh nghiệp có lịch sử 
𝑅
𝑂
𝐼
𝐶
≥
10
%
ROIC≥10%). Sau khi tính được RNAV trên mỗi cổ phiếu, áp dụng triết lý Biên an toàn của Phil Town và Buffett, Giá Mua Bất động sản An toàn được xác định bằng cách chiết khấu tỷ lệ rủi ro thanh khoản và pháp lý (
𝑀
𝑂
𝑆
BĐS
=
30
%
−
50
%
MOS
BĐS
	​

=30%−50%):   

𝑃
Buy (BĐS)
=
RNAV
Tổng
S
o
ˆ
ˊ
 CP Pha lo
a
˜
ng
×
(
1
−
𝑀
𝑂
𝑆
BĐS
)
P
Buy (BĐS)
	​

=
S
o
ˆ
ˊ
 CP Pha lo
a
˜
ng
RNAV
Tổng
	​

	​

×(1−MOS
BĐS
	​

)
Nhóm 3: Ngành Ngân hàng, Chứng khoán và Bảo hiểm — Mô hình Thu nhập Thặng dư (Residual Income) và BVPS Sticker Price

Đối với các định chế tài chính, đặc biệt là Ngân hàng thương mại, tiền gửi của khách hàng và vốn vay liên ngân hàng chính là nguyên liệu đầu vào để sản xuất ra tín dụng. Do đó, mọi công thức dựa trên 
𝐸
𝐵
𝐼
𝑇
EBIT, 
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
EBITDA, Vốn lưu động hay 
𝐹
𝐶
𝐹
FCF đều phải bị vô hiệu hóa. Trường phái giá trị của Buffett định giá ngân hàng dựa trên chất lượng tài sản, khả năng sinh lời trên vốn chủ sở hữu (
𝑅
𝑂
𝐸
ROE) và tốc độ tăng trưởng Giá trị Sổ sách (
𝐵
𝑉
𝑃
𝑆
BVPS).   

Antigravity cần triển khai song song hai công thức chuyên biệt cho nhóm ngành này. Phương pháp thứ nhất là Mô hình Thu nhập Thặng dư (Residual Income Model - RI): một ngân hàng chỉ thực sự tạo ra giá trị gia tăng cho cổ đông khi tỷ suất sinh lời thực tế trên vốn chủ sở hữu (
𝑅
𝑂
𝐸
Thực
ROE
Thực
	​

, sau khi đã trừ trích lập Quỹ khen thưởng phúc lợi TK 353) lớn hơn Chi phí Vốn Chủ sở hữu (
𝐾
𝑒
K
e
	​

) mà nhà đầu tư yêu cầu. Thu nhập thặng dư năm 
𝑡
t được xác định bởi 
𝑅
𝐼
𝑡
=
(
𝑅
𝑂
𝐸
Thực
,
𝑡
−
𝐾
𝑒
)
×
𝐵
𝑉
𝑃
𝑆
𝑡
−
1
RI
t
	​

=(ROE
Thực,t
	​

−K
e
	​

)×BVPS
t−1
	​

, từ đó suy ra Giá trị Nội tại theo mô hình RI 10 năm kết hợp giá trị cuối kỳ:   

𝐼
𝑉
Bank (RI)
=
𝐵
𝑉
𝑃
𝑆
0
+
∑
𝑡
=
1
10
(
𝑅
𝑂
𝐸
Thực
,
𝑡
−
𝐾
𝑒
)
×
𝐵
𝑉
𝑃
𝑆
𝑡
−
1
(
1
+
𝐾
𝑒
)
𝑡
+
(
𝑅
𝑂
𝐸
Terminal
−
𝐾
𝑒
)
×
𝐵
𝑉
𝑃
𝑆
10
(
𝐾
𝑒
−
𝑔
Terminal
)
×
(
1
+
𝐾
𝑒
)
10
IV
Bank (RI)
	​

=BVPS
0
	​

+
t=1
∑
10
	​

(1+K
e
	​

)
t
(ROE
Thực,t
	​

−K
e
	​

)×BVPS
t−1
	​

	​

+
(K
e
	​

−g
Terminal
	​

)×(1+K
e
	​

)
10
(ROE
Terminal
	​

−K
e
	​

)×BVPS
10
	​

	​


Phương pháp thứ hai là Biến thể Rule #1 Sticker Price theo Giá trị Sổ sách và P/B (BVPS Compounding Method). Thay vì phóng chiếu EPS và nhân với P/E, thuật toán phóng chiếu Giá trị Sổ sách trên mỗi cổ phiếu (
𝐵
𝑉
𝑃
𝑆
BVPS) sau 10 năm theo tốc độ tăng trưởng vốn tự có bền vững 
𝑔
BV
=
𝑅
𝑂
𝐸
Thực
×
(
1
−
Tỷ lệ Chi trả Cổ tức Ti
e
ˆ
ˋ
n mặt
)
g
BV
	​

=ROE
Thực
	​

×(1−Tỷ lệ Chi trả Cổ tức Ti
e
ˆ
ˋ
n mặt), sau đó nhân với hệ số 
𝑃
/
𝐵
P/B hợp lý (Justified P/B) và chiết khấu về hiện tại ở mức 
𝑀
𝐴
𝑅
𝑅
=
15
%
MARR=15%:   

𝐵
𝑉
𝑃
𝑆
10
=
𝐵
𝑉
𝑃
𝑆
0
×
(
1
+
𝑔
BV
)
10
BVPS
10
	​

=BVPS
0
	​

×(1+g
BV
	​

)
10
𝑃
𝐵
Future
=
min
⁡
(
PB
Trung b
ı
ˋ
nh Lịch sử 5 n
a
˘
m
,
PB
Justified
=
𝑅
𝑂
𝐸
Thực
−
𝑔
Terminal
𝐾
𝑒
−
𝑔
Terminal
)
PB
Future
	​

=min(PB
Trung b
ı
ˋ
nh Lịch sử 5 n
a
˘
m
	​

,PB
Justified
	​

=
K
e
	​

−g
Terminal
	​

ROE
Thực
	​

−g
Terminal
	​

	​

)
𝑃
Sticker (Bank)
=
𝐵
𝑉
𝑃
𝑆
10
×
𝑃
𝐵
Future
(
1
+
0
,
15
)
10
+
PV
(
Cổ tức Ti
e
ˆ
ˋ
n mặt 10 n
a
˘
m
)
P
Sticker (Bank)
	​

=
(1+0,15)
10
BVPS
10
	​

×PB
Future
	​

	​

+PV(Cổ tức Ti
e
ˆ
ˋ
n mặt 10 n
a
˘
m)
𝑃
MOS (Bank)
=
𝑃
Sticker (Bank)
×
(
1
−
𝑀
𝑂
𝑆
Bank
)
P
MOS (Bank)
	​

=P
Sticker (Bank)
	​

×(1−MOS
Bank
	​

)

Đối với những ngân hàng thương mại đầu ngành tại Việt Nam có bộ đệm dự phòng vững chắc và 
𝑅
𝑂
𝐸
Thực
≥
18
%
ROE
Thực
	​

≥18%, hệ thống có thể thiết lập 
𝑀
𝑂
𝑆
Bank
=
30
%
−
35
%
MOS
Bank
	​

=30%−35% trên giá trị RI/Sticker để phù hợp với độ lệch chuẩn thấp của giá trị sổ sách ngân hàng.   

Nhóm 4: Ngành Hạ tầng, Điện, Nước và Cảng biển — Mô hình Owner Earnings 10 Cap và Chiết khấu Cổ tức (GGM)

Các doanh nghiệp tiện ích và hạ tầng (như BWE, REE, NT2, GMD) có đặc điểm là chi phí đầu tư ban đầu (CapEx) rất lớn để xây dựng nhà máy phát điện, đường ống nước hoặc cầu cảng. Khi công trình đi vào vận hành thương mại, chi phí khấu hao kế toán hàng năm rất cao làm giảm lợi nhuận ròng (khiến EPS thấp và P/E có vẻ đắt), nhưng chi phí bảo trì thực tế lại rất nhỏ, tạo ra một lượng tiền mặt tự do dồi dào và tỷ lệ chi trả cổ tức tiền mặt ổn định.   

Đối với nhóm này, thuật toán Antigravity ưu tiên tối đa cho công thức 10 Cap (Owner Earnings) đã trình bày ở Mục 3 — nơi 
CapEx
Bảo tr
ı
ˋ
CapEx
Bảo tr
ı
ˋ
	​

 thực tế thấp hơn nhiều so với khấu hao kế toán, giúp phát hiện giá trị nội tại ẩn mà chỉ số P/E bỏ sót — kết hợp với Mô hình Tăng trưởng Gordon (GGM) dựa trên dòng tiền chủ sở hữu và dòng cổ tức ổn định:   

𝐼
𝑉
Utility (GGM)
=
Owner Earnings tr
e
ˆ
n m
o
ˆ
˜
i CP
×
(
1
+
𝑔
D
a
ˋ
i hạn
)
𝐾
𝑒
−
𝑔
D
a
ˋ
i hạn
IV
Utility (GGM)
	​

=
K
e
	​

−g
D
a
ˋ
i hạn
	​

Owner Earnings tr
e
ˆ
n m
o
ˆ
˜
i CP×(1+g
D
a
ˋ
i hạn
	​

)
	​

5. Kiến trúc Dữ liệu và Thuật toán Tổng hợp cho Hệ thống Antigravity

Để lập trình viên có thể nhúng trực tiếp toàn bộ nghiên cứu này vào mã nguồn trên Antigravity, phần dưới đây chuẩn hóa bảng ánh xạ mã số chỉ tiêu BCTC Việt Nam và thuật toán tính Điểm Hội tụ Định giá.

Bảng Ánh xạ Biến số Thuật toán với Mã số BCTC Việt Nam (Thông tư 200 & Thông tư 99/2025/TT-BTC)

Khi kết nối API dữ liệu tài chính Việt Nam, hệ thống Antigravity cần truy xuất chính xác các mã số chỉ tiêu sau đây để đảm bảo tính toàn vẹn của dữ liệu đầu vào qua các kỳ kế toán trước và sau ngày 01/01/2026:   

Biến số trong Thuật toán	Nguồn Báo cáo	Mã số Chỉ tiêu / Tài khoản Chuẩn VAS (TT200 / TT99)	Công thức Xử lý Làm sạch Dữ liệu (Data Cleaning Logic)
Cash_Equiv	Bảng CĐKT	Mã 110 + Mã 120 (trừ dự phòng Mã 122)	

Tiền + Tương đương tiền + Đầu tư tài chính ngắn hạn (tiền gửi có kỳ hạn).


Receivables_ST	Bảng CĐKT	Mã 130	

Các khoản phải thu ngắn hạn (theo dõi tỷ lệ Mã 130 / Tổng TS để kiểm soát chất lượng lợi nhuận).


Inventory	Bảng CĐKT	Mã 140 (Gốc: Mã 141, Dự phòng: Mã 149)	

Hàng tồn kho ròng (Trọng tâm định giá RNAV ngành Bất động sản).


Current_Assets	Bảng CĐKT	Mã 100	

Tổng Tài sản ngắn hạn (
100
=
110
+
120
+
130
+
140
+
150
100=110+120+130+140+150).


Fixed_Assets_Tang	Bảng CĐKT	Mã 221 (Nguyên giá: 222, Hao mòn: 223)	

Tài sản cố định hữu hình (Loại trừ TSCĐ hình thành từ Quỹ phúc lợi TK 3533 vì không trích khấu hao vào chi phí SXKD mà ghi giảm trực tiếp TK 3533).


Total_Assets	Bảng CĐKT	Mã 270	

Tổng cộng Tài sản (Khi tính Altman Z, lấy Mã 270 - Mã 227 (TSCĐ vô hình)).


Current_Liab	Bảng CĐKT	Mã 310	

Nợ ngắn hạn (Dùng tính Vốn lưu động 
𝑊
𝐶
=
M
a
˜
 
100
−
M
a
˜
 
310
WC=M
a
˜
 100−M
a
˜
 310).


Buyer_Prepaid	Bảng CĐKT	Mã 312 (Ngắn hạn) + Mã 332 (Dài hạn)	

Người mua trả tiền trước (Dữ liệu đầu vào bắt buộc cho mô hình RNAV BĐS).


Total_Debt	Bảng CĐKT	Mã 320 (Vay ngắn hạn) + Mã 338 (Vay dài hạn)	

Tổng nợ vay chịu lãi (Dùng tính 
𝑅
𝑂
𝐼
𝐶
ROIC, 
𝑊
𝐴
𝐶
𝐶
WACC và bộ lọc 
M
a
˜
 
338
/
𝐹
𝐶
𝐹
≤
3
M
a
˜
 338/FCF≤3).


Welfare_Fund_BS	Bảng CĐKT	Mã 322 (TK 353: 3531, 3532, 3533, 3534)	

Số dư Quỹ khen thưởng phúc lợi trên Bảng CĐKT thuộc nhóm Nợ phải trả.


Total_Equity	Bảng CĐKT	Mã 400 (hoặc Mã 410 - Vốn CSH)	

Vốn chủ sở hữu (Trừ Lợi ích cổ đông không kiểm soát Mã 429 để lấy VCSH Công ty mẹ).


Retained_Earnings	Bảng CĐKT	Mã 421 + Mã 418 (Quỹ đầu tư phát triển)	

Lợi nhuận sau thuế chưa phân phối cộng Quỹ ĐTPT (Dùng cho biến 
𝑋
2
X
2
	​

 trong Altman Z).


NPAT_Parent	KQKD	Mã 61	

Lợi nhuận sau thuế của cổ đông công ty mẹ.


Welfare_Deduct	Thuyết minh / CĐV	Phát sinh Có TK 353 đối ứng Nợ TK 421	

Khoản trích Quỹ KTPL trong kỳ. Nếu API thiếu thuyết minh, ước lượng qua biến động số dư Mã 322 cộng tiền thực chi từ quỹ trên báo cáo LCTT.


CFO	Lưu chuyển TT	Mã 20 (Báo cáo LCTT)	

Lưu chuyển tiền thuần từ hoạt động kinh doanh.


CapEx	Lưu chuyển TT	Mã 21 (Báo cáo LCTT - ghi âm)	

Tiền chi để mua sắm, xây dựng TSCĐ và các tài sản dài hạn khác.

  
Thuật toán Điều chỉnh Biên An toàn Động (Dynamic Margin of Safety) và Điểm Hội tụ

Trong thực tế đầu tư tại Việt Nam, nếu áp dụng cứng nhắc mức chiết khấu 
15
%
15% kèm Biên an toàn 
𝑀
𝑂
𝑆
=
50
%
MOS=50% cho mọi cổ phiếu, hệ thống sẽ chỉ lọc ra được cơ hội mua trong những đợt hoảng loạn toàn thị trường hiếm hoi. Ngược lại, những cổ phiếu đầu ngành có con hào kinh tế độc quyền thường xuyên giao dịch ở vùng định giá cao hơn vì dòng tiền thông minh nhận diện rõ chất lượng của chúng. Do đó, các nhà đầu tư giá trị như Seth Klarman hay những nhà quản lý quỹ áp dụng khung phân tích của Buffett và Phil Town thường linh hoạt sử dụng dải Biên an toàn từ 
20
%
20% đến 
50
%
50% tùy thuộc vào mức độ chắc chắn của dự báo và chất lượng bảng cân đối kế toán.   

Hệ thống Antigravity có thể tự động hóa hoàn toàn quyết định này bằng Thuật toán Định cỡ Biên An toàn Động (Dynamic MOS Sizing) dựa trên ma trận phân hạng chất lượng doanh nghiệp dưới đây:   

Phân hạng Cổ phiếu trên Antigravity	Điều kiện Bộ lọc Định lượng (Big Five, Piotroski F, Altman Z)	Biên An toàn Động (
𝑀
𝑂
𝑆
Động
MOS
Động
	​

) Khuyến nghị	Hành động của Hệ thống Định giá
Hạng 1: Kim Cương (Tier 1 - Compounders)	

Thỏa mãn toàn bộ Big Five (
≥
10
%
≥10%), Nợ dài hạn 
≤
3
×
𝐹
𝐶
𝐹
≤3×FCF, 
𝐹
-Score
∈
[
8
,
9
]
F-Score∈[8,9], và Altman 
𝑍
Z nằm sâu trong vùng An toàn (
𝑍
>
3
,
5
Z>3,5 hoặc 
𝑍
EM
′
′
>
3
,
2
Z
EM
′′
	​

>3,2).

	

25
%
−
30
%
25%−30% trên DCF/RNAV; 
35
%
−
40
%
35%−40% trên Sticker Price.

	

Kích hoạt tín hiệu mua tích lũy từng phần (Dollar-Cost Averaging) ngay khi thị giá chạm vùng mua.


Hạng 2: Tiêu Chuẩn (Tier 2 - Solid Value)	

Thỏa mãn tối thiểu 4/5 tiêu chí Big Five, 
𝐹
-Score
∈
[
6
,
7
]
F-Score∈[6,7], và Altman 
𝑍
Z đạt ngưỡng An toàn (
𝑍
>
2
,
99
Z>2,99 hoặc 
𝑍
EM
′
′
>
2
,
60
Z
EM
′′
	​

>2,60).

	

50
%
50% chuẩn cổ điển trên Sticker Price; Payback Time 
≤
8
≤8 năm.

	

Thiết lập cảnh báo chờ mua (Waiting Alert) khi thị giá chiết khấu đủ 50% so với Sticker Price.


Hạng 3: Xoay Chuyển (Tier 3 - Grey Zone)	

𝐹
-Score
∈
[
4
,
5
]
F-Score∈[4,5] hoặc Altman 
𝑍
Z nằm trong Vùng Xám (
1
,
81
≤
𝑍
≤
2
,
99
1,81≤Z≤2,99 hoặc 
1
,
10
≤
𝑍
EM
′
′
≤
2
,
60
1,10≤Z
EM
′′
	​

≤2,60).

	

50
%
−
60
%
50%−60% trên mọi mô hình; chặn trần giá mua 
≤
𝑃
Zombie
≤P
Zombie
	​

.

	

Yêu cầu định giá cực rẻ (chỉ mua dưới Giá trị Xác sống khi giả định tăng trưởng bằng 0%).


Hạng 4: Loại Bỏ (Tier 4 - Value Trap / Distress)	

𝐹
-Score
≤
3
F-Score≤3 hoặc Altman 
𝑍
Z rơi vào Vùng Nguy hiểm (
𝑍
<
1
,
81
Z<1,81 hoặc 
𝑍
EM
′
′
<
1
,
10
Z
EM
′′
	​

<1,10).

	

Khóa tín hiệu mua (
𝑀
𝑂
𝑆
=
N/A
MOS=N/A).

	

Gắn cờ đỏ "CẢNH BÁO BẪY GIÁ TRỊ (VALUE TRAP)", loại bỏ khỏi danh mục giải ngân bất chấp P/E thấp.

  

Cuối cùng, như Phil Town đã khẳng định, mỗi phương pháp định giá (Sticker Price, 10 Cap, Payback Time, DCF/RNAV) sẽ cho ra một con số khác nhau và mỗi con số đều đúng dưới góc nhìn riêng của nó; chính sự hội tụ (Convergence) của các mức giá này mới là cơ sở mang lại sự tự tin cao nhất cho nhà đầu tư. Trên giao diện Antigravity, thay vì chỉ xuất ra một con số duy nhất, hệ thống cần hiển thị một Vùng Mua Hội Tụ (Convergence Buy Zone) được tính bằng trung bình có trọng số theo ngành (như Bảng Ma trận ở Mục 4), kèm theo Chỉ số Hội tụ Định giá (Convergence Score):   

𝑃
Mục ti
e
ˆ
u Mua (Antigravity)
=
∑
𝑚
=
1
4
𝑤
Ng
a
ˋ
nh
,
𝑚
×
𝑃
Buy
,
𝑚
P
Mục ti
e
ˆ
u Mua (Antigravity)
	​

=
m=1
∑
4
	​

w
Ng
a
ˋ
nh,m
	​

×P
Buy,m
	​

Độ Hội tụ (Convergence Score)
=
1
−
𝜎
(
𝑃
Buy, 1
,
𝑃
Buy, 2
,
𝑃
Buy, 4
)
𝜇
(
𝑃
Buy
)
Độ Hội tụ (Convergence Score)=1−
μ(P
Buy
	​

)
σ(P
Buy, 1
	​

,P
Buy, 2
	​

,P
Buy, 4
	​

)
	​


Khi Độ Hội tụ tiến gần về 
1
1 — tức độ lệch chuẩn 
𝜎
σ giữa giá Sticker MOS, giá 10 Cap, giá Payback 8 năm và giá DCF/RNAV thu hẹp tối đa quanh giá trị trung bình 
𝜇
μ — đồng thời thị giá trên sàn chứng khoán Việt Nam giảm xuống dưới ngưỡng 
𝑃
Mục ti
e
ˆ
u Mua
P
Mục ti
e
ˆ
u Mua
	​

, công cụ trên Antigravity sẽ phát tín hiệu giải ngân mạnh mẽ nhất, kết tinh trọn vẹn kỷ luật bảo toàn vốn của Warren Buffett và hệ thống định lượng của Phil Town.   

6. Khung Phân tích Ngành Chuyên sâu và Lựa chọn Mô hình Định giá Tối ưu

Để khắc phục triệt để hạn chế của việc áp dụng một công thức chung, hệ thống Antigravity cần tích hợp một Mô-đun Phân tích Ngành từ trên xuống (Top-Down Sector Analyzer) trước khi quyết định mô hình định giá chủ đạo cho từng cổ phiếu. Trên thị trường chứng khoán Việt Nam, động lực tăng trưởng của các nhóm ngành gắn liền chặt chẽ với các biến số vĩ mô nội địa: trong kịch bản cơ sở khi tăng trưởng GDP đạt khoảng 
7
,
3
%
7,3% và tăng trưởng tín dụng toàn hệ thống đạt 
16
%
16%, lợi nhuận của các doanh nghiệp niêm yết được kỳ vọng tăng trưởng từ 
14
%
−
15
%
14%−15%, qua đó neo mặt bằng định giá 
𝑃
/
𝐸
P/E dự phóng của VN-Index quanh ngưỡng 
13
,
5
13,5 lần trong điều kiện lạm phát (CPI bình quân khoảng 
3
,
21
%
3,21%) được kiểm soát dưới trần 
4
,
5
%
−
5
,
0
%
4,5%−5,0% và tỷ giá USD/VND duy trì độ biến động hợp lý.   

Tiêu chí Lọc Hiệu quả Vốn Ngành (ROCE, ROE, ROA) và Bộ Công thức Benjamin Graham Bản địa hóa

Trước khi chạy các mô hình phức tạp, thuật toán phân tích ngành trên Antigravity cần sử dụng bộ ba chỉ số Tỷ suất Sinh lời trên Vốn Sử dụng (
𝑅
𝑂
𝐶
𝐸
ROCE), 
𝑅
𝑂
𝐸
ROE và 
𝑅
𝑂
𝐴
ROA để xếp hạng vị thế cạnh tranh của các doanh nghiệp trong cùng một ngành. Trong đó, 
𝑅
𝑂
𝐶
𝐸
ROCE đặc biệt hiệu quả khi so sánh các doanh nghiệp thâm dụng vốn cùng ngành (như thép, hóa chất, điện, cảng biển) để xác định công ty nào tạo ra nhiều lợi nhuận hoạt động nhất trên mỗi đồng vốn dài hạn bỏ ra:   

𝑅
𝑂
𝐶
𝐸
=
𝐸
𝐵
𝐼
𝑇
Tổng T
a
ˋ
i sản (M
a
˜
 270)
−
Nợ Ng
a
˘
ˊ
n hạn (M
a
˜
 310)
ROCE=
Tổng T
a
ˋ
i sản (M
a
˜
 270)−Nợ Ng
a
˘
ˊ
n hạn (M
a
˜
 310)
EBIT
	​


Bên cạnh bộ tứ công thức của Phil Town, vì Warren Buffett là học trò xuất sắc nhất của Benjamin Graham, hệ thống Antigravity nên tích hợp thêm Bộ 3 Công thức Định giá Benjamin Graham đã được hiệu chỉnh cho lãi suất thị trường Việt Nam để làm mốc tham chiếu bảo toàn vốn tuyệt đối:   

Công thức Graham Tăng trưởng Cơ bản: Giả định một doanh nghiệp không tăng trưởng (
𝑔
=
0
%
g=0%) xứng đáng có mức 
𝑃
/
𝐸
P/E cơ sở là 
8
,
5
8,5 lần, sau đó cộng thêm 
2
2 lần tốc độ tăng trưởng kép dự kiến trong 7–10 năm tới (
𝑔
g tính theo đơn vị phần trăm nguyên, ví dụ tăng trưởng 
10
%
10% thì 
𝑔
=
10
g=10):
  

𝐼
𝑉
Graham 1
=
𝐸
𝑃
𝑆
Thực
×
(
8
,
5
+
2
𝑔
)
IV
Graham 1
	​

=EPS
Thực
	​

×(8,5+2g)

Công thức Graham Điều chỉnh Lãi suất Trái phiếu Việt Nam: Công thức gốc của Graham lấy lãi suất trái phiếu doanh nghiệp hạng AAA kỳ hạn 20 năm của Mỹ thời điểm đó là 
4
,
4
%
4,4% chia cho lãi suất hiện hành (
𝑌
Y). Khi áp dụng vào thị trường Việt Nam nơi thị trường trái phiếu doanh nghiệp chưa có chuẩn xếp hạng AAA đồng nhất 20 năm, các chuyên gia phân tích chuẩn hóa mẫu số 
𝑌
VN
Y
VN
	​

 bằng Lãi suất Trái phiếu Chính phủ Việt Nam kỳ hạn 10 năm cộng biên độ 
0
,
5
%
0,5% (
𝑌
VN
=
𝑅
𝑓
+
0
,
5
%
≈
4
,
58
%
+
0
,
5
%
=
5
,
08
%
Y
VN
	​

=R
f
	​

+0,5%≈4,58%+0,5%=5,08%):
  

𝐼
𝑉
Graham 2 (VN)
=
𝐸
𝑃
𝑆
Thực
×
(
8
,
5
+
2
𝑔
)
×
4
,
4
𝑅
𝑓
 (10Y VGB)
+
0
,
5
IV
Graham 2 (VN)
	​

=
R
f (10Y VGB)
	​

+0,5
EPS
Thực
	​

×(8,5+2g)×4,4
	​


Con số Graham (Graham Number) cho Nhóm Tài sản Hữu hình: Kết hợp đồng thời cả giới hạn 
𝑃
/
𝐸
≤
15
P/E≤15 và 
𝑃
/
𝐵
≤
1
,
5
P/B≤1,5 (
15
×
1
,
5
=
22
,
5
15×1,5=22,5), cực kỳ hiệu quả để tìm điểm mua an toàn cho các doanh nghiệp sản xuất và tài chính có giá trị sổ sách thực chất:
  

𝑃
Graham Number
=
22
,
5
×
𝐸
𝑃
𝑆
Thực
×
𝐵
𝑉
𝑃
𝑆
Thực
P
Graham Number
	​

=
22,5×EPS
Thực
	​

×BVPS
Thực
	​

	​

Ma trận Phân tích Đặc thù 8 Nhóm Ngành và Thuật toán Chọn Mô hình Định giá Tối ưu

Không có bất kỳ một mô hình định giá đơn lẻ nào phù hợp cho mọi loại hình doanh nghiệp. Trong khi các doanh nghiệp trưởng thành có dòng tiền tự do ổn định là ứng cử viên lý tưởng cho DCF, thì các tập đoàn trả cổ tức tiền mặt đều đặn lại phù hợp với chiết khấu cổ tức (DDM), còn những ngành có tỷ trọng tài sản hữu hình và tài sản tài chính lớn bắt buộc phải định giá dựa trên giá trị sổ sách (
𝑃
/
𝐵
P/B, 
𝑁
𝐴
𝑉
NAV). Bảng dưới đây thiết lập thuật toán phân nhánh chi tiết cho 8 nhóm ngành trọng yếu trên sàn chứng khoán Việt Nam:   

Phân Ngành Cụ thể tại Việt Nam	Biến số Dẫn dắt Giá trị (Key Value Drivers)	Phương pháp Định giá Nội tại Tối ưu (Absolute)	Phương pháp Định giá Tương đối Tối ưu (Relative)	Lý giải Chuyên môn & Quy tắc Điều chỉnh trên Antigravity
1. Ngân hàng Thương mại (VCB, BID, CTG, ACB, MBB, TCB)	Tăng trưởng tín dụng (hạn mức NHNN), Biên lãi ròng (
𝑁
𝐼
𝑀
NIM), Tỷ lệ tiền gửi không kỳ hạn (
𝐶
𝐴
𝑆
𝐴
CASA), Tỷ lệ nợ xấu (
𝑁
𝑃
𝐿
NPL) & Bao phủ nợ xấu (
𝐿
𝐿
𝑅
LLR).	

Mô hình Thu nhập Thặng dư (
𝑅
𝐼
RI) & BVPS Sticker Price.

	

𝑃
/
𝐵
P/B hồi quy theo 
𝑅
𝑂
𝐸
ROE (Peer 
𝑃
/
𝐵
−
𝑅
𝑂
𝐸
P/B−ROE Matrix).

	

Tài sản ngân hàng có tính thanh khoản và định giá theo thị trường cao nên giá trị sổ sách (
𝐵
𝑉
𝑃
𝑆
BVPS) có độ tin cậy lớn. Phải khấu trừ phần thiếu hụt dự phòng nợ xấu khỏi 
𝐵
𝑉
𝑃
𝑆
0
BVPS
0
	​

 trước khi chạy mô hình.


2. Công ty Chứng khoán (CTCK) (SSI, VND, HCM, VCI, MBS, VIX)	Thanh khoản thị trường (giá trị giao dịch/phiên), Dư nợ cho vay ký quỹ (Margin), Danh mục tự doanh (FVTPL, AFS).	

BVPS Compounding + Đánh giá lại Danh mục Tự doanh (Mark-to-Market NAV).

	

Hệ số 
𝑃
/
𝐵
P/B phân tầng theo quy mô vốn và thị phần.

	

Dữ liệu thực tế tại Việt Nam cho thấy các CTCK đầu ngành (SSI, HCM, MBS, TCX, VIX) giao dịch ở mức 
𝑃
/
𝐵
P/B từ 
2
,
5
x
−
3
,
0
x
2,5x−3,0x, cao hơn hẳn nhóm CTCK vừa và nhỏ (
𝑃
/
𝐵
≈
1
,
5
x
P/B≈1,5x trở xuống) do lợi thế nguồn vốn giá rẻ và hệ thống công nghệ.


3. Bảo hiểm Nhân thọ & Phi Nhân thọ (BVH, PVI, MIG, BMI, PTI)	Doanh thu phí bảo hiểm gốc, Tỷ lệ bồi thường + chi phí (
𝐶
𝑜
𝑚
𝑏
𝑖
𝑛
𝑒
𝑑
 
𝑅
𝑎
𝑡
𝑖
𝑜
<
100
%
Combined Ratio<100%), Lợi suất đầu tư tiền gửi/trái phiếu Chính phủ (
𝑅
𝑓
R
f
	​

).	

Chiết khấu Cổ tức (
𝐷
𝐷
𝑀
DDM) kết hợp Thu nhập Thặng dư (
𝑅
𝐼
RI).

	

𝑃
/
𝐵
P/B kết hợp 
𝑅
𝑂
𝐸
ROE và Tỷ suất Cổ tức (
𝐷
𝑖
𝑣
𝑖
𝑑
𝑒
𝑛
𝑑
 
𝑌
𝑖
𝑒
𝑙
𝑑
Dividend Yield).

	

Ngành bảo hiểm hưởng lợi trực tiếp khi lợi suất trái phiếu và lãi suất tiền gửi nhích lên; tài sản chủ yếu là tiền gửi và trái phiếu nên 
𝑃
/
𝐵
P/B phản ánh sát giá trị nội tại.


4. Bất động sản Dân dụng & Khu Công nghiệp (VHM, KDH, NLG, KBC, IDC,bcm)	

Quỹ đất sạch pháp lý, Tiến độ bán hàng (Pre-sales / Người mua trả tiền trước), Giá thuê đất KCN và dòng vốn FDI thực hiện.

	

Giá trị Tài sản Ròng Đánh giá lại (
𝑅
𝑁
𝐴
𝑉
RNAV / 
𝑆
𝑂
𝑇
𝑃
SOTP) chiết khấu dòng tiền từng dự án.

	

𝑃
/
𝐵
P/B và 
𝑃
/
RNAV
P/RNAV so sánh ngang hàng.

	

Riêng nhóm BĐS Khu công nghiệp nhận tiền thuê đất 1 lần (treo ở Doanh thu chưa thực hiện dài hạn - Mã 336) có dòng tiền đều đặn hơn BĐS dân dụng, có thể kết hợp 
50
%
 RNAV
+
50
%
 10 Cap Owner Earnings
50% RNAV+50% 10 Cap Owner Earnings.


5. Bán lẻ & Hàng Tiêu dùng (FMCG) (VNM, MSN, MWG, PNJ, FRT, SAB)	

Tăng trưởng doanh thu trên cùng cửa hàng (
𝑆
𝑆
𝑆
𝐺
SSSG), Biên lợi nhuận gộp, Vòng quay hàng tồn kho, Sức mạnh thương hiệu (Moat).

	

Bộ tứ Rule #1 (Sticker Price, Payback Time, 10 Cap) & DCF 2 giai đoạn.

	

𝑃
/
𝐸
P/E, 
𝑃
𝐸
𝐺
PEG và 
𝑃
/
𝑆
P/S (dành cho chuỗi bán lẻ đang mở rộng/vực dậy).

	

Với các chuỗi bán lẻ đang trong giai đoạn mở rộng thần tốc hoặc mới thoát lỗ (như FRT giai đoạn đầu chuỗi nhà thuốc), lợi nhuận ròng bị nén nên phải dùng 
𝑃
/
𝑆
P/S và 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
EV/EBITDA thay vì 
𝑃
/
𝐸
P/E đơn thuần.


6. Công nghệ Thông tin & Viễn thông (FPT, CMG, CTR, FOX, ELC)	

Tốc độ tăng trưởng hợp đồng ký mới ở nước ngoài, Biên EBIT mảng phần mềm, Tỷ lệ 
𝑅
𝑂
𝐼
𝐶
ROIC và chất xám nhân sự.

	

Sticker Price (cho phép 
𝑀
𝑂
𝑆
MOS động 
25
%
−
30
%
25%−30%) & DCF 2 giai đoạn.

	

𝑃
𝐸
𝐺
PEG (Price/Earnings to Growth) và 
𝑃
/
𝐸
P/E dự phóng (Forward 
𝑃
/
𝐸
P/E).

	

Công ty công nghệ có tài sản hữu hình thấp nên 
𝑃
/
𝐵
P/B rất cao (vô nghĩa nếu định giá theo 
𝑁
𝐴
𝑉
NAV); công cụ tốt nhất để đo lường độ đắt/rẻ là chỉ số 
𝑃
𝐸
𝐺
PEG.


7. Sản xuất Chu kỳ & Vật liệu Cơ bản (HPG, HSG, DGC, DPM, DCM, BSR, PVT)	

Chu kỳ giá hàng hóa thế giới (thép HRC, phốt pho, phân ure, crack spread lọc dầu, giá cước vận tải biển) & Công suất nhà máy.

	

DCF & Sticker Price dựa trên Lợi nhuận Chuẩn hóa Giữa Chu kỳ (Normalized EPS/FCF).

	

𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
EV/EBITDA, 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
EV/EBIT và 
𝑃
/
𝐵
P/B lịch sử.

	

Các doanh nghiệp như PVT hay HPG có khấu hao và nợ vay đầu tư tàu/nhà máy lớn; dùng 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
EV/EBITDA và 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
EV/EBIT giúp loại bỏ sự khác biệt về cấu trúc nợ vay và chính sách khấu hao giữa các công ty.


8. Điện, Nước, Hạ tầng & Cảng biển (REE, BWE, NT2, POW, GMD, ACV)	Sản lượng điện/nước thương phẩm, Khung giá phát điện/biểu giá dịch vụ cảng, Thời điểm hết khấu hao nhà máy.	

10 Cap (Owner Earnings), Chiết khấu Cổ tức (
𝐷
𝐷
𝑀
DDM / 
𝐺
𝐺
𝑀
GGM) & FCFF DCF.

	

𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
EV/EBITDA và Công thức Cổ tức – Tăng trưởng 
(
𝑅
+
𝐺
)
/
𝑃
𝐸
(R+G)/PE.

	

Phù hợp hoàn hảo với mô hình 
𝐷
𝐷
𝑀
DDM và công thức 
(
𝑅
+
𝐺
)
/
𝑃
𝐸
>
1
,
5
(R+G)/PE>1,5 nhờ tỷ lệ chi trả cổ tức tiền mặt cao và dòng tiền kinh doanh dự báo được trong 10–20 năm.

  
7. Hệ thống Định giá Tương đối (Relative Valuation) và Thuật toán Xác định Giá Bán Mục tiêu (Relative Selling Price)

Một hệ thống đầu tư hoàn chỉnh trên Antigravity không chỉ trả lời câu hỏi "Mua ở giá nào?" mà bắt buộc phải trả lời chính xác câu hỏi "Bán ở giá nào để tối ưu hóa lợi nhuận?". Trong khi các mô hình Định giá Tuyệt đối (Absolute Valuation như DCF, RNAV, 10 Cap) giúp tìm ra Giá trị Nội tại để mua vào với biên an toàn, thì các mô hình Định giá Tương đối (Relative Valuation dựa trên bội số thị trường 
𝑃
/
𝐸
P/E, 
𝑃
/
𝐵
P/B, 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
EV/EBITDA, 
𝑃
𝐸
𝐺
PEG, 
𝑃
/
𝑆
P/S) lại là công cụ sắc bén nhất để đo lường mức độ hưng phấn của thị trường và xác lập Giá Bán Tương đối (Relative Selling Price).   

5 Công thức Định giá Tương đối Chuẩn hóa trên Antigravity

Để định giá tương đối không bị cảm tính, hệ thống cần tự động gom nhóm các doanh nghiệp tương đồng (Peer Group) trong cùng phân ngành ICB có quy mô vốn hóa và mô hình kinh doanh tương đương, sau đó tính toán 5 chỉ số định giá tương đối sau:   

Định giá theo Dải 
𝑃
/
𝐸
P/E Lịch sử (Historical 
𝑃
/
𝐸
P/E Standard Deviation Bands) và 
𝑃
/
𝐸
P/E Ngành:
Thay vì chỉ lấy 
𝐸
𝑃
𝑆
×
𝑃
/
𝐸
Ng
a
ˋ
nh
EPS×P/E
Ng
a
ˋ
nh
	​

 một cách cơ học, thuật toán Antigravity tính trung bình (
𝜇
𝑃
𝐸
μ
PE
	​

) và độ lệch chuẩn (
𝜎
𝑃
𝐸
σ
PE
	​

) của hệ số 
𝑃
/
𝐸
P/E trong 5 năm gần nhất của chính cổ phiếu đó. Khi 
𝑃
/
𝐸
P/E hiện tại lùi về dưới đường 
−
1
SD
−1SD hoặc 
−
2
SD
−2SD (
𝜇
𝑃
𝐸
−
2
𝜎
𝑃
𝐸
μ
PE
	​

−2σ
PE
	​

), cổ phiếu đang ở vùng định giá rẻ lịch sử; ngược lại khi vượt lên trên 
+
1
SD
+1SD đến 
+
2
SD
+2SD (
𝜇
𝑃
𝐸
+
2
𝜎
𝑃
𝐸
μ
PE
	​

+2σ
PE
	​

), cổ phiếu bước vào vùng quá nhiệt:
  

𝑃
Mục ti
e
ˆ
u 
𝑃
/
𝐸
 Cơ sở
=
𝐸
𝑃
𝑆
Thực Dự ph
o
ˊ
ng (Forward)
×
min
⁡
(
𝑃
𝐸
Trung vị Ng
a
ˋ
nh
,
𝜇
𝑃
𝐸
 (5 n
a
˘
m)
)
P
Mục ti
e
ˆ
u P/E Cơ sở
	​

=EPS
Thực Dự ph
o
ˊ
ng (Forward)
	​

×min(PE
Trung vị Ng
a
ˋ
nh
	​

,μ
PE (5 n
a
˘
m)
	​

)
𝑃
B
a
ˊ
n Tương đ
o
ˆ
ˊ
i (Dải tr
e
ˆ
n 
𝑃
/
𝐸
)
=
𝐸
𝑃
𝑆
Thực Dự ph
o
ˊ
ng (Forward)
×
(
𝜇
𝑃
𝐸
 (5 n
a
˘
m)
+
𝑘
×
𝜎
𝑃
𝐸
 (5 n
a
˘
m)
)
(
với 
𝑘
∈
[
1
,
2
]
)
P
B
a
ˊ
n Tương đ
o
ˆ
ˊ
i (Dải tr
e
ˆ
n P/E)
	​

=EPS
Thực Dự ph
o
ˊ
ng (Forward)
	​

×(μ
PE (5 n
a
˘
m)
	​

+k×σ
PE (5 n
a
˘
m)
	​

)(với k∈[1,2])

Định giá 
𝑃
/
𝐵
P/B Kết hợp Ma trận Hồi quy 
𝑅
𝑂
𝐸
ROE (Peer 
𝑃
/
𝐵
−
𝑅
𝑂
𝐸
P/B−ROE Regression):
Hạn chế lớn nhất của phương pháp 
𝑃
/
𝐵
P/B truyền thống là giá trị sổ sách chỉ phản ánh tài sản hữu hình mà bỏ qua tài sản vô hình (thương hiệu, hệ thống quản trị). Để khắc phục điểm yếu này trên Antigravity, thuật toán phải ghép cặp tỷ lệ 
𝑃
/
𝐵
P/B với 
𝑅
𝑂
𝐸
ROE qua một phương trình hồi quy tuyến tính của toàn bộ các công ty cùng ngành: 
𝑃
𝐵
^
𝑖
=
𝛼
+
𝛽
Ng
a
ˋ
nh
×
𝑅
𝑂
𝐸
𝑖
PB
i
	​

=α+β
Ng
a
ˋ
nh
	​

×ROE
i
	​

. Trên biểu đồ phân tán (Scatter Plot) với trục tung là 
𝑅
𝑂
𝐸
ROE và trục hoành là 
𝑃
/
𝐵
P/B, đường chéo hồi quy đại diện cho mức định giá hợp lý: những cổ phiếu nằm ở nửa dưới đường chéo (có 
𝑅
𝑂
𝐸
ROE cao nhưng 
𝑃
/
𝐵
P/B thấp hơn mức hồi quy) là cổ phiếu đang bị định giá thấp; những cổ phiếu nằm ở nửa trên đường chéo là đang bị thị trường định giá quá cao. Chẳng hạn, với mức 
𝑅
𝑂
𝐸
=
24
,
9
%
ROE=24,9% của Vinamilk (VNM), chiếu lên đường chéo hồi quy ngành hàng tiêu dùng nhanh (FMCG) sẽ xác lập mức 
𝑃
/
𝐵
P/B hợp lý khoảng 
6
x
6x, tương ứng giá trị hợp lý 
6
×
15.702
≈
94.212
 đ
o
ˆ
ˋ
ng/cổ phi
e
ˆ
ˊ
u
6×15.702≈94.212 đ
o
ˆ
ˋ
ng/cổ phi
e
ˆ
ˊ
u:
  

𝑃
Mục ti
e
ˆ
u 
𝑃
/
𝐵
−
𝑅
𝑂
𝐸
=
𝐵
𝑉
𝑃
𝑆
Thực
×
(
𝛼
Ng
a
ˋ
nh
+
𝛽
Ng
a
ˋ
nh
×
𝑅
𝑂
𝐸
Thực
)
P
Mục ti
e
ˆ
u P/B−ROE
	​

=BVPS
Thực
	​

×(α
Ng
a
ˋ
nh
	​

+β
Ng
a
ˋ
nh
	​

×ROE
Thực
	​

)

Định giá theo Hệ số 
𝑃
𝐸
𝐺
PEG (Price/Earnings to Growth) và Chỉ số 
(
𝑅
+
𝐺
)
/
𝑃
𝐸
(R+G)/PE:
Chỉ số 
𝑃
𝐸
𝐺
PEG điều chỉnh hệ số 
𝑃
/
𝐸
P/E theo tốc độ tăng trưởng lợi nhuận dự kiến (
𝐺
G, tính theo số nguyên phần trăm). Một cổ phiếu có 
𝑃
𝐸
𝐺
=
1
PEG=1 đang phản ánh đúng giá trị hợp lý; 
𝑃
𝐸
𝐺
<
1
PEG<1 là tín hiệu cổ phiếu đang bị định giá thấp hơn tiềm năng tăng trưởng; và 
𝑃
𝐸
𝐺
>
1
PEG>1 (đặc biệt khi 
𝑃
𝐸
𝐺
≥
1
,
5
−
2
,
0
PEG≥1,5−2,0) phản ánh cổ phiếu đã bị định giá quá cao. Đối với các doanh nghiệp vừa tăng trưởng vừa trả cổ tức tiền mặt, hệ thống bổ sung chỉ số kết hợp tỷ suất cổ tức (
𝑅
=
Cổ tức
/
Thị gi
a
ˊ
R=Cổ tức/Thị gi
a
ˊ
) và tốc độ tăng trưởng (
𝐺
G) của Peter Lynch: một cổ phiếu đạt chuẩn hấp dẫn dài hạn khi 
(
𝑅
+
𝐺
)
/
𝑃
𝐸
>
1
,
5
(R+G)/PE>1,5:
  

𝑃
𝐸
𝐺
=
𝑃
/
𝐸
𝐺
⟹
𝑃
Hợp l
y
ˊ
 
(
𝑃
𝐸
𝐺
=
1
)
=
𝐸
𝑃
𝑆
Thực
×
𝐺
PEG=
G
P/E
	​

⟹P
Hợp l
y
ˊ
	​

 (PEG=1)
	​

=EPS
Thực
	​

×G
Chỉ s
o
ˆ
ˊ
 Cổ tức - T
a
˘
ng trưởng
=
𝑅
 (%)
+
𝐺
 (%)
𝑃
/
𝐸
>
1
,
5
Chỉ s
o
ˆ
ˊ
 Cổ tức - T
a
˘
ng trưởng=
P/E
R (%)+G (%)
	​

>1,5

Định giá Doanh nghiệp theo 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
EV/EBITDA và 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
EV/EBIT:
Đối với các ngành công nghiệp nặng, dầu khí, vận tải biển (như PVT), thép, xi măng và hạ tầng, cấu trúc nợ vay và chi phí khấu hao làm biến dạng hoàn toàn chỉ số 
𝑃
/
𝐸
P/E. Hệ thống Antigravity sử dụng Giá trị Doanh nghiệp (
𝐸
𝑉
=
V
o
ˆ
ˊ
n h
o
ˊ
a
+
Tổng Nợ vay (M
a
˜
 320 + 338)
−
Ti
e
ˆ
ˋ
n v
a
ˋ
 Tương đương ti
e
ˆ
ˋ
n (M
a
˜
 110 + 120)
EV=V
o
ˆ
ˊ
n h
o
ˊ
a+Tổng Nợ vay (M
a
˜
 320 + 338)−Ti
e
ˆ
ˋ
n v
a
ˋ
 Tương đương ti
e
ˆ
ˋ
n (M
a
˜
 110 + 120)) chia cho 
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
EBITDA hoặc 
𝐸
𝐵
𝐼
𝑇
EBIT. Thông thường, mức 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
<
10
EV/EBIT<10 hoặc 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
<
6
x
−
8
x
EV/EBITDA<6x−8x tại Việt Nam là vùng định giá hấp dẫn. Công thức suy ngược từ bội số 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
EV/EBITDA mục tiêu của ngành ra Giá Cổ phiếu Hợp lý là:
  

𝑃
Mục ti
e
ˆ
u 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
=
(
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
Dự ph
o
ˊ
ng
×
Trung vị 
(
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
)
Ng
a
ˋ
nh
)
−
Tổng Nợ vay
+
Ti
e
ˆ
ˋ
n mặt
S
o
ˆ
ˊ
 lượng Cổ phi
e
ˆ
ˊ
u Lưu h
a
ˋ
nh Pha lo
a
˜
ng
P
Mục ti
e
ˆ
u EV/EBITDA
	​

=
S
o
ˆ
ˊ
 lượng Cổ phi
e
ˆ
ˊ
u Lưu h
a
ˋ
nh Pha lo
a
˜
ng
(EBITDA
Dự ph
o
ˊ
ng
	​

×Trung vị (EV/EBITDA)
Ng
a
ˋ
nh
	​

)−Tổng Nợ vay+Ti
e
ˆ
ˋ
n mặt
	​


Định giá theo Doanh thu 
𝑃
/
𝑆
P/S (Price to Sales) cho Cổ phiếu Xoay chuyển (Turnaround):
Dành riêng cho các doanh nghiệp thương mại, bán lẻ đang trong giai đoạn đầu tư mở rộng chuỗi hoặc đang vực dậy sau thời kỳ thua lỗ tạm thời (khi 
𝐸
𝑃
𝑆
≤
0
EPS≤0 làm 
𝑃
/
𝐸
P/E mất tác dụng), hệ thống sử dụng hệ số 
𝑃
/
𝑆
=
V
o
ˆ
ˊ
n h
o
ˊ
a Thị trường
/
Tổng Doanh thu Thu
a
ˆ
ˋ
n
P/S=V
o
ˆ
ˊ
n h
o
ˊ
a Thị trường/Tổng Doanh thu Thu
a
ˆ
ˋ
n để so sánh với trung vị lịch sử và trung vị ngành:
  

𝑃
Mục ti
e
ˆ
u 
𝑃
/
𝑆
=
(
Doanh thu Thu
a
ˆ
ˋ
n Dự ph
o
ˊ
ng
S
o
ˆ
ˊ
 lượng CP Lưu h
a
ˋ
nh
)
×
𝑃
/
𝑆
Mục ti
e
ˆ
u Ng
a
ˋ
nh
P
Mục ti
e
ˆ
u P/S
	​

=(
S
o
ˆ
ˊ
 lượng CP Lưu h
a
ˋ
nh
Doanh thu Thu
a
ˆ
ˋ
n Dự ph
o
ˊ
ng
	​

)×P/S
Mục ti
e
ˆ
u Ng
a
ˋ
nh
	​

Thuật toán Xác định Tỷ lệ Thắng/Thua (Win-Loss Ratio) và Giá Bán Tương đối (Exit Signals)

Trong nguyên tắc đầu tư của các định chế tài chính chuyên nghiệp như SSI hay Vietcap cũng như triết lý của Phil Town, nhà đầu tư mua vào khi thị giá thấp hơn giá trị định giá và bán ra cổ phiếu khi thị giá vượt lên trên giá trị hợp lý để hiện thực hóa lợi nhuận hoặc khi nền tảng cơ bản của doanh nghiệp không còn tuyệt vời.   

Để lượng hóa quyết định mua và bán trên giao diện Antigravity, hệ thống cần thiết lập 3 mốc giá cho mỗi cổ phiếu:

Kịch bản Xấu nhất (
𝑃
Worst
P
Worst
	​

): Được lấy bằng Giá trị Xác sống (
𝑃
Zombie
P
Zombie
	​

 khi tăng trưởng 
𝑔
=
0
%
g=0%) hoặc mức định giá ở cận dưới dải lịch sử (
𝜇
𝑃
𝐸
−
2
𝜎
𝑃
𝐸
μ
PE
	​

−2σ
PE
	​

).   

Kịch bản Cơ sở / Giá Hợp lý (
𝑃
Base / Fair Value
P
Base / Fair Value
	​

): Được tính bằng trung bình có trọng số của các phương pháp định giá nội tại (Sticker Price, RNAV, RI, DCF) và định giá tương đối chuẩn ngành (
𝑃
/
𝐸
P/E, 
𝑃
/
𝐵
−
𝑅
𝑂
𝐸
P/B−ROE, 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
EV/EBITDA). Ví dụ, nếu nhà phân tích tự tin vào dữ liệu tài sản và so sánh ngang hàng của VNM, có thể phân bổ trọng số 
20
%
20% cho phương pháp 
𝑃
/
𝐸
P/E, 
40
%
40% cho phương pháp 
𝑃
/
𝐵
−
𝑅
𝑂
𝐸
P/B−ROE và 
40
%
40% cho mô hình DCF/Sticker Price để tìm ra mức giá hợp lý hội tụ cuối cùng.   

Kịch bản Hưng phấn / Giá Bán Tương đối (
𝑃
Relative Sell / Overvalued
P
Relative Sell / Overvalued
	​

): Mốc giá mà tại đó đám đông trên thị trường đang trả một mức phí quá đắt so với tốc độ tăng trưởng thực tế của doanh nghiệp.   

Từ ba mốc này, Antigravity tự động tính toán Tỷ lệ Lợi nhuận trên Rủi ro (Win-Loss Ratio) tại mức thị giá hiện tại (
𝑃
Market
P
Market
	​

) theo công thức thực chiến:   

Tỷ lệ Win-Loss
=
𝑃
Base (Gi
a
ˊ
 Hợp l
y
ˊ
)
−
𝑃
Market (Thị gi
a
ˊ
)
𝑃
Market (Thị gi
a
ˊ
)
−
𝑃
Worst (Kịch bản X
a
ˆ
ˊ
u)
Tỷ lệ Win-Loss=
P
Market (Thị gi
a
ˊ
)
	​

−P
Worst (Kịch bản X
a
ˆ
ˊ
u)
	​

P
Base (Gi
a
ˊ
 Hợp l
y
ˊ
	​

)
	​

−P
Market (Thị gi
a
ˊ
)
	​

	​


Ví dụ thực tế với cổ phiếu lọc hóa dầu BSR: khi khoảng giá trị hợp lý được xác định từ 
𝑃
Worst
=
13.600
 đ
o
ˆ
ˋ
ng/cổ phi
e
ˆ
ˊ
u
P
Worst
	​

=13.600 đ
o
ˆ
ˋ
ng/cổ phi
e
ˆ
ˊ
u đến 
𝑃
Base
=
22.700
 đ
o
ˆ
ˋ
ng/cổ phi
e
ˆ
ˊ
u
P
Base
	​

=22.700 đ
o
ˆ
ˋ
ng/cổ phi
e
ˆ
ˊ
u và thị giá đang giao dịch ở mức 
16.000
 đ
o
ˆ
ˋ
ng/cổ phi
e
ˆ
ˊ
u
16.000 đ
o
ˆ
ˋ
ng/cổ phi
e
ˆ
ˊ
u, tỷ lệ Win-Loss đạt 
22.700
−
16.000
16.000
−
13.600
=
2
,
8
16.000−13.600
22.700−16.000
	​

=2,8 lần — nghĩa là nếu đúng, phần thưởng thu về gấp 
2
,
8
2,8 lần mức rủi ro nếu sai, kích hoạt tín hiệu mua có xác suất thắng cao.   

Ngược lại, đối với các cổ phiếu đang nắm giữ trong danh mục, Antigravity sẽ kích hoạt 3 Cấp độ Tín hiệu Bán (Automated Exit Triggers) dựa trên sự kết hợp giữa Giá trị Nội tại của Phil Town và Định giá Tương đối của thị trường:   

Cấp độ Tín hiệu Bán trên Antigravity	Điều kiện Kích hoạt Thuật toán (Logic Triggers)	Công thức Xác định Giá Bán Mục tiêu	Hành động Khuyến nghị cho Nhà đầu tư
Cấp 1: Chốt lời Từng phần (Valuation Stretch)	

Thị giá vượt qua Giá Hợp lý Hội tụ (
𝑃
Market
≥
𝑃
Base / Sticker
P
Market
	​

≥P
Base / Sticker
	​

) HOẶC tỷ lệ 
Win-Loss
<
0
,
5
Win-Loss<0,5.

	
𝑃
Sell 1
=
𝑃
Base
=
∑
𝑤
𝑖
𝑃
Fair
,
𝑖
P
Sell 1
	​

=P
Base
	​

=∑w
i
	​

P
Fair,i
	​

	

Dừng giải ngân mới; chốt lời 
30
%
−
50
%
30%−50% vị thế khi cổ phiếu không còn biên an toàn và tiến vào vùng định giá đầy đủ.


Cấp 2: Bán Toàn bộ theo Định giá Tương đối (Relative Overvaluation)	

Thị giá chạm cận trên dải độ lệch chuẩn 5 năm (
𝑃
/
𝐸
≥
𝜇
𝑃
𝐸
+
1
,
5
𝜎
𝑃
𝐸
P/E≥μ
PE
	​

+1,5σ
PE
	​

 hoặc 
𝑃
/
𝐵
≥
𝜇
𝑃
𝐵
+
1
,
5
𝜎
𝑃
𝐵
P/B≥μ
PB
	​

+1,5σ
PB
	​

) HOẶC chỉ số 
𝑃
𝐸
𝐺
≥
1
,
5
PEG≥1,5 (đối với cổ phiếu tăng trưởng).

	
𝑃
Sell 2
=
min
⁡
(
𝐸
𝑃
𝑆
Fwd
×
(
𝜇
𝑃
𝐸
+
1
,
5
𝜎
𝑃
𝐸
)
,
𝐸
𝑃
𝑆
Fwd
×
1
,
5
𝐺
)
P
Sell 2
	​

=min(EPS
Fwd
	​

×(μ
PE
	​

+1,5σ
PE
	​

),EPS
Fwd
	​

×1,5G)	

Bán 
100
%
100% vị thế để thu hồi vốn và lợi nhuận do thị giá đã phản ánh vượt quá xa tốc độ tăng trưởng tương lai.


Cấp 3: Bán Cắt lỗ / Thoát hàng Khẩn cấp do Gãy Nền tảng (Broken Moat)	

Vi phạm Quy tắc Bán số 1 của Phil Town: Doanh nghiệp không còn tuyệt vời (
𝑅
𝑂
𝐼
𝐶
ROIC tụt xuống dưới 
10
%
10% trong 2 năm, 
𝐹
-Score
≤
3
F-Score≤3, hoặc 
𝑍
-Score
Z-Score rơi vào vùng Nguy hiểm).

	

Bán ngay tại Giá Thị trường (
𝑃
Market
P
Market
	​

) bất kể đang lãi hay lỗ.

	

Thoát toàn bộ vị thế ngay lập tức để bảo vệ vốn gốc, tuyệt đối không bình quân giá xuống đối với cổ phiếu suy thoái cơ bản.

  
8. Tối ưu hóa Thuật toán Antigravity — Khắc phục Các Điểm mù Định lượng Thực chiến

Để công cụ trên Antigravity vận hành trơn tru trong môi trường dữ liệu thực tế tại Việt Nam mà không rơi vào bẫy "Đầu vào Rác, Đầu ra Rác" (Garbage In, Garbage Out) hay "Cộng dồn Bảo thủ" (Compounded Conservatism), bạn hãy lập trình bổ sung 4 hàm hiệu chỉnh toán học nâng cao sau đây vào lõi hệ thống:

1. Hàm Tăng trưởng Giảm dần (Decay Growth Rate) thay cho Hàm mũ Tuyến tính 10 năm

Trong công thức Sticker Price gốc của Phil Town (
𝐸
𝑃
𝑆
10
=
𝐸
𝑃
𝑆
0
×
(
1
+
𝑔
)
10
EPS
10
	​

=EPS
0
	​

×(1+g)
10
), việc giả định một công ty tăng trưởng đều đặn ở mức cao (ví dụ 
20
%
/
n
a
˘
m
20%/n
a
˘
m) suốt 10 năm liên tiếp thường dẫn đến sai số phóng đại rất lớn ở nửa cuối chu kỳ. Thay vào đó, hãy lập trình mô hình tăng trưởng hai nhịp ngay trong công thức Sticker Price: giữ tốc độ tăng trưởng 
𝑔
Rule1
g
Rule1
	​

 trong 5 năm đầu (giai đoạn nhìn thấy rõ đơn hàng và lợi thế cạnh tranh), sau đó áp dụng hệ số suy giảm tự nhiên 
𝛿
=
10
%
/
n
a
˘
m
δ=10%/n
a
˘
m từ năm thứ 6 đến năm thứ 10 hướng về tốc độ tăng trưởng GDP danh nghĩa của nền kinh tế:   

𝐸
𝑃
𝑆
10
 (T
o
ˆ
ˊ
i ưu)
=
𝐸
𝑃
𝑆
Thực
,
0
×
(
1
+
𝑔
Rule1
)
5
×
∏
𝑡
=
6
10
(
1
+
max
⁡
(
𝑔
GDP Danh ngh
ı
˜
a
,
𝑔
Rule1
×
(
1
−
0
,
10
)
𝑡
−
5
)
)
EPS
10 (T
o
ˆ
ˊ
i ưu)
	​

=EPS
Thực,0
	​

×(1+g
Rule1
	​

)
5
×
t=6
∏
10
	​

(1+max(g
GDP Danh ngh
ı
˜
a
	​

,g
Rule1
	​

×(1−0,10)
t−5
))
2. Hàm Làm mượt Tỷ lệ Trích Quỹ Khen thưởng Phúc lợi 3 năm (
𝜏
KTPL
τ
KTPL
	​

)

Do các doanh nghiệp niêm yết tại Việt Nam thường chỉ quyết toán chính thức Quỹ khen thưởng phúc lợi (Tài khoản 353) tại kỳ Đại hội đồng cổ đông thường niên và báo cáo kiểm toán năm, dữ liệu trích quỹ trên báo cáo tài chính Quý thường bị trống hoặc ghi nhận dồn cục. Để tránh việc chỉ số 
𝐸
𝑃
𝑆
Thực (TTM)
EPS
Thực (TTM)
	​

 trên Antigravity bị giật cục giữa các quý, thuật toán nên tính Tỷ lệ Trích lập Quỹ KTPL Bình quân Gia quyền 3 năm kiểm toán gần nhất (
𝜏
KTPL
τ
KTPL
	​

) và dùng tỷ lệ này để khấu trừ tự động cho các quý tiếp theo:   

𝜏
KTPL
=
∑
𝑦
=
𝑡
−
3
𝑡
−
1
S
o
ˆ
ˊ
 ti
e
ˆ
ˋ
n Tr
ı
ˊ
ch Qu
y
˜
 KTPL (TK 353)
𝑦
∑
𝑦
=
𝑡
−
3
𝑡
−
1
𝐿
𝑁
𝑆
𝑇
Cổ đ
o
ˆ
ng C
o
ˆ
ng ty mẹ
,
𝑦
τ
KTPL
	​

=
∑
y=t−3
t−1
	​

LNST
Cổ đ
o
ˆ
ng C
o
ˆ
ng ty mẹ,y
	​

∑
y=t−3
t−1
	​

S
o
ˆ
ˊ
 ti
e
ˆ
ˋ
n Tr
ı
ˊ
ch Qu
y
˜
	​

 KTPL (TK 353)
y
	​

	​

𝐸
𝑃
𝑆
Thực (TTM Chuẩn h
o
ˊ
a)
=
(
∑
𝑞
=
1
4
𝐿
𝑁
𝑆
𝑇
Qu
y
ˊ
 
𝑞
S
o
ˆ
ˊ
 CP Pha lo
a
˜
ng
)
×
(
1
−
𝜏
KTPL
)
EPS
Thực (TTM Chuẩn h
o
ˊ
a)
	​

=(
S
o
ˆ
ˊ
 CP Pha lo
a
˜
ng
∑
q=1
4
	​

LNST
Qu
y
ˊ
	​

 q
	​

	​

)×(1−τ
KTPL
	​

)
3. Hàm Kiểm định Thanh khoản Hàng tồn kho Bất động sản và Chất lượng Tài sản Ngân hàng

Đối với ngành Bất động sản: Để ngăn chặn việc thuật toán RNAV định giá cao những công ty có "hàng tồn kho chết" (dự án bị treo pháp lý nhiều năm không thể mở bán), Antigravity cần cài đặt một hệ số kích hoạt thanh khoản 
𝜅
Ph
a
ˊ
p l
y
ˊ
∈
[
0
,
1
]
κ
Ph
a
ˊ
p l
y
ˊ
	​

	​

∈[0,1] dựa trên tỷ lệ Người mua trả tiền trước (Mã 312 + 332) chia cho Hàng tồn kho (Mã 140). Nếu tỷ lệ này dưới 
5
%
5% và doanh thu bất động sản 2 năm liên tiếp sụt giảm, hệ số thặng dư quỹ đất 
𝜆
λ tự động bị ép về 
0
0 (chỉ định giá theo giá gốc sổ sách):
  

𝜆
Thực t
e
ˆ
ˊ
=
𝜆
Cơ sở
×
min
⁡
(
1
,
Người mua trả ti
e
ˆ
ˋ
n trước (M
a
˜
 312 + 332)
0
,
15
×
H
a
ˋ
ng t
o
ˆ
ˋ
n kho (M
a
˜
 140)
)
λ
Thực t
e
ˆ
ˊ
	​

=λ
Cơ sở
	​

×min(1,
0,15×H
a
ˋ
ng t
o
ˆ
ˋ
n kho (M
a
˜
 140)
Người mua trả ti
e
ˆ
ˋ
n trước (M
a
˜
 312 + 332)
	​

)

Đối với ngành Ngân hàng: Trước khi đưa Giá trị sổ sách (
𝐵
𝑉
𝑃
𝑆
0
BVPS
0
	​

) vào mô hình Thu nhập Thặng dư (
𝑅
𝐼
RI) hoặc định giá 
𝑃
/
𝐵
−
𝑅
𝑂
𝐸
P/B−ROE, hệ thống cần kiểm tra xem Quỹ dự phòng rủi ro tín dụng của ngân hàng đã bao phủ đủ 
100
%
100% Nợ xấu (Nhóm 3, Nhóm 4, Nhóm 5) hay chưa. Nếu Tỷ lệ bao phủ nợ xấu (
𝐿
𝐿
𝑅
<
100
%
LLR<100%), phần thiếu hụt dự phòng phải được trừ thẳng vào Vốn chủ sở hữu để có Giá trị sổ sách thực chất (
𝐵
𝑉
𝑃
𝑆
Thực
BVPS
Thực
	​

):
  

𝐵
𝑉
𝑃
𝑆
Thực (Bank)
=
𝐵
𝑉
𝑃
𝑆
B
a
ˊ
o c
a
ˊ
o
−
max
⁡
(
0
,
Tổng Nợ x
a
ˆ
ˊ
u (Nh
o
ˊ
m 3–5)
−
S
o
ˆ
ˊ
 dư Dự ph
o
ˋ
ng Rủi ro T
ı
ˊ
n dụng
)
×
(
1
−
𝑡
)
S
o
ˆ
ˊ
 lượng Cổ phi
e
ˆ
ˊ
u Lưu h
a
ˋ
nh
BVPS
Thực (Bank)
	​

=BVPS
B
a
ˊ
o c
a
ˊ
o
	​

−
S
o
ˆ
ˊ
 lượng Cổ phi
e
ˆ
ˊ
u Lưu h
a
ˋ
nh
max(0,Tổng Nợ x
a
ˆ
ˊ
u (Nh
o
ˊ
m 3–5)−S
o
ˆ
ˊ
 dư Dự ph
o
ˋ
ng Rủi ro T
ı
ˊ
n dụng)×(1−t)
	​

4. Phối hợp Tỷ trọng Định giá Nội tại và Định giá Tương đối trên Giao diện Antigravity

Để công cụ vừa giữ được triết lý đầu tư giá trị sâu sắc của Warren Buffett – Phil Town, vừa bám sát nhịp đập dòng tiền trên thị trường chứng khoán Việt Nam, đầu ra cuối cùng trên bảng điều khiển (Dashboard) của Antigravity nên kết hợp 70% Trọng số Định giá Nội tại (Intrinsic Valuation) và 30% Trọng số Định giá Tương đối (Relative Peer & Historical Valuation):   

𝑃
Fair Value Tổng hợp
=
0
,
70
×
𝑃
Nội tại Hội tụ theo Ng
a
ˋ
nh
+
0
,
30
×
𝑃
Tương đ
o
ˆ
ˊ
i Chuẩn Ng
a
ˋ
nh
P
Fair Value Tổng hợp
	​

=0,70×P
Nội tại Hội tụ theo Ng
a
ˋ
nh
	​

+0,30×P
Tương đ
o
ˆ
ˊ
i Chuẩn Ng
a
ˋ
nh
	​


Từ mức 
𝑃
Fair Value Tổng hợp
P
Fair Value Tổng hợp
	​

 này, hệ thống áp dụng tỷ lệ Biên An toàn Động (
𝑀
𝑂
𝑆
Động
MOS
Động
	​

 từ 
25
%
25% đến 
50
%
50% tùy theo phân hạng chất lượng từ Hạng 1 đến Hạng 3 ở Mục 5) để xuất ra Giá Mua Khuyến nghị (
𝑃
Buy
P
Buy
	​

), đồng thời hiển thị Tỷ lệ Win-Loss và Giá Bán Tương đối (
𝑃
Sell 1
,
𝑃
Sell 2
P
Sell 1
	​

,P
Sell 2
	​

). Cấu trúc thuật toán toàn diện này sẽ biến công cụ trên Antigravity của bạn thành một hệ thống phân tích đầu tư định lượng chuyên nghiệp, tự động thích nghi với từng nhóm ngành trên thị trường chứng khoán Việt Nam.   

=== PHẦN MỚI ===

Kiến trúc Thuật toán Định giá Cổ phiếu Đa Ngành tại Thị trường Việt Nam theo Trường phái Warren Buffett và Phil Town
1. Bản chất Định giá Giá trị và Yêu cầu Bản địa hóa Dữ liệu tại Việt Nam

Việc xây dựng một hệ thống định giá cổ phiếu tự động trên nền tảng Antigravity đòi hỏi sự chuyển hóa các nguyên lý định tính và định lượng của Warren Buffett và Phil Town thành các thuật toán toán học chặt chẽ. Trọng tâm của trường phái đầu tư giá trị hiện đại không nằm ở việc dự báo chính xác tuyệt đối biến động thị trường ngắn hạn, mà nằm ở việc xác định Giá trị Nội tại (Intrinsic Value) của những doanh nghiệp sở hữu lợi thế cạnh tranh bền vững (Moat) và chỉ giải ngân khi thị giá chiết khấu sâu so với giá trị thực nhằm thiết lập Biên An toàn (Margin of Safety - MOS). Trong khi Warren Buffett đặt nền móng với khái niệm Dòng tiền Chủ sở hữu (Owner Earnings) và chiết khấu dòng tiền (DCF), Phil Town đã chuẩn hóa triết lý này thành hệ thống Quy tắc Số 1 (Rule #1 Investing) với bốn phương pháp định giá hội tụ gồm Giá Niêm yết (Sticker Price), Giá 10 Cap (10 Cap Price), Thời gian Hoàn vốn (Payback Time) và Giá trị Xác sống (Zombie Value).   

Tuy nhiên, một sai lầm phổ biến trong các công cụ định giá tự động là áp dụng một công thức chiết khấu dòng tiền hoặc bội số P/E duy nhất cho toàn bộ thị trường. Cấu trúc bảng cân đối kế toán và cơ chế ghi nhận doanh thu của một ngân hàng thương mại, một nhà phát triển bất động sản, một tập đoàn sản xuất thép hay một doanh nghiệp bán lẻ là hoàn toàn khác biệt. Hơn thế nữa, khi áp dụng các công thức của Phố Wall vào thị trường chứng khoán Việt Nam, thuật toán bắt buộc phải xử lý các độ lệch chuẩn mực kế toán theo Chuẩn mực Kế toán Việt Nam (VAS), đặc biệt là sự chuyển dịch pháp lý từ Thông tư 200/2014/TT-BTC sang Thông tư 99/2025/TT-BTC có hiệu lực từ ngày 01/01/2026. Nếu không làm sạch dữ liệu đầu vào (Data Normalization), mọi mô hình định giá tự động sẽ rơi vào trạng thái sai lệch hệ thống, khiến nhà đầu tư mua nhầm các bẫy giá trị (Value Traps) hoặc định giá cao hơn thực tế từ 15% đến 30%.   

Xử lý Rò rỉ Lợi nhuận từ Quỹ Khen thưởng Phúc lợi và Pha loãng Cổ phiếu

Điểm khác biệt cốt lõi nhất giữa báo cáo tài chính (BCTC) theo chuẩn VAS và chuẩn quốc tế (IFRS/US GAAP) ảnh hưởng trực tiếp đến mọi công thức định giá của Buffett và Phil Town là khoản mục Quỹ khen thưởng, phúc lợi thuộc Tài khoản 353 theo Thông tư 200/2014/TT-BTC và tiếp tục được quy định chi tiết tại Thông tư 99/2025/TT-BTC. Theo chuẩn quốc tế, chi phí thưởng cho nhân viên và ban điều hành phải được hạch toán trực tiếp vào chi phí hoạt động trên Báo cáo kết quả kinh doanh trước khi tính Lợi nhuận sau thuế (LNST). Ngược lại, tại Việt Nam, khoản tiền này được trích lập từ Lợi nhuận sau thuế chưa phân phối (Tài khoản 421) sang Tài khoản 353 thuộc nhóm Nợ phải trả, bao gồm bốn tiểu khoản: Quỹ khen thưởng (3531), Quỹ phúc lợi (3532), Quỹ phúc lợi đã hình thành TSCĐ (3533) và Quỹ thưởng ban quản lý điều hành (3534).   

Đây là phần lợi nhuận chảy ra khỏi túi cổ đông nhưng không đi qua báo cáo chi phí. Nếu thuật toán trên Antigravity lấy trực tiếp LNST chia cho số lượng cổ phiếu để tính EPS hoặc lấy Dòng tiền tự do (FCF) mà không trừ đi phần trích lập này, hệ thống sẽ thổi phồng giá trị nội tại của những doanh nghiệp có thói quen trích quỹ khen thưởng phúc lợi lớn hàng năm. Công thức chuẩn hóa EPS thực nhận của cổ đông trên hệ thống phải được lập trình như sau:   

𝐸
𝑃
𝑆
Thực (Adjusted)
=
𝐿
𝑁
𝑆
𝑇
Cổ đ
o
ˆ
ng c
o
ˆ
ng ty mẹ
−
Tr
ı
ˊ
ch Qu
y
˜
 Khen thưởng Ph
u
ˊ
c lợi (TK 353)
−
Cổ tức Cổ phi
e
ˆ
ˊ
u Ưu đ
a
˜
i
S
o
ˆ
ˊ
 lượng Cổ phi
e
ˆ
ˊ
u Lưu h
a
ˋ
nh B
ı
ˋ
nh qu
a
ˆ
n Pha lo
a
˜
ng
EPS
Thực (Adjusted)
	​

=
S
o
ˆ
ˊ
 lượng Cổ phi
e
ˆ
ˊ
u Lưu h
a
ˋ
nh B
ı
ˋ
nh qu
a
ˆ
n Pha lo
a
˜
ng
LNST
Cổ đ
o
ˆ
ng c
o
ˆ
ng ty mẹ
	​

−Tr
ı
ˊ
ch Qu
y
˜
	​

 Khen thưởng Ph
u
ˊ
c lợi (TK 353)−Cổ tức Cổ phi
e
ˆ
ˊ
u Ưu đ
a
˜
i
	​


Trong thực tế vận hành tại Việt Nam, dữ liệu minh họa cho thấy một công ty có LNST đạt 800 tỷ đồng với 200 triệu cổ phiếu lưu hành sẽ có EPS thô là 4.000 đồng/cổ phiếu; nhưng khi đại hội cổ đông quyết định trích 30 tỷ đồng vào quỹ khen thưởng phúc lợi, EPS thực nhận của cổ đông lập tức giảm xuống còn 3.850 đồng/cổ phiếu. Bên cạnh đó, thị trường Việt Nam thường xuyên chứng kiến làn sóng phát hành cổ phiếu thưởng cho nhân viên (ESOP), chào bán riêng lẻ và trái phiếu chuyển đổi trong các chu kỳ nới lỏng tiền tệ. Theo quy định tại VAS 30, thuật toán định giá dài hạn bắt buộc phải sử dụng EPS pha loãng (Diluted EPS) thay vì EPS cơ bản để phản ánh đúng rủi ro chia nhỏ miếng bánh lợi nhuận trong tương lai, ngăn chặn việc hệ thống tự động hạ thấp biên an toàn của danh mục.   

Thiết lập Tham số Chiết khấu Vĩ mô Việt Nam: Kết hợp CAPM (Damodaran) và MARR (Phil Town)

Trong định giá chiết khấu dòng tiền, tỷ suất chiết khấu đóng vai trò là lực hấp dẫn kéo giá trị tương lai về hiện tại. Phil Town sử dụng một mức Tỷ suất Sinh lời Tối thiểu Chấp nhận được (Minimum Acceptable Rate of Return - MARR) cố định ở mức 
15
%
/
n
a
˘
m
15%/n
a
˘
m cho mọi cổ phiếu nhằm đảm bảo quy tắc lãi kép nhân đôi tài sản sau mỗi 5 năm, hoặc nhân 4 lần sau 10 năm do 
(
1
+
0
,
15
)
10
≈
4
,
0456
(1+0,15)
10
≈4,0456. Tuy nhiên, đối với một công cụ định giá chuyên sâu tại thị trường mới nổi như Việt Nam, việc kết hợp cả ngưỡng tuyệt đối 
15
%
15% của Phil Town lẫn Chi phí Vốn Chủ sở hữu (
𝐾
𝑒
K
e
	​

) và Chi phí Vốn Bình quân Gia quyền (
𝑊
𝐴
𝐶
𝐶
WACC) theo mô hình CAPM của Giáo sư Aswath Damodaran sẽ mang lại độ chính xác vượt trội cho từng ngành nghề.   

Dữ liệu thị trường năm 2026 ghi nhận sự hạ nhiệt rõ rệt của mặt bằng rủi ro quốc gia toàn cầu nhưng sự phân hóa giữa các thị trường vẫn duy trì độ dốc lớn. Theo bản cập nhật tháng 7/2026 của Damodaran, phần bù rủi ro vốn cổ phần cơ sở của thị trường phát triển (Mature Market ERP) ở mức 
4
,
17
%
4,17% và của Hoa Kỳ là 
4
,
45
%
4,45%, trong khi chênh lệch vỡ nợ (default spreads) thu hẹp trên diện rộng trong quý 2/2026 khi nhóm xếp hạng A1 giảm từ 67,1 điểm cơ bản xuống 64,7 điểm cơ bản, Baa3 giảm từ 209,1 xuống 201,7 điểm cơ bản, và B3 giảm từ 618,5 xuống 596,4 điểm cơ bản. Đối với Việt Nam, phần bù rủi ro thị trường chứng khoán (ERP) năm 2026 đã giảm về biên độ 
7
,
0
%
−
8
,
0
%
7,0%−8,0% với mức trung vị chuẩn là 
7
,
5
%
7,5%, cải thiện đáng kể so với mức ERP 
9
,
57
%
9,57% và phần bù rủi ro quốc gia 
4
,
57
%
4,57% ở mức xếp hạng tín nhiệm Ba2 vào tháng 7/2023. Kết hợp với lợi suất Trái phiếu Chính phủ Việt Nam kỳ hạn 10 năm (
𝑅
𝑓
R
f
	​

) giao dịch quanh ngưỡng 
4
,
50
%
−
4
,
577
%
4,50%−4,577% (biên độ 52 tuần từ 
3
,
936
%
3,936% đến 
4
,
577
%
4,577%), công thức xác định Chi phí Vốn Chủ sở hữu (
𝐾
𝑒
K
e
	​

) và 
𝑊
𝐴
𝐶
𝐶
WACC trên Antigravity được chuẩn hóa như sau:   

𝐾
𝑒
=
𝑅
𝑓
+
𝛽
Bottom-up
×
𝐸
𝑅
𝑃
VN
=
4
,
5
%
+
𝛽
Bottom-up
×
7
,
5
%
K
e
	​

=R
f
	​

+β
Bottom-up
	​

×ERP
VN
	​

=4,5%+β
Bottom-up
	​

×7,5%
𝑊
𝐴
𝐶
𝐶
=
(
𝐸
𝐸
+
𝐷
×
𝐾
𝑒
)
+
(
𝐷
𝐸
+
𝐷
×
𝐾
𝑑
×
(
1
−
𝑡
)
)
WACC=(
E+D
E
	​

×K
e
	​

)+(
E+D
D
	​

×K
d
	​

×(1−t))

Trong phương trình trên, 
𝛽
Bottom-up
β
Bottom-up
	​

 được tính toán dựa trên rủi ro kinh doanh của ngành và cấu trúc nợ vay trên vốn chủ sở hữu (
𝐷
/
𝐸
D/E) của từng doanh nghiệp thay vì dùng Beta hồi quy lịch sử vốn dễ bị nhiễu bởi tính đầu cơ trên sàn chứng khoán Việt Nam. Đối với một doanh nghiệp có rủi ro trung bình thị trường (
𝛽
=
1
β=1), 
𝐾
𝑒
K
e
	​

 tại Việt Nam năm 2026 rơi vào khoảng 
12
,
0
%
−
12
,
08
%
12,0%−12,08%. Điều này giải thích tại sao việc Phil Town ấn định mức chiết khấu 
𝑀
𝐴
𝑅
𝑅
=
15
%
MARR=15% lại mang tính bảo thủ cực kỳ hiệu quả tại Việt Nam: mức 
15
%
15% cao hơn chi phí vốn cơ sở của thị trường khoảng 
3
%
3%, tự động tích hợp một lớp đệm rủi ro thanh khoản và quản trị trước cả khi áp dụng biên an toàn 50%.   

2. Tầng Lọc Sức khỏe Tài chính và Chống Bẫy Giá trị (Pre-Valuation Gatekeepers)

Cả Warren Buffett và Phil Town đều nhấn mạnh rằng công thức định giá chỉ có ý nghĩa khi được áp dụng cho một doanh nghiệp tuyệt vời (Wonderful Business). Nếu đưa dữ liệu của một doanh nghiệp đang suy thoái cấu trúc hoặc gian lận kế toán vào mô hình P/E hay DCF, thuật toán sẽ nhận diện cổ phiếu đó là rẻ và kích hoạt tín hiệu mua sai lầm — hiện tượng được gọi là Bẫy Giá trị (Value Trap). Do đó, trước khi chạy mô-đun tính giá cổ phiếu, hệ thống Antigravity phải thiết lập một phễu lọc định lượng ba tầng để chấm điểm chất lượng doanh nghiệp và điều chỉnh tự động tỷ lệ Biên An toàn (MOS).   

Tầng 1: Bộ lọc Big Five và Kỷ luật Nợ vay của Phil Town

Để lượng hóa khái niệm Con hào kinh tế (Moat) của Buffett, Phil Town yêu cầu doanh nghiệp phải đạt tốc độ tăng trưởng kép hàng năm (CAGR) tối thiểu 
10
%
/
n
a
˘
m
10%/n
a
˘
m trong suốt 10 năm — hoặc tối thiểu 5 năm liên tiếp đối với dữ liệu thị trường Việt Nam nơi nhiều công ty chưa có lịch sử dữ liệu 10 năm đồng nhất — trên cả năm chỉ số tài chính cốt lõi (Big Five Numbers). Chỉ số đầu tiên và quan trọng nhất là Tỷ suất Sinh lời trên Vốn Đầu tư (
𝑅
𝑂
𝐼
𝐶
ROIC), phản ánh hiệu quả phân bổ vốn của ban lãnh đạo và bắt buộc phải duy trì mức trung bình từ 
10
%
/
n
a
˘
m
10%/n
a
˘
m trở lên:   

𝑅
𝑂
𝐼
𝐶
=
𝐸
𝐵
𝐼
𝑇
×
(
1
−
Thu
e
ˆ
ˊ
 su
a
ˆ
ˊ
t TNDN thực t
e
ˆ
ˊ
)
V
o
ˆ
ˊ
n Chủ sở hữu
+
Nợ vay Ng
a
˘
ˊ
n hạn v
a
ˋ
 D
a
ˋ
i hạn
−
Ti
e
ˆ
ˋ
n v
a
ˋ
 Tương đương ti
e
ˆ
ˋ
n
ROIC=
V
o
ˆ
ˊ
n Chủ sở hữu+Nợ vay Ng
a
˘
ˊ
n hạn v
a
ˋ
 D
a
ˋ
i hạn−Ti
e
ˆ
ˋ
n v
a
ˋ
 Tương đương ti
e
ˆ
ˋ
n
EBIT×(1−Thu
e
ˆ
ˊ
 su
a
ˆ
ˊ
t TNDN thực t
e
ˆ
ˊ
)
	​


Bốn chỉ số tăng trưởng kép còn lại trong bộ Big Five bao gồm tốc độ tăng trưởng Vốn Chủ sở hữu hay Giá trị sổ sách trên mỗi cổ phiếu (Equity / BVPS Growth) phản ánh khả năng tích lũy thặng dư thực chất, tốc độ tăng trưởng EPS pha loãng đã điều chỉnh (Adjusted Diluted EPS Growth), tốc độ tăng trưởng Doanh thu thuần (Sales Growth), và tốc độ tăng trưởng Dòng tiền Tự do (Free Cash Flow Growth); tất cả đều phải đạt ngưỡng 
𝐶
𝐴
𝐺
𝑅
≥
10
%
/
n
a
˘
m
CAGR≥10%/n
a
˘
m. Song song với Big Five, tiêu chí Quản trị Nợ vay (Manageable Debt) đòi hỏi tổng Nợ vay dài hạn (Mã số 338 trên Bảng cân đối kế toán) phải được thanh toán hết trong vòng tối đa 3 năm bằng Dòng tiền tự do hiện tại, tương đương điều kiện 
Long-term Debt
/
𝐹
𝐶
𝐹
≤
3
Long-term Debt/FCF≤3 để đảm bảo doanh nghiệp không bị tổn thương khi chu kỳ tín dụng thắt chặt.   

Tầng 2: Thuật toán Piotroski F-Score (9 Tiêu chí Nhị phân trên BCTC VAS)

Nghiên cứu thực nghiệm chuyên sâu trên mẫu 501 doanh nghiệp niêm yết tại thị trường chứng khoán Việt Nam đã chứng minh rằng việc sử dụng bảng điểm Piotroski F-Score để phân tách doanh nghiệp khỏe mạnh (Winners) và yếu kém (Losers) mang lại tỷ suất sinh lời điều chỉnh theo rủi ro thị trường vượt trội hơn 
30
%
/
n
a
˘
m
30%/n
a
˘
m — một con số có ý nghĩa thống kê rất cao không chỉ ở nhóm cổ phiếu giá trị (P/B thấp) mà cả ở nhóm cổ phiếu tăng trưởng (P/B cao). Trước đó, kiểm nghiệm lịch sử (backtest) gốc của Giáo sư Joseph D. Piotroski trong giai đoạn 20 năm cũng ghi nhận mức gia tăng lợi nhuận bình quân 
+
23
%
/
n
a
˘
m
+23%/n
a
˘
m.   

Trên Antigravity, thuật toán F-Score được lập trình thành hàm tổng của 9 biến nhị phân (nhận giá trị 
1
1 nếu thỏa mãn điều kiện và 
0
0 nếu không thỏa mãn), chia làm ba trụ cột đánh giá khả năng sinh lời, cơ cấu nguồn vốn và hiệu quả hoạt động:   

Nhóm Tiêu chí	Mã Biến	Công thức Toán học và Điều kiện Logic (So sánh Năm 
𝑡
t và Năm 
𝑡
−
1
t−1)	Ý nghĩa Kiểm định Chất lượng BCTC tại Việt Nam
1. Khả năng Sinh lời (4 Điểm)	
𝐹
𝑅
𝑂
𝐴
F
ROA
	​

	
N
e
ˆ
ˊ
u 
𝑅
𝑂
𝐴
𝑡
=
𝐿
𝑁
𝑆
𝑇
Thực
,
𝑡
Tổng T
a
ˋ
i sản
𝑡
>
0
⇒
+
1
 điểm
N
e
ˆ
ˊ
u ROA
t
	​

=
Tổng T
a
ˋ
i sản
t
	​

LNST
Thực,t
	​

	​

>0⇒+1 điểm	

Doanh nghiệp kinh doanh có lãi thực tế sau khi trừ Quỹ KTPL.


	
𝐹
𝐶
𝐹
𝑂
F
CFO
	​

	
N
e
ˆ
ˊ
u 
𝐶
𝐹
𝑂
𝑡
 (Lưu chuyển ti
e
ˆ
ˋ
n thu
a
ˆ
ˋ
n từ HĐKD)
>
0
⇒
+
1
 điểm
N
e
ˆ
ˊ
u CFO
t
	​

 (Lưu chuyển ti
e
ˆ
ˋ
n thu
a
ˆ
ˋ
n từ HĐKD)>0⇒+1 điểm	

Hoạt động cốt lõi tạo ra tiền mặt dương, không phải lợi nhuận trên giấy.


	
𝐹
Δ
𝑅
𝑂
𝐴
F
ΔROA
	​

	
N
e
ˆ
ˊ
u 
𝑅
𝑂
𝐴
𝑡
>
𝑅
𝑂
𝐴
𝑡
−
1
⇒
+
1
 điểm
N
e
ˆ
ˊ
u ROA
t
	​

>ROA
t−1
	​

⇒+1 điểm	

Hiệu suất sinh lời trên tài sản đang trong xu hướng cải thiện.


	
𝐹
Accrual
F
Accrual
	​

	
N
e
ˆ
ˊ
u 
𝐶
𝐹
𝑂
𝑡
>
𝐿
𝑁
𝑆
𝑇
Thực
,
𝑡
⇒
+
1
 điểm
N
e
ˆ
ˊ
u CFO
t
	​

>LNST
Thực,t
	​

⇒+1 điểm	

Chặn đứng thủ thuật kế toán ghi nhận doanh thu ảo qua khoản phải thu.


2. Đòn bẩy & Thanh khoản (3 Điểm)	
𝐹
Δ
Lever
F
ΔLever
	​

	
N
e
ˆ
ˊ
u 
(
Nợ D
a
ˋ
i hạn
Tổng T
a
ˋ
i sản
)
𝑡
<
(
Nợ D
a
ˋ
i hạn
Tổng T
a
ˋ
i sản
)
𝑡
−
1
⇒
+
1
 điểm
N
e
ˆ
ˊ
u (
Tổng T
a
ˋ
i sản
Nợ D
a
ˋ
i hạn
	​

)
t
	​

<(
Tổng T
a
ˋ
i sản
Nợ D
a
ˋ
i hạn
	​

)
t−1
	​

⇒+1 điểm	

Giảm sự phụ thuộc vào đòn bẩy nợ vay dài hạn (Mã 338 / Mã 270).


	
𝐹
Δ
Liquid
F
ΔLiquid
	​

	
N
e
ˆ
ˊ
u 
Current Ratio
𝑡
=
(
TS Ng
a
˘
ˊ
n hạn
Nợ Ng
a
˘
ˊ
n hạn
)
𝑡
>
Current Ratio
𝑡
−
1
⇒
+
1
 điểm
N
e
ˆ
ˊ
u Current Ratio
t
	​

=(
Nợ Ng
a
˘
ˊ
n hạn
TS Ng
a
˘
ˊ
n hạn
	​

)
t
	​

>Current Ratio
t−1
	​

⇒+1 điểm	

Năng lực thanh toán nợ ngắn hạn (Mã 100 / Mã 310) được cải thiện.


	
𝐹
EqOffer
F
EqOffer
	​

	
N
e
ˆ
ˊ
u 
S
o
ˆ
ˊ
 lượng CP Lưu h
a
ˋ
nh
𝑡
≤
S
o
ˆ
ˊ
 lượng CP Lưu h
a
ˋ
nh
𝑡
−
1
 (trừ chia t
a
ˊ
ch/thưởng)
⇒
+
1
 điểm
N
e
ˆ
ˊ
u S
o
ˆ
ˊ
 lượng CP Lưu h
a
ˋ
nh
t
	​

≤S
o
ˆ
ˊ
 lượng CP Lưu h
a
ˋ
nh
t−1
	​

 (trừ chia t
a
ˊ
ch/thưởng)⇒+1 điểm	

Doanh nghiệp tự chủ vốn, không pha loãng cổ đông qua phát hành thêm/ESOP.


3. Hiệu quả Hoạt động (2 Điểm)	
𝐹
Δ
Margin
F
ΔMargin
	​

	
N
e
ˆ
ˊ
u 
Bi
e
ˆ
n Lợi nhuận Gộp
𝑡
>
Bi
e
ˆ
n Lợi nhuận Gộp
𝑡
−
1
⇒
+
1
 điểm
N
e
ˆ
ˊ
u Bi
e
ˆ
n Lợi nhuận Gộp
t
	​

>Bi
e
ˆ
n Lợi nhuận Gộp
t−1
	​

⇒+1 điểm	

Sức mạnh định giá bán (Pricing Power / Moat) tăng lên hoặc giá vốn giảm.


	
𝐹
Δ
Turn
F
ΔTurn
	​

	
N
e
ˆ
ˊ
u 
(
Doanh thu Thu
a
ˆ
ˋ
n
Tổng T
a
ˋ
i sản B
ı
ˋ
nh qu
a
ˆ
n
)
𝑡
>
(
Doanh thu Thu
a
ˆ
ˋ
n
Tổng T
a
ˋ
i sản B
ı
ˋ
nh qu
a
ˆ
n
)
𝑡
−
1
⇒
+
1
 điểm
N
e
ˆ
ˊ
u (
Tổng T
a
ˋ
i sản B
ı
ˋ
nh qu
a
ˆ
n
Doanh thu Thu
a
ˆ
ˋ
n
	​

)
t
	​

>(
Tổng T
a
ˋ
i sản B
ı
ˋ
nh qu
a
ˆ
n
Doanh thu Thu
a
ˆ
ˋ
n
	​

)
t−1
	​

⇒+1 điểm	

Vòng quay tài sản tăng, giải phóng hàng tồn kho và công nợ nhanh hơn.

  

Tổng điểm 
𝐹
-Score
=
∑
𝑖
=
1
9
𝐹
𝑖
F-Score=∑
i=1
9
	​

F
i
	​

 đạt từ 7 đến 9 điểm xác nhận doanh nghiệp có nền tảng tài chính lành mạnh vượt trội; đạt từ 4 đến 6 điểm phản ánh trạng thái tài chính trung bình ổn định; và từ 0 đến 3 điểm là tín hiệu cảnh báo suy thoái nghiêm trọng, như trường hợp thực tế của cổ phiếu QNS năm 2017 khi F-Score tụt xuống 3 điểm trước khi thị giá sụt giảm mạnh từ Quý 2/2017.   

Tầng 3: Mô hình Cảnh báo Phá sản Altman Z-Score Đa Biến thể (Z, Z', và Z'' Thị trường Mới nổi)

Một sai lầm kỹ thuật thường gặp ở các trang tài chính Việt Nam là áp dụng duy nhất công thức Altman Z-Score nguyên bản năm 1968 cho mọi doanh nghiệp. Trong thực tế, Edward Altman đã thiết kế ba phương trình riêng biệt tùy thuộc vào đặc thù ngành nghề và cấu trúc thị trường. Đặc biệt, đối với các doanh nghiệp phi sản xuất (thương mại, dịch vụ, công nghệ, bất động sản) và các doanh nghiệp hoạt động tại Thị trường Mới nổi (Emerging Markets), biến số vòng quay tài sản (
𝑋
5
=
Sales
/
Total Assets
X
5
	​

=Sales/Total Assets) bị loại bỏ hoàn toàn để tránh sự méo mó giữa các ngành, đồng thời phương trình được cộng thêm hằng số chuẩn hóa 
3
,
25
3,25 nhằm tương đương hóa điểm 0 với trái phiếu vỡ nợ hạng D (Default).   

Để lập trình mô-đun này vào Antigravity, hệ thống cần trích xuất năm tỷ số tài chính nền tảng, trong đó mẫu số Tổng Tài sản (
𝑇
𝐴
TA) khuyến nghị loại trừ Tài sản cố định vô hình (Mã 227) để đảm bảo tính bảo thủ. Biến số thứ nhất 
𝑋
1
=
(
T
a
ˋ
i sản Ng
a
˘
ˊ
n hạn M
a
˜
 100
−
Nợ Ng
a
˘
ˊ
n hạn M
a
˜
 310
)
/
𝑇
𝐴
X
1
	​

=(T
a
ˋ
i sản Ng
a
˘
ˊ
n hạn M
a
˜
 100−Nợ Ng
a
˘
ˊ
n hạn M
a
˜
 310)/TA đo lường thanh khoản ròng ngắn hạn; biến số thứ hai 
𝑋
2
=
(
LNST Chưa Ph
a
ˆ
n ph
o
ˆ
ˊ
i M
a
˜
 421
+
Qu
y
˜
 Đ
a
ˆ
ˋ
u tư Ph
a
ˊ
t triển M
a
˜
 418
)
/
𝑇
𝐴
X
2
	​

=(LNST Chưa Ph
a
ˆ
n ph
o
ˆ
ˊ
i M
a
˜
 421+Qu
y
˜
	​

 Đ
a
ˆ
ˋ
u tư Ph
a
ˊ
t triển M
a
˜
 418)/TA đo lường khả năng tích lũy lợi nhuận giữ lại qua thời gian so với nợ vay; và biến số thứ ba 
𝑋
3
=
𝐸
𝐵
𝐼
𝑇
/
𝑇
𝐴
X
3
	​

=EBIT/TA đo lường hiệu suất sinh lời thuần túy của tài sản trước ảnh hưởng của thuế và đòn bẩy tài chính. Biến số thứ tư có hai dạng: 
𝑋
4
𝑀
=
V
o
ˆ
ˊ
n h
o
ˊ
a Thị trường
/
Tổng Nợ Phải trả (M
a
˜
 300)
X
4M
	​

=V
o
ˆ
ˊ
n h
o
ˊ
a Thị trường/Tổng Nợ Phải trả (M
a
˜
 300) áp dụng cho mô hình Z sản xuất niêm yết, hoặc 
𝑋
4
𝐵
=
Gi
a
ˊ
 trị Sổ s
a
ˊ
ch V
o
ˆ
ˊ
n Chủ sở hữu (M
a
˜
 400)
/
Tổng Nợ Phải trả (M
a
˜
 300)
X
4B
	​

=Gi
a
ˊ
 trị Sổ s
a
ˊ
ch V
o
ˆ
ˊ
n Chủ sở hữu (M
a
˜
 400)/Tổng Nợ Phải trả (M
a
˜
 300) áp dụng cho mô hình 
𝑍
′
Z
′
 và 
𝑍
′
′
Z
′′
 nhằm loại bỏ nhiễu biến động giá cổ phiếu đầu cơ. Cuối cùng, biến số thứ năm 
𝑋
5
=
Doanh thu Thu
a
ˆ
ˋ
n
/
𝑇
𝐴
X
5
	​

=Doanh thu Thu
a
ˆ
ˋ
n/TA đo lường vòng quay tài sản và chỉ được sử dụng cho các doanh nghiệp sản xuất. Cấu trúc phân nhánh phương trình và ngưỡng cảnh báo phá sản theo ngành trên Antigravity được chuẩn hóa trong bảng dưới đây:   

Mô hình Altman	Nhóm Ngành Áp dụng tại Việt Nam	Phương trình Toán học Chuẩn hóa	Ngưỡng An toàn (Safe Zone)	Vùng Xám (Grey Zone)	Vùng Nguy hiểm (Distress)
Altman 
𝑍
Z (1968)	

Sản xuất công nghiệp niêm yết (Thép, Xi măng, Hóa chất, Ô tô, Chế biến).

	

𝑍
=
1
,
2
𝑋
1
+
1
,
4
𝑋
2
+
3
,
3
𝑋
3
+
0
,
6
𝑋
4
𝑀
+
1
,
0
𝑋
5
Z=1,2X
1
	​

+1,4X
2
	​

+3,3X
3
	​

+0,6X
4M
	​

+1,0X
5
	​


	

𝑍
>
2
,
99
Z>2,99

	

1
,
81
≤
𝑍
≤
2
,
99
1,81≤Z≤2,99

	

𝑍
<
1
,
81
Z<1,81


Altman 
𝑍
′
Z
′
 (Prime)	

Doanh nghiệp sản xuất chưa niêm yết, SME IPO hoặc thanh khoản rất thấp trên UPCoM.

	

𝑍
′
=
0
,
717
𝑋
1
+
0
,
847
𝑋
2
+
3
,
107
𝑋
3
+
0
,
420
𝑋
4
𝐵
+
0
,
998
𝑋
5
Z
′
=0,717X
1
	​

+0,847X
2
	​

+3,107X
3
	​

+0,420X
4B
	​

+0,998X
5
	​


	

𝑍
′
>
2
,
90
Z
′
>2,90

	

1
,
23
≤
𝑍
′
≤
2
,
90
1,23≤Z
′
≤2,90

	

𝑍
′
<
1
,
23
Z
′
<1,23


Altman 
𝑍
EM
′
′
Z
EM
′′
	​

 (Emerging Markets)	

Phi sản xuất, Bán lẻ, FMCG, Công nghệ (IT), Y tế, Dịch vụ, BĐS tại Thị trường Mới nổi.

	

𝑍
EM
′
′
=
3
,
25
+
6
,
56
𝑋
1
+
3
,
26
𝑋
2
+
6
,
72
𝑋
3
+
1
,
05
𝑋
4
𝐵
Z
EM
′′
	​

=3,25+6,56X
1
	​

+3,26X
2
	​

+6,72X
3
	​

+1,05X
4B
	​


	

𝑍
EM
′
′
>
2
,
60
Z
EM
′′
	​

>2,60

	

1
,
10
≤
𝑍
EM
′
′
≤
2
,
60
1,10≤Z
EM
′′
	​

≤2,60

	

𝑍
EM
′
′
<
1
,
10
Z
EM
′′
	​

<1,10

  

Hệ thống cần thiết lập điều kiện ngoại lệ (Exception Rule): tuyệt đối không chạy Altman Z-Score cho nhóm Ngân hàng, Chứng khoán và Bảo hiểm vì đặc thù đòn bẩy nợ của định chế tài chính hoàn toàn khác với doanh nghiệp phi tài chính.   

3. Hệ thống Công thức Định giá Lõi của Warren Buffett và Phil Town

Khi một cổ phiếu vượt qua các bộ lọc sức khỏe tài chính hoặc được gắn nhãn rủi ro tương ứng, hệ thống Antigravity sẽ kích hoạt bộ tứ công thức định giá hội tụ của Phil Town và Warren Buffett.   

Công thức 1: Giá Hợp lý (Sticker Price) và Giá Mua Biên An toàn (MOS Price)

Phương pháp Sticker Price của Phil Town hoạt động theo cơ chế tính ngược từ giá bán kỳ vọng ở năm thứ 10 về thời điểm hiện tại. Để tránh sự lạc quan thái quá khi phóng chiếu tương lai, thuật toán bắt buộc áp dụng nguyên tắc lấy giá trị thấp hơn (Conservative Minimum Rule) ở cả hai biến số tốc độ tăng trưởng và hệ số P/E. Trước hết, hệ thống xác định tốc độ tăng trưởng bảo thủ (
𝑔
Rule1
g
Rule1
	​

) bằng cách lấy giá trị nhỏ nhất giữa tốc độ tăng trưởng vốn chủ sở hữu lịch sử (
𝐶
𝐴
𝐺
𝑅
BVPS
CAGR
BVPS
	​

) và tốc độ tăng trưởng EPS dự phóng của giới phân tích, đồng thời chặn trần theo ngành:   

𝑔
Rule1
=
min
⁡
(
𝐶
𝐴
𝐺
𝑅
BVPS (Lịch sử 5-10 n
a
˘
m)
,
𝑔
EPS Dự ph
o
ˊ
ng (Analysts)
,
𝑔
Tr
a
ˆ
ˋ
n Ng
a
ˋ
nh
)
g
Rule1
	​

=min(CAGR
BVPS (Lịch sử 5-10 n
a
˘
m)
	​

,g
EPS Dự ph
o
ˊ
ng (Analysts)
	​

,g
Tr
a
ˆ
ˋ
n Ng
a
ˋ
nh
	​

)

Trong kiểm nghiệm mẫu của Phil Town, ngay cả khi tốc độ tăng trưởng vốn chủ sở hữu lịch sử lên tới 
110
,
1
%
/
n
a
˘
m
110,1%/n
a
˘
m nhưng giới phân tích dự báo tăng trưởng EPS tương lai là 
20
,
0
%
/
n
a
˘
m
20,0%/n
a
˘
m, thuật toán sẽ chọn mức thấp hơn là 
20
,
0
%
20,0%. Tại thị trường Việt Nam, để ngăn chặn sai số hàm mũ trong 10 năm, hệ thống Antigravity cần đặt thêm một ngưỡng trần cứng (
𝑔
Tr
a
ˆ
ˋ
n Ng
a
ˋ
nh
≤
25
%
/
n
a
˘
m
g
Tr
a
ˆ
ˋ
n Ng
a
ˋ
nh
	​

≤25%/n
a
˘
m). Tiếp theo, thuật toán phóng chiếu EPS thực nhận vào năm thứ 10 và xác định hệ số P/E tương lai bảo thủ (
𝑃
𝐸
Future
PE
Future
	​

) dựa trên quy tắc P/E mặc định tối đa bằng hai lần tốc độ tăng trưởng (
2
×
𝑔
Rule1
×
100
2×g
Rule1
	​

×100) so sánh với P/E trung bình lịch sử 5 năm của cổ phiếu:   

𝐸
𝑃
𝑆
10
=
𝐸
𝑃
𝑆
Thực (TTM)
×
(
1
+
𝑔
Rule1
)
10
EPS
10
	​

=EPS
Thực (TTM)
	​

×(1+g
Rule1
	​

)
10
𝑃
𝐸
Future
=
min
⁡
(
2
×
(
𝑔
Rule1
×
100
)
,
𝑃
𝐸
Trung b
ı
ˋ
nh Lịch sử 5 n
a
˘
m
,
𝑃
𝐸
Tr
a
ˆ
ˋ
n Thị trường VN
)
PE
Future
	​

=min(2×(g
Rule1
	​

×100),PE
Trung b
ı
ˋ
nh Lịch sử 5 n
a
˘
m
	​

,PE
Tr
a
ˆ
ˋ
n Thị trường VN
	​

)

Sau khi có 
𝐸
𝑃
𝑆
10
EPS
10
	​

 và 
𝑃
𝐸
Future
PE
Future
	​

 (với 
𝑃
𝐸
Tr
a
ˆ
ˋ
n Thị trường VN
PE
Tr
a
ˆ
ˋ
n Thị trường VN
	​

 khuyến nghị giới hạn ở mức 
25
x
−
30
x
25x−30x do mặt bằng lãi suất nội tệ), hệ thống tính Giá Thị trường Tương lai ở năm thứ 10 (
𝑃
10
P
10
	​

), chiết khấu về hiện tại theo mức 
𝑀
𝐴
𝑅
𝑅
=
15
%
/
n
a
˘
m
MARR=15%/n
a
˘
m để thu được Giá Hợp lý (
𝑃
Sticker
P
Sticker
	​

), và chia đôi để xác lập Giá Mua An toàn (
𝑃
MOS
P
MOS
	​

):   

𝑃
10
=
𝐸
𝑃
𝑆
10
×
𝑃
𝐸
Future
P
10
	​

=EPS
10
	​

×PE
Future
	​

𝑃
Sticker
=
𝑃
10
(
1
+
𝑀
𝐴
𝑅
𝑅
)
10
=
𝑃
10
(
1
+
0
,
15
)
10
≈
𝑃
10
4
,
0456
P
Sticker
	​

=
(1+MARR)
10
P
10
	​

	​

=
(1+0,15)
10
P
10
	​

	​

≈
4,0456
P
10
	​

	​

𝑃
MOS
=
𝑃
Sticker
×
(
1
−
𝑀
𝑂
𝑆
)
=
𝑃
Sticker
×
50
%
P
MOS
	​

=P
Sticker
	​

×(1−MOS)=P
Sticker
	​

×50%

Với bộ tham số kiểm thử chuẩn (
𝐸
𝑃
𝑆
0
=
1
,
03
 USD
EPS
0
	​

=1,03 USD, 
𝑔
=
20
%
g=20%, 
𝑃
𝐸
Lịch sử
=
101
PE
Lịch sử
	​

=101), thuật toán cho ra 
𝐸
𝑃
𝑆
10
=
1
,
03
×
(
1
,
20
)
10
=
6
,
38
 USD
EPS
10
	​

=1,03×(1,20)
10
=6,38 USD; hệ số 
𝑃
𝐸
Future
=
min
⁡
(
40
,
101
)
=
40
PE
Future
	​

=min(40,101)=40; giá tương lai 
𝑃
10
=
6
,
38
×
40
=
255
,
20
 USD
P
10
	​

=6,38×40=255,20 USD; suy ra 
𝑃
Sticker
=
255
,
20
/
(
1
,
15
)
10
=
63
,
08
 USD
P
Sticker
	​

=255,20/(1,15)
10
=63,08 USD và 
𝑃
MOS
=
31
,
54
 USD
P
MOS
	​

=31,54 USD. Phân tích toán học sâu hơn cho thấy việc kết hợp chiết khấu 
15
%
/
n
a
˘
m
15%/n
a
˘
m và biên an toàn 
50
%
50% tạo ra một màng lọc cực kỳ khắt khe: nếu quy đổi về mô hình DCF hai giai đoạn, một công ty tăng trưởng 
0
%
0% chỉ xứng đáng được mua ở mức 
𝑃
/
𝐸
=
3
,
33
x
P/E=3,33x; tăng trưởng 
10
%
/
n
a
˘
m
10%/n
a
˘
m trong 5 năm rồi 
2
%
2% vĩnh viễn tương ứng 
𝑃
/
𝐸
=
5
,
33
x
P/E=5,33x; tăng trưởng 
22
%
/
n
a
˘
m
22%/n
a
˘
m trong 5 năm rồi 
5
%
5% vĩnh viễn tương ứng 
𝑃
/
𝐸
=
10
,
0
x
P/E=10,0x; và chỉ những siêu cổ phiếu tăng trưởng 
25
%
/
n
a
˘
m
25%/n
a
˘
m suốt 10 năm rồi 
5
%
5% vĩnh viễn mới có giá mua MOS ở mức 
𝑃
/
𝐸
=
20
,
0
x
P/E=20,0x.   

Công thức 2: Dòng tiền Chủ sở hữu (Owner Earnings) và Giá 10 Cap (10 Cap Price)

Phương pháp 10 Cap xuất phát từ tư duy đầu tư bất động sản cho thuê của Warren Buffett và Phil Town: nếu mua đứt toàn bộ doanh nghiệp và không tính đến yếu tố tăng trưởng, dòng tiền ròng chảy về túi chủ sở hữu mỗi năm phải đạt tối thiểu 
10
%
10% trên tổng vốn bỏ ra, tương đương hoàn vốn trong 10 năm ở trạng thái tĩnh. Thay vì dùng lợi nhuận kế toán, Buffett định nghĩa Dòng tiền Chủ sở hữu (Owner Earnings) là lượng tiền mặt thực sự có thể rút ra khỏi doanh nghiệp mà không làm suy giảm năng lực cạnh tranh hay sản lượng hiện tại.   

Tại Việt Nam, nhiều doanh nghiệp đang trong giai đoạn mở rộng nhà máy (như HPG đầu tư khu liên hợp Dung Quất) sẽ có tổng chi phí đầu tư tài sản cố định (Total CapEx) rất lớn, khiến Free Cash Flow truyền thống bị âm. Do đó, thuật toán trên Antigravity cần tách biệt CapEx Bảo trì (Maintenance CapEx) khỏi CapEx Mở rộng (Growth CapEx) và trừ đi khoản trích Quỹ khen thưởng phúc lợi:   

Owner Earnings
=
𝐶
𝐹
𝑂
−
CapEx
Bảo tr
ı
ˋ
−
Tr
ı
ˊ
ch Qu
y
˜
 KTPL (TK 353)
Owner Earnings=CFO−CapEx
Bảo tr
ı
ˋ
	​

−Tr
ı
ˊ
ch Qu
y
˜
	​

 KTPL (TK 353)

Nếu doanh nghiệp không thuyết minh chi tiết 
CapEx
Bảo tr
ı
ˋ
CapEx
Bảo tr
ı
ˋ
	​

, thuật toán có thể ước lượng biến này thông qua công thức bảo thủ 
CapEx
Bảo tr
ı
ˋ
≈
min
⁡
(
Tổng CapEx
,
Chi ph
ı
ˊ
 Kh
a
ˆ
ˊ
u hao TSCĐ trong k
y
ˋ
)
CapEx
Bảo tr
ı
ˋ
	​

≈min(Tổng CapEx,Chi ph
ı
ˊ
 Kh
a
ˆ
ˊ
u hao TSCĐ trong k
y
ˋ
	​

). Khi đó, công thức định giá 10 Cap trên mỗi cổ phiếu được xác định bằng cách chia Owner Earnings trên mỗi cổ phiếu cho tỷ suất yêu cầu 
10
%
10%:   

𝑃
10Cap
=
Owner Earnings tr
e
ˆ
n m
o
ˆ
˜
i Cổ phi
e
ˆ
ˊ
u
10
%
=
10
×
(
Owner Earnings
S
o
ˆ
ˊ
 CP Pha lo
a
˜
ng
)
P
10Cap
	​

=
10%
Owner Earnings tr
e
ˆ
n m
o
ˆ
˜
i Cổ phi
e
ˆ
ˊ
u
	​

=10×(
S
o
ˆ
ˊ
 CP Pha lo
a
˜
ng
Owner Earnings
	​

)

Ví dụ thực tế từ Phil Town cho thấy một cổ phiếu tạo ra 
8
 USD
8 USD (hoặc 
8.000
 VNĐ
8.000 VNĐ) Owner Earnings trên mỗi cổ phiếu sẽ có giá mua 10 Cap chính xác là 
8
/
10
%
=
80
 USD
8/10%=80 USD (hoặc 
80.000
 VNĐ
80.000 VNĐ).   

Công thức 3: Thời gian Hoàn vốn (Payback Time Price)

Trong khi 10 Cap bỏ qua yếu tố tăng trưởng, phương pháp Payback Time trả lời câu hỏi của quỹ đầu tư tư nhân (Private Equity): nếu mua toàn bộ doanh nghiệp ở mức giá hiện tại và cộng dồn dòng tiền tự do tăng trưởng hàng năm, mất bao nhiêu năm để nhà đầu tư thu hồi đủ 
100
%
100% vốn gốc. Trên thị trường niêm yết đại chúng, nhà đầu tư thường chấp nhận trả mức giá tương đương 16 năm dòng tiền tự do; do đó, để tích hợp biên an toàn 
50
%
50%, Phil Town đặt ngưỡng trần mua tối đa là 8 năm (
𝑁
Max
=
8
N
Max
	​

=8).   

Theo định nghĩa của Rule #1, dòng tiền tự do được phóng chiếu tăng trưởng kép trong 8 năm tiếp theo để xác định tổng giá trị thu hồi vốn. Thay vì dùng vòng lặp tốn tài nguyên tính toán, lập trình viên có thể nhúng trực tiếp công thức tổng cấp số nhân đóng (Closed-Form Geometric Series) vào Antigravity để tính chính xác Giá Mua Payback Time Tối đa (
𝑃
Payback
P
Payback
	​

) tại ngưỡng 
𝑁
=
8
N=8 năm:   

𝑃
Payback (8 n
a
˘
m)
=
∑
𝑛
=
1
8
𝐹
𝐶
𝐹
Thực
,
0
×
(
1
+
𝑔
Rule1
)
𝑛
=
𝐹
𝐶
𝐹
Thực
,
0
×
(
1
+
𝑔
Rule1
)
×
[
(
1
+
𝑔
Rule1
)
8
−
1
𝑔
Rule1
]
P
Payback (8 n
a
˘
m)
	​

=
n=1
∑
8
	​

FCF
Thực,0
	​

×(1+g
Rule1
	​

)
n
=FCF
Thực,0
	​

×(1+g
Rule1
	​

)×[
g
Rule1
	​

(1+g
Rule1
	​

)
8
−1
	​

]

Ngược lại, để tính Số năm Hoàn vốn Thực tế (
𝑁
Payback
N
Payback
	​

) tại mức thị giá hiện tại (
𝑃
Market
P
Market
	​

) nhằm hiển thị lên giao diện người dùng, công thức logarit nghịch đảo là:   

𝑁
Payback
=
ln
⁡
(
1
+
𝑃
Market
×
𝑔
Rule1
𝐹
𝐶
𝐹
Thực
,
0
×
(
1
+
𝑔
Rule1
)
)
ln
⁡
(
1
+
𝑔
Rule1
)
N
Payback
	​

=
ln(1+g
Rule1
	​

)
ln(1+
FCF
Thực,0
	​

×(1+g
Rule1
	​

)
P
Market
	​

×g
Rule1
	​

	​

)
	​


Chẳng hạn, với một công ty có 
𝐹
𝐶
𝐹
0
=
5
 USD
FCF
0
	​

=5 USD, tốc độ tăng trưởng 
𝑔
=
10
%
/
n
a
˘
m
g=10%/n
a
˘
m và đang giao dịch ở mức giá 
𝑃
Market
=
40
 USD
P
Market
	​

=40 USD, tổng dòng tiền thu hồi sẽ khớp hoàn toàn với vốn đầu tư ban đầu sau 6 năm — nằm trọn trong vùng mua lý tưởng (dưới 8 năm) của Rule #1.   

Công thức 4: DCF Hai Giai đoạn của Buffett và Giá trị Xác sống (Zombie Value)

Để hoàn thiện góc nhìn Giá trị Nội tại của Warren Buffett và kiểm chứng chéo với kịch bản xấu nhất của Phil Town, hệ thống cần tính toán đồng thời Giá trị Xác sống (Zombie Value) và Giá trị Nội tại DCF Hai Giai đoạn. Giá trị Xác sống định giá doanh nghiệp trong kịch bản bi quan nhất khi tốc độ tăng trưởng ngừng lại hoàn toàn (
𝑔
=
0
%
g=0%) mãi mãi (tương đương mô hình Tăng trưởng Gordon với tăng trưởng bằng không), cộng với lượng tiền mặt ròng hiện có trên mỗi cổ phiếu:   

𝑃
Zombie
=
Owner Earnings tr
e
ˆ
n m
o
ˆ
˜
i CP
𝐾
𝑒
+
Ti
e
ˆ
ˋ
n mặt R
o
ˋ
ng tr
e
ˆ
n m
o
ˆ
˜
i CP
P
Zombie
	​

=
K
e
	​

Owner Earnings tr
e
ˆ
n m
o
ˆ
˜
i CP
	​

+Ti
e
ˆ
ˋ
n mặt R
o
ˋ
ng tr
e
ˆ
n m
o
ˆ
˜
i CP

Song song đó, mô hình Chiết khấu Dòng tiền Hai Giai đoạn (2-Stage Intrinsic DCF) phóng chiếu dòng tiền tăng trưởng ở tốc độ 
𝑔
Rule1
g
Rule1
	​

 trong 10 năm đầu và tăng trưởng ổn định ở mức 
𝑔
Terminal
=
3
%
−
4
%
g
Terminal
	​

=3%−4% (tương đương lạm phát mục tiêu dài hạn) từ năm thứ 11 trở đi, sau đó chiết khấu về hiện tại theo chi phí vốn 
𝐾
𝑒
K
e
	​

 (hoặc 
𝑊
𝐴
𝐶
𝐶
WACC):   

𝐼
𝑉
DCF
=
∑
𝑡
=
1
10
𝐹
𝐶
𝐹
0
×
(
1
+
𝑔
Rule1
)
𝑡
(
1
+
𝐾
𝑒
)
𝑡
+
𝐹
𝐶
𝐹
10
×
(
1
+
𝑔
Terminal
)
(
𝐾
𝑒
−
𝑔
Terminal
)
×
(
1
+
𝐾
𝑒
)
10
IV
DCF
	​

=
t=1
∑
10
	​

(1+K
e
	​

)
t
FCF
0
	​

×(1+g
Rule1
	​

)
t
	​

+
(K
e
	​

−g
Terminal
	​

)×(1+K
e
	​

)
10
FCF
10
	​

×(1+g
Terminal
	​

)
	​

4. Ma trận Phân hóa Công thức Định giá theo Đặc thù Ngành tại Việt Nam

Một công cụ định giá thông minh trên Antigravity phải hoạt động theo cơ chế định tuyến tự động (Sector Routing Engine): ngay khi người dùng nhập mã cổ phiếu, hệ thống truy xuất mã ngành ICB (Industry Classification Benchmark) và kích hoạt bộ công thức cũng như trọng số riêng biệt cho ngành đó.   

Phân nhóm Ngành (ICB)	Cổ phiếu Đại diện (VN)	Tại sao Công thức Chung Thất bại?	Bộ Công thức Định giá Chuẩn hóa trên Antigravity	Trọng số Hội tụ Khuyến nghị
1. Sản xuất, Bán lẻ, Tiêu dùng, Công nghệ	VNM, FPT, MWG, PNJ, DGC, HPG	

Nhóm chu kỳ (Thép, Hóa chất) có EPS đỉnh chu kỳ rất cao và P/E rất thấp, dễ tạo bẫy giá trị chu kỳ.

	

Sticker Price & MOS (50%); Payback Time (
≤
8
≤8 năm); 10 Cap (Owner Earnings); 2-Stage DCF (chuẩn hóa EPS trung bình 5 năm cho ngành chu kỳ).

	

30% Sticker MOS; 25% Payback Time; 25% 10 Cap; 20% 2-Stage DCF.


2. Bất động sản Dân dụng & KCN	VHM, NLG, KDH, KBC, IDC, SIP	

Doanh thu/EPS ghi nhận dồn cục khi bàn giao nhà; FCF âm nặng khi gom quỹ đất dù giá trị thực tăng.

	

RNAV / SOTP (Đánh giá lại Hàng tồn kho & Chiết khấu dòng tiền từng dự án); P/B Mục tiêu điều chỉnh Người mua trả tiền trước.

	

70% RNAV (Chiết khấu MOS); 30% Justified P/B Dự án.


3. Ngân hàng, Chứng khoán, Bảo hiểm	VCB, ACB, MBB, TCB, SSI, BVH	

Nợ vay là nguyên liệu kinh doanh; không có khái niệm Vốn lưu động hay FCF/CapEx truyền thống.

	

Residual Income (Thu nhập thặng dư); BVPS Compounding Sticker Price (Biến thể Rule #1 theo P/B & ROE); Justified P/B.

	

40% Residual Income; 40% BVPS Sticker MOS; 20% Justified P/B.


4. Hạ tầng, Điện, Nước, Cảng biển	REE, BWE, NT2, GMD, ACV, PHP	

Tài sản cố định cực lớn, khấu hao kế toán làm méo mó EPS trong khi dòng tiền mặt thực rất dồi dào.

	

10 Cap (Owner Earnings); 2-Stage FCFF / EV/EBITDA; Chiết khấu Cổ tức (DDM / GGM).

	

40% 10 Cap Owner Earnings; 35% FCFF DCF; 25% DDM / GGM.

  
Nhóm 1: Ngành Sản xuất, Tiêu dùng, Bán lẻ và Công nghệ (Biến thể Phẳng và Biến thể Chu kỳ)

Đối với các doanh nghiệp tăng trưởng bền vững có con hào thương hiệu hoặc công nghệ rõ nét (như FPT, VNM, PNJ), bộ tứ công thức của Phil Town và Buffett hoạt động với hiệu suất cao nhất. Tuy nhiên, đối với nhóm ngành Sản xuất Chu kỳ (Thép như HPG, HSG; Hóa chất và Phân bón như DGC, DPM; Thủy sản như VHC), nếu thuật toán lấy 
𝐸
𝑃
𝑆
TTM
EPS
TTM
	​

 tại đỉnh chu kỳ giá hàng hóa để chạy Sticker Price trong 10 năm, kết quả định giá sẽ bị thổi phồng nghiêm trọng.   

Để khắc phục hiện tượng này, Antigravity phải thay thế 
𝐸
𝑃
𝑆
TTM
EPS
TTM
	​

 và 
𝐹
𝐶
𝐹
TTM
FCF
TTM
	​

 bằng Lợi nhuận Chuẩn hóa Giữa Chu kỳ (Normalized Mid-Cycle EPS & FCF) trước khi đưa vào công thức Sticker Price và 10 Cap:   

𝐸
𝑃
𝑆
Normalized
=
BVPS
Hiện tại
×
𝑅
𝑂
𝐸
Trung b
ı
ˋ
nh Chu k
y
ˋ
 5–7 n
a
˘
m
EPS
Normalized
	​

=BVPS
Hiện tại
	​

×ROE
Trung b
ı
ˋ
nh Chu k
y
ˋ
	​

 5–7 n
a
˘
m
	​

𝐹
𝐶
𝐹
Normalized
=
Doanh thu
Hiện tại
×
Bi
e
ˆ
n FCF
Trung b
ı
ˋ
nh Chu k
y
ˋ
 5–7 n
a
˘
m
FCF
Normalized
	​

=Doanh thu
Hiện tại
	​

×Bi
e
ˆ
n FCF
Trung b
ı
ˋ
nh Chu k
y
ˋ
	​

 5–7 n
a
˘
m
	​


Cách tiếp cận này giúp hệ thống tự động hạ định giá khi cổ phiếu chu kỳ đang ở đỉnh lợi nhuận và nâng định giá để nhận diện cơ hội mua khi doanh nghiệp đang ở đáy chu kỳ nhưng bảng cân đối kế toán vẫn nằm trong vùng an toàn (
𝑍
-Score
>
2
,
99
Z-Score>2,99).   

Nhóm 2: Ngành Bất động sản (Dân dụng và Khu Công nghiệp) — Mô hình RNAV (Revalued Net Asset Value)

Trong chế độ kế toán Việt Nam, doanh nghiệp phát triển bất động sản chỉ được phép ghi nhận doanh thu và lợi nhuận lên Báo cáo kết quả kinh doanh khi đã bàn giao bất động sản cho khách hàng, bất chấp việc dự án đã bán hết và thu tiền mặt về từ nhiều năm trước. Do đó, định giá cổ phiếu bất động sản bằng P/E hay tăng trưởng EPS ngắn hạn là không phù hợp; phương pháp tiêu chuẩn bắt buộc là Định giá lại Giá trị Tài sản Ròng (RNAV / Sum-of-the-Parts - SOTP).   

Trên Bảng cân đối kế toán bất động sản, hai khoản mục trọng yếu nhất là Hàng tồn kho (Mã số 140) kết hợp Chi phí xây dựng cơ bản dở dang dài hạn (Mã số 242) — nơi ghi nhận quỹ đất theo giá vốn lịch sử — và Người mua trả tiền trước ngắn hạn/dài hạn (Mã số 312 và 332) — nơi phản ánh lượng tiền mặt khách hàng đã thanh toán theo tiến độ dự án. Hệ thống Antigravity định giá từng dự án 
𝑖
i bằng phương pháp chiết khấu dòng tiền dự án (NPV dự án) với tỷ suất chiết khấu là 
𝑊
𝐴
𝐶
𝐶
WACC của doanh nghiệp, sau đó cộng phần chênh lệch đánh giá lại vào Vốn chủ sở hữu sổ sách để thu được tổng RNAV:   

𝑁
𝑃
𝑉
Dự 
a
ˊ
n 
𝑖
=
∑
𝑡
=
1
𝑇
𝑖
D
o
ˋ
ng ti
e
ˆ
ˋ
n Thu
a
ˆ
ˋ
n Dự 
a
ˊ
n
𝑖
,
𝑡
(
1
+
𝑊
𝐴
𝐶
𝐶
)
𝑡
NPV
Dự 
a
ˊ
n i
	​

=
t=1
∑
T
i
	​

	​

(1+WACC)
t
D
o
ˋ
ng ti
e
ˆ
ˋ
n Thu
a
ˆ
ˋ
n Dự 
a
ˊ
n
i,t
	​

	​

RNAV
Tổng
=
V
o
ˆ
ˊ
n Chủ sở hữu Sổ s
a
ˊ
ch (M
a
˜
 400)
+
∑
𝑖
=
1
𝑘
(
𝑁
𝑃
𝑉
Dự 
a
ˊ
n 
𝑖
−
Gi
a
ˊ
 trị Ghi sổ Dự 
a
ˊ
n 
𝑖
)
RNAV
Tổng
	​

=V
o
ˆ
ˊ
n Chủ sở hữu Sổ s
a
ˊ
ch (M
a
˜
 400)+
i=1
∑
k
	​

(NPV
Dự 
a
ˊ
n i
	​

−Gi
a
ˊ
 trị Ghi sổ Dự 
a
ˊ
n i)

Trong trường hợp công cụ chạy tự động hàng loạt (Screening Mode) khi người dùng chưa nhập bảng dòng tiền chi tiết của từng lô đất, Antigravity sử dụng Công thức RNAV Định lượng Nhanh (Automated Proxy RNAV) trích xuất trực tiếp từ BCTC:   

RNAV
Proxy
=
VCSH (M
a
˜
 400)
+
[
Người mua trả ti
e
ˆ
ˋ
n trước (M
a
˜
 312 + 332)
×
Bi
e
ˆ
n LN R
o
ˋ
ng TB 3 n
a
˘
m
]
+
[
(
H
a
ˋ
ng t
o
ˆ
ˋ
n kho (M
a
˜
 140)
−
Người mua trả ti
e
ˆ
ˋ
n trước
)
×
𝜆
]
RNAV
Proxy
	​

=VCSH (M
a
˜
 400)+[Người mua trả ti
e
ˆ
ˋ
n trước (M
a
˜
 312 + 332)×Bi
e
ˆ
n LN R
o
ˋ
ng TB 3 n
a
˘
m]+[(H
a
ˋ
ng t
o
ˆ
ˋ
n kho (M
a
˜
 140)−Người mua trả ti
e
ˆ
ˋ
n trước)×λ]

Trong công thức trên, hệ số thặng dư quỹ đất 
𝜆
λ được thiết lập dựa trên chất lượng pháp lý và lịch sử sinh lời của quỹ đất (mặc định 
𝜆
=
0
,
20
λ=0,20 đến 
0
,
50
0,50 đối với doanh nghiệp có lịch sử 
𝑅
𝑂
𝐼
𝐶
≥
10
%
ROIC≥10%). Sau khi tính được RNAV trên mỗi cổ phiếu, áp dụng triết lý Biên an toàn của Phil Town và Buffett, Giá Mua Bất động sản An toàn được xác định bằng cách chiết khấu tỷ lệ rủi ro thanh khoản và pháp lý (
𝑀
𝑂
𝑆
BĐS
=
30
%
−
50
%
MOS
BĐS
	​

=30%−50%):   

𝑃
Buy (BĐS)
=
RNAV
Tổng
S
o
ˆ
ˊ
 CP Pha lo
a
˜
ng
×
(
1
−
𝑀
𝑂
𝑆
BĐS
)
P
Buy (BĐS)
	​

=
S
o
ˆ
ˊ
 CP Pha lo
a
˜
ng
RNAV
Tổng
	​

	​

×(1−MOS
BĐS
	​

)
Nhóm 3: Ngành Ngân hàng, Chứng khoán và Bảo hiểm — Mô hình Thu nhập Thặng dư (Residual Income) và BVPS Sticker Price

Đối với các định chế tài chính, đặc biệt là Ngân hàng thương mại, tiền gửi của khách hàng và vốn vay liên ngân hàng chính là nguyên liệu đầu vào để sản xuất ra tín dụng. Do đó, mọi công thức dựa trên 
𝐸
𝐵
𝐼
𝑇
EBIT, 
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
EBITDA, Vốn lưu động hay 
𝐹
𝐶
𝐹
FCF đều phải bị vô hiệu hóa. Trường phái giá trị của Buffett định giá ngân hàng dựa trên chất lượng tài sản, khả năng sinh lời trên vốn chủ sở hữu (
𝑅
𝑂
𝐸
ROE) và tốc độ tăng trưởng Giá trị Sổ sách (
𝐵
𝑉
𝑃
𝑆
BVPS).   

Antigravity cần triển khai song song hai công thức chuyên biệt cho nhóm ngành này. Phương pháp thứ nhất là Mô hình Thu nhập Thặng dư (Residual Income Model - RI): một ngân hàng chỉ thực sự tạo ra giá trị gia tăng cho cổ đông khi tỷ suất sinh lời thực tế trên vốn chủ sở hữu (
𝑅
𝑂
𝐸
Thực
ROE
Thực
	​

, sau khi đã trừ trích lập Quỹ khen thưởng phúc lợi TK 353) lớn hơn Chi phí Vốn Chủ sở hữu (
𝐾
𝑒
K
e
	​

) mà nhà đầu tư yêu cầu. Thu nhập thặng dư năm 
𝑡
t được xác định bởi 
𝑅
𝐼
𝑡
=
(
𝑅
𝑂
𝐸
Thực
,
𝑡
−
𝐾
𝑒
)
×
𝐵
𝑉
𝑃
𝑆
𝑡
−
1
RI
t
	​

=(ROE
Thực,t
	​

−K
e
	​

)×BVPS
t−1
	​

, từ đó suy ra Giá trị Nội tại theo mô hình RI 10 năm kết hợp giá trị cuối kỳ:   

𝐼
𝑉
Bank (RI)
=
𝐵
𝑉
𝑃
𝑆
0
+
∑
𝑡
=
1
10
(
𝑅
𝑂
𝐸
Thực
,
𝑡
−
𝐾
𝑒
)
×
𝐵
𝑉
𝑃
𝑆
𝑡
−
1
(
1
+
𝐾
𝑒
)
𝑡
+
(
𝑅
𝑂
𝐸
Terminal
−
𝐾
𝑒
)
×
𝐵
𝑉
𝑃
𝑆
10
(
𝐾
𝑒
−
𝑔
Terminal
)
×
(
1
+
𝐾
𝑒
)
10
IV
Bank (RI)
	​

=BVPS
0
	​

+
t=1
∑
10
	​

(1+K
e
	​

)
t
(ROE
Thực,t
	​

−K
e
	​

)×BVPS
t−1
	​

	​

+
(K
e
	​

−g
Terminal
	​

)×(1+K
e
	​

)
10
(ROE
Terminal
	​

−K
e
	​

)×BVPS
10
	​

	​


Phương pháp thứ hai là Biến thể Rule #1 Sticker Price theo Giá trị Sổ sách và P/B (BVPS Compounding Method). Thay vì phóng chiếu EPS và nhân với P/E, thuật toán phóng chiếu Giá trị Sổ sách trên mỗi cổ phiếu (
𝐵
𝑉
𝑃
𝑆
BVPS) sau 10 năm theo tốc độ tăng trưởng vốn tự có bền vững 
𝑔
BV
=
𝑅
𝑂
𝐸
Thực
×
(
1
−
Tỷ lệ Chi trả Cổ tức Ti
e
ˆ
ˋ
n mặt
)
g
BV
	​

=ROE
Thực
	​

×(1−Tỷ lệ Chi trả Cổ tức Ti
e
ˆ
ˋ
n mặt), sau đó nhân với hệ số 
𝑃
/
𝐵
P/B hợp lý (Justified P/B) và chiết khấu về hiện tại ở mức 
𝑀
𝐴
𝑅
𝑅
=
15
%
MARR=15%:   

𝐵
𝑉
𝑃
𝑆
10
=
𝐵
𝑉
𝑃
𝑆
0
×
(
1
+
𝑔
BV
)
10
BVPS
10
	​

=BVPS
0
	​

×(1+g
BV
	​

)
10
𝑃
𝐵
Future
=
min
⁡
(
PB
Trung b
ı
ˋ
nh Lịch sử 5 n
a
˘
m
,
PB
Justified
=
𝑅
𝑂
𝐸
Thực
−
𝑔
Terminal
𝐾
𝑒
−
𝑔
Terminal
)
PB
Future
	​

=min(PB
Trung b
ı
ˋ
nh Lịch sử 5 n
a
˘
m
	​

,PB
Justified
	​

=
K
e
	​

−g
Terminal
	​

ROE
Thực
	​

−g
Terminal
	​

	​

)
𝑃
Sticker (Bank)
=
𝐵
𝑉
𝑃
𝑆
10
×
𝑃
𝐵
Future
(
1
+
0
,
15
)
10
+
PV
(
Cổ tức Ti
e
ˆ
ˋ
n mặt 10 n
a
˘
m
)
P
Sticker (Bank)
	​

=
(1+0,15)
10
BVPS
10
	​

×PB
Future
	​

	​

+PV(Cổ tức Ti
e
ˆ
ˋ
n mặt 10 n
a
˘
m)
𝑃
MOS (Bank)
=
𝑃
Sticker (Bank)
×
(
1
−
𝑀
𝑂
𝑆
Bank
)
P
MOS (Bank)
	​

=P
Sticker (Bank)
	​

×(1−MOS
Bank
	​

)

Đối với những ngân hàng thương mại đầu ngành tại Việt Nam có bộ đệm dự phòng vững chắc và 
𝑅
𝑂
𝐸
Thực
≥
18
%
ROE
Thực
	​

≥18%, hệ thống có thể thiết lập 
𝑀
𝑂
𝑆
Bank
=
30
%
−
35
%
MOS
Bank
	​

=30%−35% trên giá trị RI/Sticker để phù hợp với độ lệch chuẩn thấp của giá trị sổ sách ngân hàng.   

Nhóm 4: Ngành Hạ tầng, Điện, Nước và Cảng biển — Mô hình Owner Earnings 10 Cap và Chiết khấu Cổ tức (GGM)

Các doanh nghiệp tiện ích và hạ tầng (như BWE, REE, NT2, GMD) có đặc điểm là chi phí đầu tư ban đầu (CapEx) rất lớn để xây dựng nhà máy phát điện, đường ống nước hoặc cầu cảng. Khi công trình đi vào vận hành thương mại, chi phí khấu hao kế toán hàng năm rất cao làm giảm lợi nhuận ròng (khiến EPS thấp và P/E có vẻ đắt), nhưng chi phí bảo trì thực tế lại rất nhỏ, tạo ra một lượng tiền mặt tự do dồi dào và tỷ lệ chi trả cổ tức tiền mặt ổn định.   

Đối với nhóm này, thuật toán Antigravity ưu tiên tối đa cho công thức 10 Cap (Owner Earnings) đã trình bày ở Mục 3 — nơi 
CapEx
Bảo tr
ı
ˋ
CapEx
Bảo tr
ı
ˋ
	​

 thực tế thấp hơn nhiều so với khấu hao kế toán, giúp phát hiện giá trị nội tại ẩn mà chỉ số P/E bỏ sót — kết hợp với Mô hình Tăng trưởng Gordon (GGM) dựa trên dòng tiền chủ sở hữu và dòng cổ tức ổn định:   

𝐼
𝑉
Utility (GGM)
=
Owner Earnings tr
e
ˆ
n m
o
ˆ
˜
i CP
×
(
1
+
𝑔
D
a
ˋ
i hạn
)
𝐾
𝑒
−
𝑔
D
a
ˋ
i hạn
IV
Utility (GGM)
	​

=
K
e
	​

−g
D
a
ˋ
i hạn
	​

Owner Earnings tr
e
ˆ
n m
o
ˆ
˜
i CP×(1+g
D
a
ˋ
i hạn
	​

)
	​

5. Kiến trúc Dữ liệu và Thuật toán Tổng hợp cho Hệ thống Antigravity

Để lập trình viên có thể nhúng trực tiếp toàn bộ nghiên cứu này vào mã nguồn trên Antigravity, phần dưới đây chuẩn hóa bảng ánh xạ mã số chỉ tiêu BCTC Việt Nam và thuật toán tính Điểm Hội tụ Định giá.

Bảng Ánh xạ Biến số Thuật toán với Mã số BCTC Việt Nam (Thông tư 200 & Thông tư 99/2025/TT-BTC)

Khi kết nối API dữ liệu tài chính Việt Nam, hệ thống Antigravity cần truy xuất chính xác các mã số chỉ tiêu sau đây để đảm bảo tính toàn vẹn của dữ liệu đầu vào qua các kỳ kế toán trước và sau ngày 01/01/2026:   

Biến số trong Thuật toán	Nguồn Báo cáo	Mã số Chỉ tiêu / Tài khoản Chuẩn VAS (TT200 / TT99)	Công thức Xử lý Làm sạch Dữ liệu (Data Cleaning Logic)
Cash_Equiv	Bảng CĐKT	Mã 110 + Mã 120 (trừ dự phòng Mã 122)	

Tiền + Tương đương tiền + Đầu tư tài chính ngắn hạn (tiền gửi có kỳ hạn).


Receivables_ST	Bảng CĐKT	Mã 130	

Các khoản phải thu ngắn hạn (theo dõi tỷ lệ Mã 130 / Tổng TS để kiểm soát chất lượng lợi nhuận).


Inventory	Bảng CĐKT	Mã 140 (Gốc: Mã 141, Dự phòng: Mã 149)	

Hàng tồn kho ròng (Trọng tâm định giá RNAV ngành Bất động sản).


Current_Assets	Bảng CĐKT	Mã 100	

Tổng Tài sản ngắn hạn (
100
=
110
+
120
+
130
+
140
+
150
100=110+120+130+140+150).


Fixed_Assets_Tang	Bảng CĐKT	Mã 221 (Nguyên giá: 222, Hao mòn: 223)	

Tài sản cố định hữu hình (Loại trừ TSCĐ hình thành từ Quỹ phúc lợi TK 3533 vì không trích khấu hao vào chi phí SXKD mà ghi giảm trực tiếp TK 3533).


Total_Assets	Bảng CĐKT	Mã 270	

Tổng cộng Tài sản (Khi tính Altman Z, lấy Mã 270 - Mã 227 (TSCĐ vô hình)).


Current_Liab	Bảng CĐKT	Mã 310	

Nợ ngắn hạn (Dùng tính Vốn lưu động 
𝑊
𝐶
=
M
a
˜
 
100
−
M
a
˜
 
310
WC=M
a
˜
 100−M
a
˜
 310).


Buyer_Prepaid	Bảng CĐKT	Mã 312 (Ngắn hạn) + Mã 332 (Dài hạn)	

Người mua trả tiền trước (Dữ liệu đầu vào bắt buộc cho mô hình RNAV BĐS).


Total_Debt	Bảng CĐKT	Mã 320 (Vay ngắn hạn) + Mã 338 (Vay dài hạn)	

Tổng nợ vay chịu lãi (Dùng tính 
𝑅
𝑂
𝐼
𝐶
ROIC, 
𝑊
𝐴
𝐶
𝐶
WACC và bộ lọc 
M
a
˜
 
338
/
𝐹
𝐶
𝐹
≤
3
M
a
˜
 338/FCF≤3).


Welfare_Fund_BS	Bảng CĐKT	Mã 322 (TK 353: 3531, 3532, 3533, 3534)	

Số dư Quỹ khen thưởng phúc lợi trên Bảng CĐKT thuộc nhóm Nợ phải trả.


Total_Equity	Bảng CĐKT	Mã 400 (hoặc Mã 410 - Vốn CSH)	

Vốn chủ sở hữu (Trừ Lợi ích cổ đông không kiểm soát Mã 429 để lấy VCSH Công ty mẹ).


Retained_Earnings	Bảng CĐKT	Mã 421 + Mã 418 (Quỹ đầu tư phát triển)	

Lợi nhuận sau thuế chưa phân phối cộng Quỹ ĐTPT (Dùng cho biến 
𝑋
2
X
2
	​

 trong Altman Z).


NPAT_Parent	KQKD	Mã 61	

Lợi nhuận sau thuế của cổ đông công ty mẹ.


Welfare_Deduct	Thuyết minh / CĐV	Phát sinh Có TK 353 đối ứng Nợ TK 421	

Khoản trích Quỹ KTPL trong kỳ. Nếu API thiếu thuyết minh, ước lượng qua biến động số dư Mã 322 cộng tiền thực chi từ quỹ trên báo cáo LCTT.


CFO	Lưu chuyển TT	Mã 20 (Báo cáo LCTT)	

Lưu chuyển tiền thuần từ hoạt động kinh doanh.


CapEx	Lưu chuyển TT	Mã 21 (Báo cáo LCTT - ghi âm)	

Tiền chi để mua sắm, xây dựng TSCĐ và các tài sản dài hạn khác.

  
Thuật toán Điều chỉnh Biên An toàn Động (Dynamic Margin of Safety) và Điểm Hội tụ

Trong thực tế đầu tư tại Việt Nam, nếu áp dụng cứng nhắc mức chiết khấu 
15
%
15% kèm Biên an toàn 
𝑀
𝑂
𝑆
=
50
%
MOS=50% cho mọi cổ phiếu, hệ thống sẽ chỉ lọc ra được cơ hội mua trong những đợt hoảng loạn toàn thị trường hiếm hoi. Ngược lại, những cổ phiếu đầu ngành có con hào kinh tế độc quyền thường xuyên giao dịch ở vùng định giá cao hơn vì dòng tiền thông minh nhận diện rõ chất lượng của chúng. Do đó, các nhà đầu tư giá trị như Seth Klarman hay những nhà quản lý quỹ áp dụng khung phân tích của Buffett và Phil Town thường linh hoạt sử dụng dải Biên an toàn từ 
20
%
20% đến 
50
%
50% tùy thuộc vào mức độ chắc chắn của dự báo và chất lượng bảng cân đối kế toán.   

Hệ thống Antigravity có thể tự động hóa hoàn toàn quyết định này bằng Thuật toán Định cỡ Biên An toàn Động (Dynamic MOS Sizing) dựa trên ma trận phân hạng chất lượng doanh nghiệp dưới đây:   

Phân hạng Cổ phiếu trên Antigravity	Điều kiện Bộ lọc Định lượng (Big Five, Piotroski F, Altman Z)	Biên An toàn Động (
𝑀
𝑂
𝑆
Động
MOS
Động
	​

) Khuyến nghị	Hành động của Hệ thống Định giá
Hạng 1: Kim Cương (Tier 1 - Compounders)	

Thỏa mãn toàn bộ Big Five (
≥
10
%
≥10%), Nợ dài hạn 
≤
3
×
𝐹
𝐶
𝐹
≤3×FCF, 
𝐹
-Score
∈
[
8
,
9
]
F-Score∈[8,9], và Altman 
𝑍
Z nằm sâu trong vùng An toàn (
𝑍
>
3
,
5
Z>3,5 hoặc 
𝑍
EM
′
′
>
3
,
2
Z
EM
′′
	​

>3,2).

	

25
%
−
30
%
25%−30% trên DCF/RNAV; 
35
%
−
40
%
35%−40% trên Sticker Price.

	

Kích hoạt tín hiệu mua tích lũy từng phần (Dollar-Cost Averaging) ngay khi thị giá chạm vùng mua.


Hạng 2: Tiêu Chuẩn (Tier 2 - Solid Value)	

Thỏa mãn tối thiểu 4/5 tiêu chí Big Five, 
𝐹
-Score
∈
[
6
,
7
]
F-Score∈[6,7], và Altman 
𝑍
Z đạt ngưỡng An toàn (
𝑍
>
2
,
99
Z>2,99 hoặc 
𝑍
EM
′
′
>
2
,
60
Z
EM
′′
	​

>2,60).

	

50
%
50% chuẩn cổ điển trên Sticker Price; Payback Time 
≤
8
≤8 năm.

	

Thiết lập cảnh báo chờ mua (Waiting Alert) khi thị giá chiết khấu đủ 50% so với Sticker Price.


Hạng 3: Xoay Chuyển (Tier 3 - Grey Zone)	

𝐹
-Score
∈
[
4
,
5
]
F-Score∈[4,5] hoặc Altman 
𝑍
Z nằm trong Vùng Xám (
1
,
81
≤
𝑍
≤
2
,
99
1,81≤Z≤2,99 hoặc 
1
,
10
≤
𝑍
EM
′
′
≤
2
,
60
1,10≤Z
EM
′′
	​

≤2,60).

	

50
%
−
60
%
50%−60% trên mọi mô hình; chặn trần giá mua 
≤
𝑃
Zombie
≤P
Zombie
	​

.

	

Yêu cầu định giá cực rẻ (chỉ mua dưới Giá trị Xác sống khi giả định tăng trưởng bằng 0%).


Hạng 4: Loại Bỏ (Tier 4 - Value Trap / Distress)	

𝐹
-Score
≤
3
F-Score≤3 hoặc Altman 
𝑍
Z rơi vào Vùng Nguy hiểm (
𝑍
<
1
,
81
Z<1,81 hoặc 
𝑍
EM
′
′
<
1
,
10
Z
EM
′′
	​

<1,10).

	

Khóa tín hiệu mua (
𝑀
𝑂
𝑆
=
N/A
MOS=N/A).

	

Gắn cờ đỏ "CẢNH BÁO BẪY GIÁ TRỊ (VALUE TRAP)", loại bỏ khỏi danh mục giải ngân bất chấp P/E thấp.

  

Cuối cùng, như Phil Town đã khẳng định, mỗi phương pháp định giá (Sticker Price, 10 Cap, Payback Time, DCF/RNAV) sẽ cho ra một con số khác nhau và mỗi con số đều đúng dưới góc nhìn riêng của nó; chính sự hội tụ (Convergence) của các mức giá này mới là cơ sở mang lại sự tự tin cao nhất cho nhà đầu tư. Trên giao diện Antigravity, thay vì chỉ xuất ra một con số duy nhất, hệ thống cần hiển thị một Vùng Mua Hội Tụ (Convergence Buy Zone) được tính bằng trung bình có trọng số theo ngành (như Bảng Ma trận ở Mục 4), kèm theo Chỉ số Hội tụ Định giá (Convergence Score):   

𝑃
Mục ti
e
ˆ
u Mua (Antigravity)
=
∑
𝑚
=
1
4
𝑤
Ng
a
ˋ
nh
,
𝑚
×
𝑃
Buy
,
𝑚
P
Mục ti
e
ˆ
u Mua (Antigravity)
	​

=
m=1
∑
4
	​

w
Ng
a
ˋ
nh,m
	​

×P
Buy,m
	​

Độ Hội tụ (Convergence Score)
=
1
−
𝜎
(
𝑃
Buy, 1
,
𝑃
Buy, 2
,
𝑃
Buy, 4
)
𝜇
(
𝑃
Buy
)
Độ Hội tụ (Convergence Score)=1−
μ(P
Buy
	​

)
σ(P
Buy, 1
	​

,P
Buy, 2
	​

,P
Buy, 4
	​

)
	​


Khi Độ Hội tụ tiến gần về 
1
1 — tức độ lệch chuẩn 
𝜎
σ giữa giá Sticker MOS, giá 10 Cap, giá Payback 8 năm và giá DCF/RNAV thu hẹp tối đa quanh giá trị trung bình 
𝜇
μ — đồng thời thị giá trên sàn chứng khoán Việt Nam giảm xuống dưới ngưỡng 
𝑃
Mục ti
e
ˆ
u Mua
P
Mục ti
e
ˆ
u Mua
	​

, công cụ trên Antigravity sẽ phát tín hiệu giải ngân mạnh mẽ nhất, kết tinh trọn vẹn kỷ luật bảo toàn vốn của Warren Buffett và hệ thống định lượng của Phil Town.   

6. Khung Phân tích Ngành Chuyên sâu và Lựa chọn Mô hình Định giá Tối ưu

Để khắc phục triệt để hạn chế của việc áp dụng một công thức chung, hệ thống Antigravity cần tích hợp một Mô-đun Phân tích Ngành từ trên xuống (Top-Down Sector Analyzer) trước khi quyết định mô hình định giá chủ đạo cho từng cổ phiếu. Trên thị trường chứng khoán Việt Nam, động lực tăng trưởng của các nhóm ngành gắn liền chặt chẽ với các biến số vĩ mô nội địa: trong kịch bản cơ sở khi tăng trưởng GDP đạt khoảng 
7
,
3
%
7,3% và tăng trưởng tín dụng toàn hệ thống đạt 
16
%
16%, lợi nhuận của các doanh nghiệp niêm yết được kỳ vọng tăng trưởng từ 
14
%
−
15
%
14%−15%, qua đó neo mặt bằng định giá 
𝑃
/
𝐸
P/E dự phóng của VN-Index quanh ngưỡng 
13
,
5
13,5 lần trong điều kiện lạm phát (CPI bình quân khoảng 
3
,
21
%
3,21%) được kiểm soát dưới trần 
4
,
5
%
−
5
,
0
%
4,5%−5,0% và tỷ giá USD/VND duy trì độ biến động hợp lý.   

Tiêu chí Lọc Hiệu quả Vốn Ngành (ROCE, ROE, ROA) và Bộ Công thức Benjamin Graham Bản địa hóa

Trước khi chạy các mô hình phức tạp, thuật toán phân tích ngành trên Antigravity cần sử dụng bộ ba chỉ số Tỷ suất Sinh lời trên Vốn Sử dụng (
𝑅
𝑂
𝐶
𝐸
ROCE), 
𝑅
𝑂
𝐸
ROE và 
𝑅
𝑂
𝐴
ROA để xếp hạng vị thế cạnh tranh của các doanh nghiệp trong cùng một ngành. Trong đó, 
𝑅
𝑂
𝐶
𝐸
ROCE đặc biệt hiệu quả khi so sánh các doanh nghiệp thâm dụng vốn cùng ngành (như thép, hóa chất, điện, cảng biển) để xác định công ty nào tạo ra nhiều lợi nhuận hoạt động nhất trên mỗi đồng vốn dài hạn bỏ ra:   

𝑅
𝑂
𝐶
𝐸
=
𝐸
𝐵
𝐼
𝑇
Tổng T
a
ˋ
i sản (M
a
˜
 270)
−
Nợ Ng
a
˘
ˊ
n hạn (M
a
˜
 310)
ROCE=
Tổng T
a
ˋ
i sản (M
a
˜
 270)−Nợ Ng
a
˘
ˊ
n hạn (M
a
˜
 310)
EBIT
	​


Bên cạnh bộ tứ công thức của Phil Town, vì Warren Buffett là học trò xuất sắc nhất của Benjamin Graham, hệ thống Antigravity nên tích hợp thêm Bộ 3 Công thức Định giá Benjamin Graham đã được hiệu chỉnh cho lãi suất thị trường Việt Nam để làm mốc tham chiếu bảo toàn vốn tuyệt đối:   

Công thức Graham Tăng trưởng Cơ bản: Giả định một doanh nghiệp không tăng trưởng (
𝑔
=
0
%
g=0%) xứng đáng có mức 
𝑃
/
𝐸
P/E cơ sở là 
8
,
5
8,5 lần, sau đó cộng thêm 
2
2 lần tốc độ tăng trưởng kép dự kiến trong 7–10 năm tới (
𝑔
g tính theo đơn vị phần trăm nguyên, ví dụ tăng trưởng 
10
%
10% thì 
𝑔
=
10
g=10):
  

𝐼
𝑉
Graham 1
=
𝐸
𝑃
𝑆
Thực
×
(
8
,
5
+
2
𝑔
)
IV
Graham 1
	​

=EPS
Thực
	​

×(8,5+2g)

Công thức Graham Điều chỉnh Lãi suất Trái phiếu Việt Nam: Công thức gốc của Graham lấy lãi suất trái phiếu doanh nghiệp hạng AAA kỳ hạn 20 năm của Mỹ thời điểm đó là 
4
,
4
%
4,4% chia cho lãi suất hiện hành (
𝑌
Y). Khi áp dụng vào thị trường Việt Nam nơi thị trường trái phiếu doanh nghiệp chưa có chuẩn xếp hạng AAA đồng nhất 20 năm, các chuyên gia phân tích chuẩn hóa mẫu số 
𝑌
VN
Y
VN
	​

 bằng Lãi suất Trái phiếu Chính phủ Việt Nam kỳ hạn 10 năm cộng biên độ 
0
,
5
%
0,5% (
𝑌
VN
=
𝑅
𝑓
+
0
,
5
%
≈
4
,
58
%
+
0
,
5
%
=
5
,
08
%
Y
VN
	​

=R
f
	​

+0,5%≈4,58%+0,5%=5,08%):
  

𝐼
𝑉
Graham 2 (VN)
=
𝐸
𝑃
𝑆
Thực
×
(
8
,
5
+
2
𝑔
)
×
4
,
4
𝑅
𝑓
 (10Y VGB)
+
0
,
5
IV
Graham 2 (VN)
	​

=
R
f (10Y VGB)
	​

+0,5
EPS
Thực
	​

×(8,5+2g)×4,4
	​


Con số Graham (Graham Number) cho Nhóm Tài sản Hữu hình: Kết hợp đồng thời cả giới hạn 
𝑃
/
𝐸
≤
15
P/E≤15 và 
𝑃
/
𝐵
≤
1
,
5
P/B≤1,5 (
15
×
1
,
5
=
22
,
5
15×1,5=22,5), cực kỳ hiệu quả để tìm điểm mua an toàn cho các doanh nghiệp sản xuất và tài chính có giá trị sổ sách thực chất:
  

𝑃
Graham Number
=
22
,
5
×
𝐸
𝑃
𝑆
Thực
×
𝐵
𝑉
𝑃
𝑆
Thực
P
Graham Number
	​

=
22,5×EPS
Thực
	​

×BVPS
Thực
	​

	​

Ma trận Phân tích Đặc thù 8 Nhóm Ngành và Thuật toán Chọn Mô hình Định giá Tối ưu

Không có bất kỳ một mô hình định giá đơn lẻ nào phù hợp cho mọi loại hình doanh nghiệp. Trong khi các doanh nghiệp trưởng thành có dòng tiền tự do ổn định là ứng cử viên lý tưởng cho DCF, thì các tập đoàn trả cổ tức tiền mặt đều đặn lại phù hợp với chiết khấu cổ tức (DDM), còn những ngành có tỷ trọng tài sản hữu hình và tài sản tài chính lớn bắt buộc phải định giá dựa trên giá trị sổ sách (
𝑃
/
𝐵
P/B, 
𝑁
𝐴
𝑉
NAV). Bảng dưới đây thiết lập thuật toán phân nhánh chi tiết cho 8 nhóm ngành trọng yếu trên sàn chứng khoán Việt Nam:   

Phân Ngành Cụ thể tại Việt Nam	Biến số Dẫn dắt Giá trị (Key Value Drivers)	Phương pháp Định giá Nội tại Tối ưu (Absolute)	Phương pháp Định giá Tương đối Tối ưu (Relative)	Lý giải Chuyên môn & Quy tắc Điều chỉnh trên Antigravity
1. Ngân hàng Thương mại (VCB, BID, CTG, ACB, MBB, TCB)	Tăng trưởng tín dụng (hạn mức NHNN), Biên lãi ròng (
𝑁
𝐼
𝑀
NIM), Tỷ lệ tiền gửi không kỳ hạn (
𝐶
𝐴
𝑆
𝐴
CASA), Tỷ lệ nợ xấu (
𝑁
𝑃
𝐿
NPL) & Bao phủ nợ xấu (
𝐿
𝐿
𝑅
LLR).	

Mô hình Thu nhập Thặng dư (
𝑅
𝐼
RI) & BVPS Sticker Price.

	

𝑃
/
𝐵
P/B hồi quy theo 
𝑅
𝑂
𝐸
ROE (Peer 
𝑃
/
𝐵
−
𝑅
𝑂
𝐸
P/B−ROE Matrix).

	

Tài sản ngân hàng có tính thanh khoản và định giá theo thị trường cao nên giá trị sổ sách (
𝐵
𝑉
𝑃
𝑆
BVPS) có độ tin cậy lớn. Phải khấu trừ phần thiếu hụt dự phòng nợ xấu khỏi 
𝐵
𝑉
𝑃
𝑆
0
BVPS
0
	​

 trước khi chạy mô hình.


2. Công ty Chứng khoán (CTCK) (SSI, VND, HCM, VCI, MBS, VIX)	Thanh khoản thị trường (giá trị giao dịch/phiên), Dư nợ cho vay ký quỹ (Margin), Danh mục tự doanh (FVTPL, AFS).	

BVPS Compounding + Đánh giá lại Danh mục Tự doanh (Mark-to-Market NAV).

	

Hệ số 
𝑃
/
𝐵
P/B phân tầng theo quy mô vốn và thị phần.

	

Dữ liệu thực tế tại Việt Nam cho thấy các CTCK đầu ngành (SSI, HCM, MBS, TCX, VIX) giao dịch ở mức 
𝑃
/
𝐵
P/B từ 
2
,
5
x
−
3
,
0
x
2,5x−3,0x, cao hơn hẳn nhóm CTCK vừa và nhỏ (
𝑃
/
𝐵
≈
1
,
5
x
P/B≈1,5x trở xuống) do lợi thế nguồn vốn giá rẻ và hệ thống công nghệ.


3. Bảo hiểm Nhân thọ & Phi Nhân thọ (BVH, PVI, MIG, BMI, PTI)	Doanh thu phí bảo hiểm gốc, Tỷ lệ bồi thường + chi phí (
𝐶
𝑜
𝑚
𝑏
𝑖
𝑛
𝑒
𝑑
 
𝑅
𝑎
𝑡
𝑖
𝑜
<
100
%
Combined Ratio<100%), Lợi suất đầu tư tiền gửi/trái phiếu Chính phủ (
𝑅
𝑓
R
f
	​

).	

Chiết khấu Cổ tức (
𝐷
𝐷
𝑀
DDM) kết hợp Thu nhập Thặng dư (
𝑅
𝐼
RI).

	

𝑃
/
𝐵
P/B kết hợp 
𝑅
𝑂
𝐸
ROE và Tỷ suất Cổ tức (
𝐷
𝑖
𝑣
𝑖
𝑑
𝑒
𝑛
𝑑
 
𝑌
𝑖
𝑒
𝑙
𝑑
Dividend Yield).

	

Ngành bảo hiểm hưởng lợi trực tiếp khi lợi suất trái phiếu và lãi suất tiền gửi nhích lên; tài sản chủ yếu là tiền gửi và trái phiếu nên 
𝑃
/
𝐵
P/B phản ánh sát giá trị nội tại.


4. Bất động sản Dân dụng & Khu Công nghiệp (VHM, KDH, NLG, KBC, IDC,bcm)	

Quỹ đất sạch pháp lý, Tiến độ bán hàng (Pre-sales / Người mua trả tiền trước), Giá thuê đất KCN và dòng vốn FDI thực hiện.

	

Giá trị Tài sản Ròng Đánh giá lại (
𝑅
𝑁
𝐴
𝑉
RNAV / 
𝑆
𝑂
𝑇
𝑃
SOTP) chiết khấu dòng tiền từng dự án.

	

𝑃
/
𝐵
P/B và 
𝑃
/
RNAV
P/RNAV so sánh ngang hàng.

	

Riêng nhóm BĐS Khu công nghiệp nhận tiền thuê đất 1 lần (treo ở Doanh thu chưa thực hiện dài hạn - Mã 336) có dòng tiền đều đặn hơn BĐS dân dụng, có thể kết hợp 
50
%
 RNAV
+
50
%
 10 Cap Owner Earnings
50% RNAV+50% 10 Cap Owner Earnings.


5. Bán lẻ & Hàng Tiêu dùng (FMCG) (VNM, MSN, MWG, PNJ, FRT, SAB)	

Tăng trưởng doanh thu trên cùng cửa hàng (
𝑆
𝑆
𝑆
𝐺
SSSG), Biên lợi nhuận gộp, Vòng quay hàng tồn kho, Sức mạnh thương hiệu (Moat).

	

Bộ tứ Rule #1 (Sticker Price, Payback Time, 10 Cap) & DCF 2 giai đoạn.

	

𝑃
/
𝐸
P/E, 
𝑃
𝐸
𝐺
PEG và 
𝑃
/
𝑆
P/S (dành cho chuỗi bán lẻ đang mở rộng/vực dậy).

	

Với các chuỗi bán lẻ đang trong giai đoạn mở rộng thần tốc hoặc mới thoát lỗ (như FRT giai đoạn đầu chuỗi nhà thuốc), lợi nhuận ròng bị nén nên phải dùng 
𝑃
/
𝑆
P/S và 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
EV/EBITDA thay vì 
𝑃
/
𝐸
P/E đơn thuần.


6. Công nghệ Thông tin & Viễn thông (FPT, CMG, CTR, FOX, ELC)	

Tốc độ tăng trưởng hợp đồng ký mới ở nước ngoài, Biên EBIT mảng phần mềm, Tỷ lệ 
𝑅
𝑂
𝐼
𝐶
ROIC và chất xám nhân sự.

	

Sticker Price (cho phép 
𝑀
𝑂
𝑆
MOS động 
25
%
−
30
%
25%−30%) & DCF 2 giai đoạn.

	

𝑃
𝐸
𝐺
PEG (Price/Earnings to Growth) và 
𝑃
/
𝐸
P/E dự phóng (Forward 
𝑃
/
𝐸
P/E).

	

Công ty công nghệ có tài sản hữu hình thấp nên 
𝑃
/
𝐵
P/B rất cao (vô nghĩa nếu định giá theo 
𝑁
𝐴
𝑉
NAV); công cụ tốt nhất để đo lường độ đắt/rẻ là chỉ số 
𝑃
𝐸
𝐺
PEG.


7. Sản xuất Chu kỳ & Vật liệu Cơ bản (HPG, HSG, DGC, DPM, DCM, BSR, PVT)	

Chu kỳ giá hàng hóa thế giới (thép HRC, phốt pho, phân ure, crack spread lọc dầu, giá cước vận tải biển) & Công suất nhà máy.

	

DCF & Sticker Price dựa trên Lợi nhuận Chuẩn hóa Giữa Chu kỳ (Normalized EPS/FCF).

	

𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
EV/EBITDA, 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
EV/EBIT và 
𝑃
/
𝐵
P/B lịch sử.

	

Các doanh nghiệp như PVT hay HPG có khấu hao và nợ vay đầu tư tàu/nhà máy lớn; dùng 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
EV/EBITDA và 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
EV/EBIT giúp loại bỏ sự khác biệt về cấu trúc nợ vay và chính sách khấu hao giữa các công ty.


8. Điện, Nước, Hạ tầng & Cảng biển (REE, BWE, NT2, POW, GMD, ACV)	Sản lượng điện/nước thương phẩm, Khung giá phát điện/biểu giá dịch vụ cảng, Thời điểm hết khấu hao nhà máy.	

10 Cap (Owner Earnings), Chiết khấu Cổ tức (
𝐷
𝐷
𝑀
DDM / 
𝐺
𝐺
𝑀
GGM) & FCFF DCF.

	

𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
EV/EBITDA và Công thức Cổ tức – Tăng trưởng 
(
𝑅
+
𝐺
)
/
𝑃
𝐸
(R+G)/PE.

	

Phù hợp hoàn hảo với mô hình 
𝐷
𝐷
𝑀
DDM và công thức 
(
𝑅
+
𝐺
)
/
𝑃
𝐸
>
1
,
5
(R+G)/PE>1,5 nhờ tỷ lệ chi trả cổ tức tiền mặt cao và dòng tiền kinh doanh dự báo được trong 10–20 năm.

  
7. Hệ thống Định giá Tương đối (Relative Valuation) và Thuật toán Xác định Giá Bán Mục tiêu (Relative Selling Price)

Một hệ thống đầu tư hoàn chỉnh trên Antigravity không chỉ trả lời câu hỏi "Mua ở giá nào?" mà bắt buộc phải trả lời chính xác câu hỏi "Bán ở giá nào để tối ưu hóa lợi nhuận?". Trong khi các mô hình Định giá Tuyệt đối (Absolute Valuation như DCF, RNAV, 10 Cap) giúp tìm ra Giá trị Nội tại để mua vào với biên an toàn, thì các mô hình Định giá Tương đối (Relative Valuation dựa trên bội số thị trường 
𝑃
/
𝐸
P/E, 
𝑃
/
𝐵
P/B, 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
EV/EBITDA, 
𝑃
𝐸
𝐺
PEG, 
𝑃
/
𝑆
P/S) lại là công cụ sắc bén nhất để đo lường mức độ hưng phấn của thị trường và xác lập Giá Bán Tương đối (Relative Selling Price).   

5 Công thức Định giá Tương đối Chuẩn hóa trên Antigravity

Để định giá tương đối không bị cảm tính, hệ thống cần tự động gom nhóm các doanh nghiệp tương đồng (Peer Group) trong cùng phân ngành ICB có quy mô vốn hóa và mô hình kinh doanh tương đương, sau đó tính toán 5 chỉ số định giá tương đối sau:   

Định giá theo Dải 
𝑃
/
𝐸
P/E Lịch sử (Historical 
𝑃
/
𝐸
P/E Standard Deviation Bands) và 
𝑃
/
𝐸
P/E Ngành:
Thay vì chỉ lấy 
𝐸
𝑃
𝑆
×
𝑃
/
𝐸
Ng
a
ˋ
nh
EPS×P/E
Ng
a
ˋ
nh
	​

 một cách cơ học, thuật toán Antigravity tính trung bình (
𝜇
𝑃
𝐸
μ
PE
	​

) và độ lệch chuẩn (
𝜎
𝑃
𝐸
σ
PE
	​

) của hệ số 
𝑃
/
𝐸
P/E trong 5 năm gần nhất của chính cổ phiếu đó. Khi 
𝑃
/
𝐸
P/E hiện tại lùi về dưới đường 
−
1
SD
−1SD hoặc 
−
2
SD
−2SD (
𝜇
𝑃
𝐸
−
2
𝜎
𝑃
𝐸
μ
PE
	​

−2σ
PE
	​

), cổ phiếu đang ở vùng định giá rẻ lịch sử; ngược lại khi vượt lên trên 
+
1
SD
+1SD đến 
+
2
SD
+2SD (
𝜇
𝑃
𝐸
+
2
𝜎
𝑃
𝐸
μ
PE
	​

+2σ
PE
	​

), cổ phiếu bước vào vùng quá nhiệt:
  

𝑃
Mục ti
e
ˆ
u 
𝑃
/
𝐸
 Cơ sở
=
𝐸
𝑃
𝑆
Thực Dự ph
o
ˊ
ng (Forward)
×
min
⁡
(
𝑃
𝐸
Trung vị Ng
a
ˋ
nh
,
𝜇
𝑃
𝐸
 (5 n
a
˘
m)
)
P
Mục ti
e
ˆ
u P/E Cơ sở
	​

=EPS
Thực Dự ph
o
ˊ
ng (Forward)
	​

×min(PE
Trung vị Ng
a
ˋ
nh
	​

,μ
PE (5 n
a
˘
m)
	​

)
𝑃
B
a
ˊ
n Tương đ
o
ˆ
ˊ
i (Dải tr
e
ˆ
n 
𝑃
/
𝐸
)
=
𝐸
𝑃
𝑆
Thực Dự ph
o
ˊ
ng (Forward)
×
(
𝜇
𝑃
𝐸
 (5 n
a
˘
m)
+
𝑘
×
𝜎
𝑃
𝐸
 (5 n
a
˘
m)
)
(
với 
𝑘
∈
[
1
,
2
]
)
P
B
a
ˊ
n Tương đ
o
ˆ
ˊ
i (Dải tr
e
ˆ
n P/E)
	​

=EPS
Thực Dự ph
o
ˊ
ng (Forward)
	​

×(μ
PE (5 n
a
˘
m)
	​

+k×σ
PE (5 n
a
˘
m)
	​

)(với k∈[1,2])

Định giá 
𝑃
/
𝐵
P/B Kết hợp Ma trận Hồi quy 
𝑅
𝑂
𝐸
ROE (Peer 
𝑃
/
𝐵
−
𝑅
𝑂
𝐸
P/B−ROE Regression):
Hạn chế lớn nhất của phương pháp 
𝑃
/
𝐵
P/B truyền thống là giá trị sổ sách chỉ phản ánh tài sản hữu hình mà bỏ qua tài sản vô hình (thương hiệu, hệ thống quản trị). Để khắc phục điểm yếu này trên Antigravity, thuật toán phải ghép cặp tỷ lệ 
𝑃
/
𝐵
P/B với 
𝑅
𝑂
𝐸
ROE qua một phương trình hồi quy tuyến tính của toàn bộ các công ty cùng ngành: 
𝑃
𝐵
^
𝑖
=
𝛼
+
𝛽
Ng
a
ˋ
nh
×
𝑅
𝑂
𝐸
𝑖
PB
i
	​

=α+β
Ng
a
ˋ
nh
	​

×ROE
i
	​

. Trên biểu đồ phân tán (Scatter Plot) với trục tung là 
𝑅
𝑂
𝐸
ROE và trục hoành là 
𝑃
/
𝐵
P/B, đường chéo hồi quy đại diện cho mức định giá hợp lý: những cổ phiếu nằm ở nửa dưới đường chéo (có 
𝑅
𝑂
𝐸
ROE cao nhưng 
𝑃
/
𝐵
P/B thấp hơn mức hồi quy) là cổ phiếu đang bị định giá thấp; những cổ phiếu nằm ở nửa trên đường chéo là đang bị thị trường định giá quá cao. Chẳng hạn, với mức 
𝑅
𝑂
𝐸
=
24
,
9
%
ROE=24,9% của Vinamilk (VNM), chiếu lên đường chéo hồi quy ngành hàng tiêu dùng nhanh (FMCG) sẽ xác lập mức 
𝑃
/
𝐵
P/B hợp lý khoảng 
6
x
6x, tương ứng giá trị hợp lý 
6
×
15.702
≈
94.212
 đ
o
ˆ
ˋ
ng/cổ phi
e
ˆ
ˊ
u
6×15.702≈94.212 đ
o
ˆ
ˋ
ng/cổ phi
e
ˆ
ˊ
u:
  

𝑃
Mục ti
e
ˆ
u 
𝑃
/
𝐵
−
𝑅
𝑂
𝐸
=
𝐵
𝑉
𝑃
𝑆
Thực
×
(
𝛼
Ng
a
ˋ
nh
+
𝛽
Ng
a
ˋ
nh
×
𝑅
𝑂
𝐸
Thực
)
P
Mục ti
e
ˆ
u P/B−ROE
	​

=BVPS
Thực
	​

×(α
Ng
a
ˋ
nh
	​

+β
Ng
a
ˋ
nh
	​

×ROE
Thực
	​

)

Định giá theo Hệ số 
𝑃
𝐸
𝐺
PEG (Price/Earnings to Growth) và Chỉ số 
(
𝑅
+
𝐺
)
/
𝑃
𝐸
(R+G)/PE:
Chỉ số 
𝑃
𝐸
𝐺
PEG điều chỉnh hệ số 
𝑃
/
𝐸
P/E theo tốc độ tăng trưởng lợi nhuận dự kiến (
𝐺
G, tính theo số nguyên phần trăm). Một cổ phiếu có 
𝑃
𝐸
𝐺
=
1
PEG=1 đang phản ánh đúng giá trị hợp lý; 
𝑃
𝐸
𝐺
<
1
PEG<1 là tín hiệu cổ phiếu đang bị định giá thấp hơn tiềm năng tăng trưởng; và 
𝑃
𝐸
𝐺
>
1
PEG>1 (đặc biệt khi 
𝑃
𝐸
𝐺
≥
1
,
5
−
2
,
0
PEG≥1,5−2,0) phản ánh cổ phiếu đã bị định giá quá cao. Đối với các doanh nghiệp vừa tăng trưởng vừa trả cổ tức tiền mặt, hệ thống bổ sung chỉ số kết hợp tỷ suất cổ tức (
𝑅
=
Cổ tức
/
Thị gi
a
ˊ
R=Cổ tức/Thị gi
a
ˊ
) và tốc độ tăng trưởng (
𝐺
G) của Peter Lynch: một cổ phiếu đạt chuẩn hấp dẫn dài hạn khi 
(
𝑅
+
𝐺
)
/
𝑃
𝐸
>
1
,
5
(R+G)/PE>1,5:
  

𝑃
𝐸
𝐺
=
𝑃
/
𝐸
𝐺
⟹
𝑃
Hợp l
y
ˊ
 
(
𝑃
𝐸
𝐺
=
1
)
=
𝐸
𝑃
𝑆
Thực
×
𝐺
PEG=
G
P/E
	​

⟹P
Hợp l
y
ˊ
	​

 (PEG=1)
	​

=EPS
Thực
	​

×G
Chỉ s
o
ˆ
ˊ
 Cổ tức - T
a
˘
ng trưởng
=
𝑅
 (%)
+
𝐺
 (%)
𝑃
/
𝐸
>
1
,
5
Chỉ s
o
ˆ
ˊ
 Cổ tức - T
a
˘
ng trưởng=
P/E
R (%)+G (%)
	​

>1,5

Định giá Doanh nghiệp theo 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
EV/EBITDA và 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
EV/EBIT:
Đối với các ngành công nghiệp nặng, dầu khí, vận tải biển (như PVT), thép, xi măng và hạ tầng, cấu trúc nợ vay và chi phí khấu hao làm biến dạng hoàn toàn chỉ số 
𝑃
/
𝐸
P/E. Hệ thống Antigravity sử dụng Giá trị Doanh nghiệp (
𝐸
𝑉
=
V
o
ˆ
ˊ
n h
o
ˊ
a
+
Tổng Nợ vay (M
a
˜
 320 + 338)
−
Ti
e
ˆ
ˋ
n v
a
ˋ
 Tương đương ti
e
ˆ
ˋ
n (M
a
˜
 110 + 120)
EV=V
o
ˆ
ˊ
n h
o
ˊ
a+Tổng Nợ vay (M
a
˜
 320 + 338)−Ti
e
ˆ
ˋ
n v
a
ˋ
 Tương đương ti
e
ˆ
ˋ
n (M
a
˜
 110 + 120)) chia cho 
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
EBITDA hoặc 
𝐸
𝐵
𝐼
𝑇
EBIT. Thông thường, mức 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
<
10
EV/EBIT<10 hoặc 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
<
6
x
−
8
x
EV/EBITDA<6x−8x tại Việt Nam là vùng định giá hấp dẫn. Công thức suy ngược từ bội số 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
EV/EBITDA mục tiêu của ngành ra Giá Cổ phiếu Hợp lý là:
  

𝑃
Mục ti
e
ˆ
u 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
=
(
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
Dự ph
o
ˊ
ng
×
Trung vị 
(
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
)
Ng
a
ˋ
nh
)
−
Tổng Nợ vay
+
Ti
e
ˆ
ˋ
n mặt
S
o
ˆ
ˊ
 lượng Cổ phi
e
ˆ
ˊ
u Lưu h
a
ˋ
nh Pha lo
a
˜
ng
P
Mục ti
e
ˆ
u EV/EBITDA
	​

=
S
o
ˆ
ˊ
 lượng Cổ phi
e
ˆ
ˊ
u Lưu h
a
ˋ
nh Pha lo
a
˜
ng
(EBITDA
Dự ph
o
ˊ
ng
	​

×Trung vị (EV/EBITDA)
Ng
a
ˋ
nh
	​

)−Tổng Nợ vay+Ti
e
ˆ
ˋ
n mặt
	​


Định giá theo Doanh thu 
𝑃
/
𝑆
P/S (Price to Sales) cho Cổ phiếu Xoay chuyển (Turnaround):
Dành riêng cho các doanh nghiệp thương mại, bán lẻ đang trong giai đoạn đầu tư mở rộng chuỗi hoặc đang vực dậy sau thời kỳ thua lỗ tạm thời (khi 
𝐸
𝑃
𝑆
≤
0
EPS≤0 làm 
𝑃
/
𝐸
P/E mất tác dụng), hệ thống sử dụng hệ số 
𝑃
/
𝑆
=
V
o
ˆ
ˊ
n h
o
ˊ
a Thị trường
/
Tổng Doanh thu Thu
a
ˆ
ˋ
n
P/S=V
o
ˆ
ˊ
n h
o
ˊ
a Thị trường/Tổng Doanh thu Thu
a
ˆ
ˋ
n để so sánh với trung vị lịch sử và trung vị ngành:
  

𝑃
Mục ti
e
ˆ
u 
𝑃
/
𝑆
=
(
Doanh thu Thu
a
ˆ
ˋ
n Dự ph
o
ˊ
ng
S
o
ˆ
ˊ
 lượng CP Lưu h
a
ˋ
nh
)
×
𝑃
/
𝑆
Mục ti
e
ˆ
u Ng
a
ˋ
nh
P
Mục ti
e
ˆ
u P/S
	​

=(
S
o
ˆ
ˊ
 lượng CP Lưu h
a
ˋ
nh
Doanh thu Thu
a
ˆ
ˋ
n Dự ph
o
ˊ
ng
	​

)×P/S
Mục ti
e
ˆ
u Ng
a
ˋ
nh
	​

Thuật toán Xác định Tỷ lệ Thắng/Thua (Win-Loss Ratio) và Giá Bán Tương đối (Exit Signals)

Trong nguyên tắc đầu tư của các định chế tài chính chuyên nghiệp như SSI hay Vietcap cũng như triết lý của Phil Town, nhà đầu tư mua vào khi thị giá thấp hơn giá trị định giá và bán ra cổ phiếu khi thị giá vượt lên trên giá trị hợp lý để hiện thực hóa lợi nhuận hoặc khi nền tảng cơ bản của doanh nghiệp không còn tuyệt vời.   

Để lượng hóa quyết định mua và bán trên giao diện Antigravity, hệ thống cần thiết lập 3 mốc giá cho mỗi cổ phiếu:

Kịch bản Xấu nhất (
𝑃
Worst
P
Worst
	​

): Được lấy bằng Giá trị Xác sống (
𝑃
Zombie
P
Zombie
	​

 khi tăng trưởng 
𝑔
=
0
%
g=0%) hoặc mức định giá ở cận dưới dải lịch sử (
𝜇
𝑃
𝐸
−
2
𝜎
𝑃
𝐸
μ
PE
	​

−2σ
PE
	​

).   

Kịch bản Cơ sở / Giá Hợp lý (
𝑃
Base / Fair Value
P
Base / Fair Value
	​

): Được tính bằng trung bình có trọng số của các phương pháp định giá nội tại (Sticker Price, RNAV, RI, DCF) và định giá tương đối chuẩn ngành (
𝑃
/
𝐸
P/E, 
𝑃
/
𝐵
−
𝑅
𝑂
𝐸
P/B−ROE, 
𝐸
𝑉
/
𝐸
𝐵
𝐼
𝑇
𝐷
𝐴
EV/EBITDA). Ví dụ, nếu nhà phân tích tự tin vào dữ liệu tài sản và so sánh ngang hàng của VNM, có thể phân bổ trọng số 
20
%
20% cho phương pháp 
𝑃
/
𝐸
P/E, 
40
%
40% cho phương pháp 
𝑃
/
𝐵
−
𝑅
𝑂
𝐸
P/B−ROE và 
40
%
40% cho mô hình DCF/Sticker Price để tìm ra mức giá hợp lý hội tụ cuối cùng.   

Kịch bản Hưng phấn / Giá Bán Tương đối (
𝑃
Relative Sell / Overvalued
P
Relative Sell / Overvalued
	​

): Mốc giá mà tại đó đám đông trên thị trường đang trả một mức phí quá đắt so với tốc độ tăng trưởng thực tế của doanh nghiệp.   

Từ ba mốc này, Antigravity tự động tính toán Tỷ lệ Lợi nhuận trên Rủi ro (Win-Loss Ratio) tại mức thị giá hiện tại (
𝑃
Market
P
Market
	​

) theo công thức thực chiến:   

Tỷ lệ Win-Loss
=
𝑃
Base (Gi
a
ˊ
 Hợp l
y
ˊ
)
−
𝑃
Market (Thị gi
a
ˊ
)
𝑃
Market (Thị gi
a
ˊ
)
−
𝑃
Worst (Kịch bản X
a
ˆ
ˊ
u)
Tỷ lệ Win-Loss=
P
Market (Thị gi
a
ˊ
)
	​

−P
Worst (Kịch bản X
a
ˆ
ˊ
u)
	​

P
Base (Gi
a
ˊ
 Hợp l
y
ˊ
	​

)
	​

−P
Market (Thị gi
a
ˊ
)
	​

	​


Ví dụ thực tế với cổ phiếu lọc hóa dầu BSR: khi khoảng giá trị hợp lý được xác định từ 
𝑃
Worst
=
13.600
 đ
o
ˆ
ˋ
ng/cổ phi
e
ˆ
ˊ
u
P
Worst
	​

=13.600 đ
o
ˆ
ˋ
ng/cổ phi
e
ˆ
ˊ
u đến 
𝑃
Base
=
22.700
 đ
o
ˆ
ˋ
ng/cổ phi
e
ˆ
ˊ
u
P
Base
	​

=22.700 đ
o
ˆ
ˋ
ng/cổ phi
e
ˆ
ˊ
u và thị giá đang giao dịch ở mức 
16.000
 đ
o
ˆ
ˋ
ng/cổ phi
e
ˆ
ˊ
u
16.000 đ
o
ˆ
ˋ
ng/cổ phi
e
ˆ
ˊ
u, tỷ lệ Win-Loss đạt 
22.700
−
16.000
16.000
−
13.600
=
2
,
8
16.000−13.600
22.700−16.000
	​

=2,8 lần — nghĩa là nếu đúng, phần thưởng thu về gấp 
2
,
8
2,8 lần mức rủi ro nếu sai, kích hoạt tín hiệu mua có xác suất thắng cao.   

Ngược lại, đối với các cổ phiếu đang nắm giữ trong danh mục, Antigravity sẽ kích hoạt 3 Cấp độ Tín hiệu Bán (Automated Exit Triggers) dựa trên sự kết hợp giữa Giá trị Nội tại của Phil Town và Định giá Tương đối của thị trường:   

Cấp độ Tín hiệu Bán trên Antigravity	Điều kiện Kích hoạt Thuật toán (Logic Triggers)	Công thức Xác định Giá Bán Mục tiêu	Hành động Khuyến nghị cho Nhà đầu tư
Cấp 1: Chốt lời Từng phần (Valuation Stretch)	

Thị giá vượt qua Giá Hợp lý Hội tụ (
𝑃
Market
≥
𝑃
Base / Sticker
P
Market
	​

≥P
Base / Sticker
	​

) HOẶC tỷ lệ 
Win-Loss
<
0
,
5
Win-Loss<0,5.

	
𝑃
Sell 1
=
𝑃
Base
=
∑
𝑤
𝑖
𝑃
Fair
,
𝑖
P
Sell 1
	​

=P
Base
	​

=∑w
i
	​

P
Fair,i
	​

	

Dừng giải ngân mới; chốt lời 
30
%
−
50
%
30%−50% vị thế khi cổ phiếu không còn biên an toàn và tiến vào vùng định giá đầy đủ.


Cấp 2: Bán Toàn bộ theo Định giá Tương đối (Relative Overvaluation)	

Thị giá chạm cận trên dải độ lệch chuẩn 5 năm (
𝑃
/
𝐸
≥
𝜇
𝑃
𝐸
+
1
,
5
𝜎
𝑃
𝐸
P/E≥μ
PE
	​

+1,5σ
PE
	​

 hoặc 
𝑃
/
𝐵
≥
𝜇
𝑃
𝐵
+
1
,
5
𝜎
𝑃
𝐵
P/B≥μ
PB
	​

+1,5σ
PB
	​

) HOẶC chỉ số 
𝑃
𝐸
𝐺
≥
1
,
5
PEG≥1,5 (đối với cổ phiếu tăng trưởng).

	
𝑃
Sell 2
=
min
⁡
(
𝐸
𝑃
𝑆
Fwd
×
(
𝜇
𝑃
𝐸
+
1
,
5
𝜎
𝑃
𝐸
)
,
𝐸
𝑃
𝑆
Fwd
×
1
,
5
𝐺
)
P
Sell 2
	​

=min(EPS
Fwd
	​

×(μ
PE
	​

+1,5σ
PE
	​

),EPS
Fwd
	​

×1,5G)	

Bán 
100
%
100% vị thế để thu hồi vốn và lợi nhuận do thị giá đã phản ánh vượt quá xa tốc độ tăng trưởng tương lai.


Cấp 3: Bán Cắt lỗ / Thoát hàng Khẩn cấp do Gãy Nền tảng (Broken Moat)	

Vi phạm Quy tắc Bán số 1 của Phil Town: Doanh nghiệp không còn tuyệt vời (
𝑅
𝑂
𝐼
𝐶
ROIC tụt xuống dưới 
10
%
10% trong 2 năm, 
𝐹
-Score
≤
3
F-Score≤3, hoặc 
𝑍
-Score
Z-Score rơi vào vùng Nguy hiểm).

	

Bán ngay tại Giá Thị trường (
𝑃
Market
P
Market
	​

) bất kể đang lãi hay lỗ.

	

Thoát toàn bộ vị thế ngay lập tức để bảo vệ vốn gốc, tuyệt đối không bình quân giá xuống đối với cổ phiếu suy thoái cơ bản.

  
8. Tối ưu hóa Thuật toán Antigravity — Khắc phục Các Điểm mù Định lượng Thực chiến

Để công cụ trên Antigravity vận hành trơn tru trong môi trường dữ liệu thực tế tại Việt Nam mà không rơi vào bẫy "Đầu vào Rác, Đầu ra Rác" (Garbage In, Garbage Out) hay "Cộng dồn Bảo thủ" (Compounded Conservatism), bạn hãy lập trình bổ sung 4 hàm hiệu chỉnh toán học nâng cao sau đây vào lõi hệ thống:

1. Hàm Tăng trưởng Giảm dần (Decay Growth Rate) thay cho Hàm mũ Tuyến tính 10 năm

Trong công thức Sticker Price gốc của Phil Town (
𝐸
𝑃
𝑆
10
=
𝐸
𝑃
𝑆
0
×
(
1
+
𝑔
)
10
EPS
10
	​

=EPS
0
	​

×(1+g)
10
), việc giả định một công ty tăng trưởng đều đặn ở mức cao (ví dụ 
20
%
/
n
a
˘
m
20%/n
a
˘
m) suốt 10 năm liên tiếp thường dẫn đến sai số phóng đại rất lớn ở nửa cuối chu kỳ. Thay vào đó, hãy lập trình mô hình tăng trưởng hai nhịp ngay trong công thức Sticker Price: giữ tốc độ tăng trưởng 
𝑔
Rule1
g
Rule1
	​

 trong 5 năm đầu (giai đoạn nhìn thấy rõ đơn hàng và lợi thế cạnh tranh), sau đó áp dụng hệ số suy giảm tự nhiên 
𝛿
=
10
%
/
n
a
˘
m
δ=10%/n
a
˘
m từ năm thứ 6 đến năm thứ 10 hướng về tốc độ tăng trưởng GDP danh nghĩa của nền kinh tế:   

𝐸
𝑃
𝑆
10
 (T
o
ˆ
ˊ
i ưu)
=
𝐸
𝑃
𝑆
Thực
,
0
×
(
1
+
𝑔
Rule1
)
5
×
∏
𝑡
=
6
10
(
1
+
max
⁡
(
𝑔
GDP Danh ngh
ı
˜
a
,
𝑔
Rule1
×
(
1
−
0
,
10
)
𝑡
−
5
)
)
EPS
10 (T
o
ˆ
ˊ
i ưu)
	​

=EPS
Thực,0
	​

×(1+g
Rule1
	​

)
5
×
t=6
∏
10
	​

(1+max(g
GDP Danh ngh
ı
˜
a
	​

,g
Rule1
	​

×(1−0,10)
t−5
))
2. Hàm Làm mượt Tỷ lệ Trích Quỹ Khen thưởng Phúc lợi 3 năm (
𝜏
KTPL
τ
KTPL
	​

)

Do các doanh nghiệp niêm yết tại Việt Nam thường chỉ quyết toán chính thức Quỹ khen thưởng phúc lợi (Tài khoản 353) tại kỳ Đại hội đồng cổ đông thường niên và báo cáo kiểm toán năm, dữ liệu trích quỹ trên báo cáo tài chính Quý thường bị trống hoặc ghi nhận dồn cục. Để tránh việc chỉ số 
𝐸
𝑃
𝑆
Thực (TTM)
EPS
Thực (TTM)
	​

 trên Antigravity bị giật cục giữa các quý, thuật toán nên tính Tỷ lệ Trích lập Quỹ KTPL Bình quân Gia quyền 3 năm kiểm toán gần nhất (
𝜏
KTPL
τ
KTPL
	​

) và dùng tỷ lệ này để khấu trừ tự động cho các quý tiếp theo:   

𝜏
KTPL
=
∑
𝑦
=
𝑡
−
3
𝑡
−
1
S
o
ˆ
ˊ
 ti
e
ˆ
ˋ
n Tr
ı
ˊ
ch Qu
y
˜
 KTPL (TK 353)
𝑦
∑
𝑦
=
𝑡
−
3
𝑡
−
1
𝐿
𝑁
𝑆
𝑇
Cổ đ
o
ˆ
ng C
o
ˆ
ng ty mẹ
,
𝑦
τ
KTPL
	​

=
∑
y=t−3
t−1
	​

LNST
Cổ đ
o
ˆ
ng C
o
ˆ
ng ty mẹ,y
	​

∑
y=t−3
t−1
	​

S
o
ˆ
ˊ
 ti
e
ˆ
ˋ
n Tr
ı
ˊ
ch Qu
y
˜
	​

 KTPL (TK 353)
y
	​

	​

𝐸
𝑃
𝑆
Thực (TTM Chuẩn h
o
ˊ
a)
=
(
∑
𝑞
=
1
4
𝐿
𝑁
𝑆
𝑇
Qu
y
ˊ
 
𝑞
S
o
ˆ
ˊ
 CP Pha lo
a
˜
ng
)
×
(
1
−
𝜏
KTPL
)
EPS
Thực (TTM Chuẩn h
o
ˊ
a)
	​

=(
S
o
ˆ
ˊ
 CP Pha lo
a
˜
ng
∑
q=1
4
	​

LNST
Qu
y
ˊ
	​

 q
	​

	​

)×(1−τ
KTPL
	​

)
3. Hàm Kiểm định Thanh khoản Hàng tồn kho Bất động sản và Chất lượng Tài sản Ngân hàng

Đối với ngành Bất động sản: Để ngăn chặn việc thuật toán RNAV định giá cao những công ty có "hàng tồn kho chết" (dự án bị treo pháp lý nhiều năm không thể mở bán), Antigravity cần cài đặt một hệ số kích hoạt thanh khoản 
𝜅
Ph
a
ˊ
p l
y
ˊ
∈
[
0
,
1
]
κ
Ph
a
ˊ
p l
y
ˊ
	​

	​

∈[0,1] dựa trên tỷ lệ Người mua trả tiền trước (Mã 312 + 332) chia cho Hàng tồn kho (Mã 140). Nếu tỷ lệ này dưới 
5
%
5% và doanh thu bất động sản 2 năm liên tiếp sụt giảm, hệ số thặng dư quỹ đất 
𝜆
λ tự động bị ép về 
0
0 (chỉ định giá theo giá gốc sổ sách):
  

𝜆
Thực t
e
ˆ
ˊ
=
𝜆
Cơ sở
×
min
⁡
(
1
,
Người mua trả ti
e
ˆ
ˋ
n trước (M
a
˜
 312 + 332)
0
,
15
×
H
a
ˋ
ng t
o
ˆ
ˋ
n kho (M
a
˜
 140)
)
λ
Thực t
e
ˆ
ˊ
	​

=λ
Cơ sở
	​

×min(1,
0,15×H
a
ˋ
ng t
o
ˆ
ˋ
n kho (M
a
˜
 140)
Người mua trả ti
e
ˆ
ˋ
n trước (M
a
˜
 312 + 332)
	​

)

Đối với ngành Ngân hàng: Trước khi đưa Giá trị sổ sách (
𝐵
𝑉
𝑃
𝑆
0
BVPS
0
	​

) vào mô hình Thu nhập Thặng dư (
𝑅
𝐼
RI) hoặc định giá 
𝑃
/
𝐵
−
𝑅
𝑂
𝐸
P/B−ROE, hệ thống cần kiểm tra xem Quỹ dự phòng rủi ro tín dụng của ngân hàng đã bao phủ đủ 
100
%
100% Nợ xấu (Nhóm 3, Nhóm 4, Nhóm 5) hay chưa. Nếu Tỷ lệ bao phủ nợ xấu (
𝐿
𝐿
𝑅
<
100
%
LLR<100%), phần thiếu hụt dự phòng phải được trừ thẳng vào Vốn chủ sở hữu để có Giá trị sổ sách thực chất (
𝐵
𝑉
𝑃
𝑆
Thực
BVPS
Thực
	​

):
  

𝐵
𝑉
𝑃
𝑆
Thực (Bank)
=
𝐵
𝑉
𝑃
𝑆
B
a
ˊ
o c
a
ˊ
o
−
max
⁡
(
0
,
Tổng Nợ x
a
ˆ
ˊ
u (Nh
o
ˊ
m 3–5)
−
S
o
ˆ
ˊ
 dư Dự ph
o
ˋ
ng Rủi ro T
ı
ˊ
n dụng
)
×
(
1
−
𝑡
)
S
o
ˆ
ˊ
 lượng Cổ phi
e
ˆ
ˊ
u Lưu h
a
ˋ
nh
BVPS
Thực (Bank)
	​

=BVPS
B
a
ˊ
o c
a
ˊ
o
	​

−
S
o
ˆ
ˊ
 lượng Cổ phi
e
ˆ
ˊ
u Lưu h
a
ˋ
nh
max(0,Tổng Nợ x
a
ˆ
ˊ
u (Nh
o
ˊ
m 3–5)−S
o
ˆ
ˊ
 dư Dự ph
o
ˋ
ng Rủi ro T
ı
ˊ
n dụng)×(1−t)
	​

4. Phối hợp Tỷ trọng Định giá Nội tại và Định giá Tương đối trên Giao diện Antigravity

Để công cụ vừa giữ được triết lý đầu tư giá trị sâu sắc của Warren Buffett – Phil Town, vừa bám sát nhịp đập dòng tiền trên thị trường chứng khoán Việt Nam, đầu ra cuối cùng trên bảng điều khiển (Dashboard) của Antigravity nên kết hợp 70% Trọng số Định giá Nội tại (Intrinsic Valuation) và 30% Trọng số Định giá Tương đối (Relative Peer & Historical Valuation):   

𝑃
Fair Value Tổng hợp
=
0
,
70
×
𝑃
Nội tại Hội tụ theo Ng
a
ˋ
nh
+
0
,
30
×
𝑃
Tương đ
o
ˆ
ˊ
i Chuẩn Ng
a
ˋ
nh
P
Fair Value Tổng hợp
	​

=0,70×P
Nội tại Hội tụ theo Ng
a
ˋ
nh
	​

+0,30×P
Tương đ
o
ˆ
ˊ
i Chuẩn Ng
a
ˋ
nh
	​


Từ mức 
𝑃
Fair Value Tổng hợp
P
Fair Value Tổng hợp
	​

 này, hệ thống áp dụng tỷ lệ Biên An toàn Động (
𝑀
𝑂
𝑆
Động
MOS
Động
	​

 từ 
25
%
25% đến 
50
%
50% tùy theo phân hạng chất lượng từ Hạng 1 đến Hạng 3 ở Mục 5) để xuất ra Giá Mua Khuyến nghị (
𝑃
Buy
P
Buy
	​

), đồng thời hiển thị Tỷ lệ Win-Loss và Giá Bán Tương đối (
𝑃
Sell 1
,
𝑃
Sell 2
P
Sell 1
	​

,P
Sell 2
	​

). Cấu trúc thuật toán toàn diện này sẽ biến công cụ trên Antigravity của bạn thành một hệ thống phân tích đầu tư định lượng chuyên nghiệp, tự động thích nghi với từng nhóm ngành trên thị trường chứng khoán Việt Nam.   

---
# ==============================================================================
# PHỤ LỤC BỔ SUNG ĐẶC BIỆT (UPDATE 1):
# NÂNG CẤP THUẬT TOÁN ĐỊNH GIÁ THÍCH ỨNG CHU KỲ TTCK VIỆT NAM (2020–2026)
# KHẮC PHỤC BẪY CHIẾT KHẤU KÉP VÀ SỰ MÉO MÓ CHỈ SỐ BỀ MẶT VN-INDEX
# ==============================================================================

Dưới đây là **Kế hoạch Nghiên cứu Chuyên sâu** kèm theo **Toàn bộ Kết quả Phân tích Thực nghiệm và Hệ thống Công thức Toán học Cải tiến** để bạn cập nhật trực tiếp vào kiến trúc của công cụ định giá trên Antigravity.

### PHẦN 1: KẾ HOẠCH NGHIÊN CỨU CHUYÊN SÂU (RESEARCH PLAN)

Để giải quyết triệt để bài toán "đứng ngoài thị trường 10 năm" khi áp dụng công thức của Warren Buffett và Phil Town tại Việt Nam, cấu trúc nghiên cứu và nâng cấp thuật toán được chia làm 4 giai đoạn:

1. **Giai đoạn 1 — Giải phẫu Cấu trúc Chu kỳ và "Sự Méo mó Chỉ số" (Index Distortion) của TTCK Việt Nam:** Phân tích dữ liệu thực nghiệm giai đoạn 2020–2026 để bóc tách hiện tượng phân hóa dòng tiền, sự lệch pha giữa chỉ số VN-Index bề mặt (Headline Index) và phần lõi của thị trường (Core Market) khi bị chi phối bởi các cổ phiếu vốn hóa lớn có định giá đột biến.

2. **Giai đoạn 2 — Định lượng Toán học các Điểm mù của Công thức Rule #1 và Buffett Cổ điển:** Chứng minh bằng toán học tại sao việc kết hợp cứng nhắc tỷ suất chiết khấu $15\%$ và Biên an toàn $50\%$ lại tạo ra một ngưỡng chặn $P/E$ phi thực tế so với mặt bằng chi phí vốn ($K_e$) và cấu trúc định giá của các doanh nghiệp đầu ngành tại Việt Nam.

3. **Giai đoạn 3 — Thiết kế Thuật toán Định giá Thích ứng Chu kỳ (Cyclical-Adaptive Valuation Engine):** Xây dựng bộ công thức thay thế thông số tĩnh bằng: (a) Chỉ số Nhận diện Vùng Chu kỳ Thị trường Lõi (loại bỏ nhiễu cổ phiếu trụ), (b) Chênh lệch Lợi suất Thu nhập ($E/P$ so với lãi suất trái phiếu Chính phủ $R_f$), và (c) Biên an toàn co giãn động theo chất lượng doanh nghiệp và phân vị lịch sử.

4. **Giai đoạn 4 — Lập trình Ma trận Giải ngân Đa tầng (Multi-Tranche Execution) cho Antigravity:** Chuyển đổi đầu ra từ dạng nhị phân ("Mua / Đứng ngoài") sang hệ thống tự động phân bổ tỷ trọng vốn theo 3 vùng định giá kết hợp tỷ lệ Thắng/Thua (Win-Loss Ratio) và chu kỳ tích lũy 6–9 tháng.

### PHẦN 2: PHÂN TÍCH THỰC NGHIỆM CHU KỲ TTCK VIỆT NAM VÀ SỰ MÉO MÓ ĐỊNH GIÁ (2020–2026)

Khi nghiên cứu dữ liệu lịch sử và cấu trúc vận hành của thị trường chứng khoán Việt Nam đến năm 2026, có **3 quy luật cấu trúc** giải thích tại sao một công cụ định giá máy móc theo sách giáo khoa phương Tây sẽ hoàn toàn bị tê liệt:

#### 1. Hiện tượng "Xanh Vỏ Đỏ Lòng" và Sự Bóp nghẹt Định giá từ Cổ phiếu Trụ

Trên thị trường chứng khoán Việt Nam, điểm số và hệ số $P/E$ của VN-Index thường xuyên bị làm lệch bởi một vài cổ phiếu vốn hóa siêu lớn, che khuất hoàn toàn mức độ rẻ thực tế của phần lớn cổ phiếu trên sàn:

* **Sự tập trung cực đoan của dòng tiền:** Thống kê của FiinGroup chỉ ra rằng trong năm 2025, dù VN-Index ghi nhận hiệu suất cao nhất trong 8 năm khi tăng 517,71 điểm (+40,87%), nhưng riêng nhóm cổ phiếu họ Vingroup (với VIC tăng hơn 730% và VHM tăng hơn 210%) đã đóng góp tới 264 điểm — tương đương **51% tổng mức tăng của toàn chỉ số VN-Index**. Trong cả năm đó, chỉ có đúng **19% số cổ phiếu trên sàn (79/422 mã)** có mức tăng vượt chỉ số chung; dòng tiền nội và margin tập trung tới 50,3% giá trị giao dịch vào rổ VN30, khiến nhóm vốn hóa vừa (VNMID chiếm 38,7%) chỉ tăng khiêm tốn và nhóm vốn hóa nhỏ (VNSML chiếm 7,7%) gần như đi ngang.

* **Sự tách rời giữa Kinh tế Vĩ mô, Điểm số Chung và Cổ phiếu Lõi:** Bước sang năm 2026, ngay cả khi tăng trưởng GDP quý 3/2026 đạt mức ấn tượng 9,95%, dữ liệu từ đầu năm đến tháng 10/2026 cho thấy trong khi VN-Index bề mặt chỉ giảm nhẹ 2,6%, thì **chỉ số phần lõi của thị trường (sau khi loại bỏ nhóm Vingroup) đã sụt giảm gần 15%**.

* **Độ lệch chuẩn định giá khổng lồ giữa Bề mặt và Phần lõi:** Do đà tăng của một số cổ phiếu vốn hóa lớn giao dịch ở bội số cực cao, $P/E$ toàn thị trường bị đẩy lên 15,7x – 16,4x (cao hơn mức trung bình 10 năm là 14,9x) và $P/E$ nhóm Phi tài chính vọt lên tới **22,5x** — vùng rất cao trong lịch sử. Thế nhưng, khi loại bỏ nhóm Vingroup và Gelex ra khỏi mẫu tính toán, **$P/E$ của toàn bộ khối Phi tài chính còn lại thực chất chỉ ở mức 14,7x**, tiệm cận sát vùng đáy 5 năm là 12x (vùng định giá rẻ hiếm khi xuất hiện từ năm 2020 đến nay). Tương tự, tính toán của VNDirect và MoneyGain xác nhận nếu loại cổ phiếu VIC khỏi rổ chỉ số, $P/E$ trượt 12 tháng của VN-Index chỉ ở mức **12,1x – 12,5x**, thấp hơn 12% so với trung bình 3 năm (13,8x), trong khi $P/E$ dự phóng theo SSI Research lùi về mức rất hấp dẫn là **11,4x**. Ngay trong cùng nhóm bất động sản, trong khi VHM có $P/E$ là 7,5 lần ($P/B$ 2,3 lần, $ROE$ 33,8%) và VRE có $P/E$ là 7,8 lần ($ROE$ 15,5%), thì VIC lại giao dịch ở $P/E$ lên tới 73,1 lần và VPL ở mức 56,2 lần.

#### 2. Chu kỳ Đảo chiều Nhanh và Biên độ Dao động Nội niên 50%

Khác với thị trường Mỹ nơi các cổ phiếu bluechips tăng trưởng ổn định với biên độ hẹp, thị trường Việt Nam chịu tác động mạnh từ dòng tiền cá nhân trong nước và áp lực rút vốn từng đợt của khối ngoại (như năm 2025 khối ngoại bán ròng kỷ lục 135,3 nghìn tỷ đồng trên 3 sàn, gồm 113,5 nghìn tỷ qua khớp lệnh và 21,8 nghìn tỷ qua thỏa thuận). Hệ quả là dù nền tảng cơ bản của doanh nghiệp không thay đổi nhanh, **giá một cổ phiếu trung bình vẫn thường xuyên biến động trong biên độ lên tới 50% mỗi năm**. Tuy nhiên, các nhịp chiết khấu sâu về vùng đáy hoảng loạn toàn thị trường chỉ diễn ra chớp nhoáng, còn trong 80% thời gian của chu kỳ tăng trưởng (khi GDP tăng 7,3% – 9,95% và lợi nhuận doanh nghiệp tăng 14% – 15%/năm), thị trường sẽ được tái định giá ở vùng $P/E$ mục tiêu từ 12,5x đến 14,5x.

### PHẦN 3: GIẢI PHẪU 4 YẾU ĐIỂM CỦA PHƯƠNG PHÁP CŨ KHIẾN TOOL BÁO "ĐỨNG NGOÀI 10 NĂM"

Nếu bạn giữ nguyên công thức gốc của Phil Town và Buffett ở các phiên bản trước, thuật toán trên Antigravity sẽ mắc phải 4 lỗi thiết kế nghiêm trọng:

| **Yếu điểm của Phương pháp Cũ**                                     | **Cơ chế Gây Lỗi Toán học trên Antigravity**                                                                                                                                                                                                                                         | **Hệ quả Thực tế tại Thị trường Việt Nam**                                                                                                                                                                                                        |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Bẫy "Chiết khấu Kép" (MARR 15% + MOS 50%)**                    | Vừa chiết khấu dòng tiền ở mức 15%/năm (chia cho 4,0456 sau 10 năm), vừa cắt tiếp 50% giá trị nội tại. Quy đổi ra DCF, công thức này ép P/E mua tối đa xuống 3,33x (khi tăng trưởng 0%), 5,33x (khi tăng trưởng 10%/năm trong 5 năm) và 10,0x (khi tăng trưởng 22%/năm trong 5 năm). | Ngay cả ở vùng đáy 5 năm, P/E lõi của khối Phi tài chính Việt Nam cũng ở mức 12x – 14,7x. Đòi hỏi mua cổ phiếu tăng trưởng 10% – 20% ở mức P/E từ 5,33x – 10x khiến tool từ chối 99% cơ hội suốt 10 năm.                                          |
| **2. Tách rời Chi phí Vốn Thực tế (Ke) và Lợi suất Thu nhập (E/P)** | Dùng cố định lãi suất chiết khấu 15% bất chấp chu kỳ tiền tệ. Trong khi đó, lợi suất TPCP 10 năm của Việt Nam hiện chỉ ở mức 4,5% – 4,58% và ERP đã hạ nhiệt về 7,5%, đưa chi phí vốn cơ sở về quanh 10% – 12%.                                                                      | Khi định giá bằng lãi suất chiết khấu quá cao so với WACC/Ke thực tế rồi lại đòi MOS 50%, công cụ vô tình loại bỏ hoàn toàn các cổ phiếu có Lợi suất thu nhập (E/P) từ 8% – 10% (vốn đã cao gấp đôi lãi suất trái phiếu).                         |
| **3. Bị Đánh lừa bởi Chỉ số Bề mặt (Headline Index Blindness)**     | Nếu lấy P/E của VN-Index tổng thể (15,7x – 16,4x) hoặc P/E Phi tài chính bề mặt (22,5x) làm biến số nhận diện chu kỳ vĩ mô.                                                                                                                                                          | Khi VIC (P/E 73,1x) và VPL (P/E 56,2x) kéo P/E chung lên cao, tool sẽ phán đoán "Thị trường đang ở vùng đỉnh bong bóng" và khóa lệnh mua, dù 81% cổ phiếu trên sàn đang bị bán chiết khấu về vùng đáy định giá.                                   |
| **4. Định giá Tĩnh cho Cổ phiếu Compounders (Moat Mạnh)**           | Chờ đợi một mức giá rẻ mạt duy nhất (All-or-Nothing) cho các doanh nghiệp có con hào kinh tế độc quyền.                                                                                                                                                                              | Thị trường luôn trả phần bù chất lượng (Quality Premium) cho các doanh nghiệp đầu ngành có Moat rõ rệt. Nếu không có cơ chế giải ngân theo dải phân vị hàng năm và rải lệnh trong 6–9 tháng, nhà đầu tư sẽ vĩnh viễn đứng nhìn cổ phiếu tăng giá. |

### PHẦN 4: BỘ CÔNG THỨC KHẮC PHỤC TOÀN DIỆN CHO TOOL ANTIGRAVITY

Để công cụ Antigravity phát tín hiệu mua bán sát với thực tế thị trường Việt Nam trong mọi giai đoạn của chu kỳ mà vẫn giữ trọn tinh thần bảo toàn vốn của Buffett và Phil Town, bạn hãy lập trình thay thế bằng **4 Mô-đun Công thức Thích ứng Chu kỳ** dưới đây:

#### Mô-đun 1: Thuật toán Nhận diện Chu kỳ Thị trường Lõi (Core Market Regime & Earnings Yield Spread)

Tuyệt đối không dùng $P/E$ bề mặt của VN-Index làm tham chiếu vĩ mô. Hãy lập trình cho Antigravity tính **Hệ số Định giá Thị trường Lõi ($PE_{\text{Core}}$)** bằng cách lấy $P/E$ của rổ VN100 (vốn có $P/E$ thấp hơn VN-Index 2,3 lần và phản ánh sát sức khỏe doanh nghiệp đầu ngành) hoặc loại bỏ các mã vốn hóa lớn có $P/E > 40\text{x}$ (như VIC, VPL) ra khỏi mẫu số tính tổng lợi nhuận thị trường:

$$PE_{\text{Core Market}} = \frac{\sum_{i \in \text{VN-Index}, \; PE_i \le 40} \text{Vốn hóa}_i}{\sum_{i \in \text{VN-Index}, \; PE_i \le 40} LNST_{\text{Thực}, i}}$$

Từ $PE_{\text{Core Market}}$, hệ thống tính toán **Chênh lệch Lợi suất Thu nhập Thị trường (Market Earnings Yield Spread - $EYS_{\text{Market}}$)** bằng cách lấy đạo hàm ngược của $P/E$ (tức Lợi suất thu nhập $E/P$) trừ đi Lãi suất Trái phiếu Chính phủ Việt Nam kỳ hạn 10 năm ($R_f \approx 4,5\% - 4,58\%$):

$$EYS_{\text{Market}} = \left( \frac{1}{PE_{\text{Core Market}}} \right) - R_{f\text{ (10Y VGB)}}$$

* **Quy tắc phân loại chu kỳ tự động trên Antigravity:**
  
  * **Pha Rẻ Lịch sử / Đáy Chu kỳ ($PE_{\text{Core}} \le 12,0\text{x}$ hoặc $EYS_{\text{Market}} \ge 3,8\%$):** Như giai đoạn $P/E$ dự phóng lùi về 11,4x hay $P/E$ lõi chạm 12,1x. Hệ thống tự động mở rộng hạn mức giải ngân tối đa.
  
  * **Pha Hợp lý / Tăng trưởng Cơ sở ($12,0\text{x} < PE_{\text{Core}} \le 14,9\text{x}$ hoặc $2,2\% \le EYS_{\text{Market}} < 3,8\%$):** Tương ứng vùng $P/E$ mục tiêu 12,5x – 14,5x của VDSC và VNDirect và mức trung bình 10 năm (14,9x) của FiinGroup. Hệ thống kích hoạt chiến lược chọn lọc cổ phiếu theo dải điều chỉnh hàng năm.
  
  * **Pha Quá nhiệt / Đỉnh Chu kỳ ($PE_{\text{Core}} > 16,5\text{x}$ hoặc $EYS_{\text{Market}} < 1,5\%$):** Khi phần thưởng rủi ro cổ phiếu quá thấp so với lãi suất phi rủi ro (ví dụ khi tín dụng thắt chặt và lãi suất tiền gửi/trái phiếu tăng cao). Hệ thống tự động siết chặt Biên an toàn lên mức tối đa và ưu tiên giữ tiền mặt/trái phiếu.

#### Mô-đun 2: Công thức Sticker Price Thích ứng Chi phí Vốn Thực tế (Loại bỏ "Chiết khấu Kép")

Để khắc phục việc ép $P/E$ mua xuống mức phi lý 3,33x – 5,33x, thuật toán Antigravity tách công thức định giá của Phil Town và Buffett thành hai bước độc lập:

1. **Bước 2A — Tính Giá trị Nội tại Hợp lý ($P_{\text{Fair Intrinsic}}$) bằng Chi phí Vốn Thực tế ($K_e$) thay vì 15% cứng nhắc:** Theo đúng phương pháp thực chiến kết hợp Aswath Damodaran và Seth Klarman, giá trị hợp lý của doanh nghiệp phải được chiết khấu bằng chi phí vốn chủ sở hữu thực tế của doanh nghiệp đó (với ngưỡng sàn bảo thủ là $10\%/\text{năm}$) thay vì áp đặt $15\%$ cho mọi cổ phiếu:
   $$r_{\text{Discount}} = \max \left( 10,0\%, \; R_{f\text{ (4,5\%)}} + \beta_{\text{Bottom-up}} \times ERP_{\text{VN (7,5\%)}} \right)$$
   $$P_{\text{Fair Sticker (Adjusted)}} = \frac{EPS_{\text{Chuẩn hóa}} \times (1 + g_{\text{Decay}})^{10} \times PE_{\text{Future}}}{\left( 1 + r_{\text{Discount}} \right)^{10}}$$

2. **Bước 2B — Tính Biên An toàn Co giãn Động ($MOS_{\text{Adaptive}}$) từ 20% đến 50%:** Thay vì luôn cắt 50% (vốn làm mất sạch cơ hội ở nhóm cổ phiếu chất lượng cao), hệ thống tích hợp chuẩn Biên an toàn từ $15\% - 20\%$ (theo khung áp dụng Rule #1 hiện đại cho doanh nghiệp có Moat vững chắc) đến $30\% - 50\%$ (theo khung của Seth Klarman cho doanh nghiệp rủi ro cao hơn):
   $$MOS_{\text{Adaptive}} = MOS_{\text{Cơ sở theo Hạng Cổ phiếu}} - \Delta MOS_{\text{Chu kỳ Thị trường}}$$
   
   * Với **Cổ phiếu Hạng 1 (Compounders — đạt Big Five $\ge 10\%$, F-Score 8–9, Z-Score An toàn):** $MOS_{\text{Cơ sở}} = 25\%$. Nếu thị trường lõi đang ở vùng rẻ ($PE_{\text{Core}} \le 12,5\text{x}$), $\Delta MOS_{\text{Chu kỳ}} = 5\%$, đưa mức chiết khấu yêu cầu về **$20\%$**.
   
   * Với **Cổ phiếu Hạng 2 (Solid Value — đạt 4/5 Big Five, F-Score 6–7):** $MOS_{\text{Cơ sở}} = 35\%$ (chuẩn Seth Klarman).
   
   * Với **Cổ phiếu Hạng 3 (Chu kỳ / Vùng xám):** Giữ nguyên $MOS_{\text{Cơ sở}} = 50\%$ (chuẩn Phil Town cổ điển).

**Kiểm chứng sự khác biệt toán học:** Giả sử bạn định giá một doanh nghiệp đầu ngành tại Việt Nam (như FPT hoặc VNM) có $EPS_0 = 5.000\text{ đ}$, tăng trưởng dự kiến $15\%/\text{năm}$ ($\Rightarrow EPS_{10} = 20.227\text{ đ}$), $PE_{\text{Future}} = 18\text{x}$ ($\Rightarrow P_{10} = 364.100\text{ đ}$) và chi phí vốn thực tế $K_e = 11\%$:

* **Theo công thức cũ ($MARR = 15\%$ + $MOS = 50\%$):** $P_{\text{Sticker}} = 364.100 / (1,15)^{10} = 90.000\text{ đ} \implies P_{\text{MOS Cũ}} = 45.000\text{ đ}$ (Tương ứng đòi mua ở **$P/E = 9,0\text{x}$** — mức giá gần như không bao giờ xảy ra đối với một siêu cổ phiếu tăng trưởng 15%/năm, khiến nhà đầu tư đứng ngoài 10 năm).

* **Theo công thức cải tiến ($K_e = 11\%$ + $MOS_{\text{Hạng 1}} = 25\%$):** $P_{\text{Fair Sticker}} = 364.100 / (1,11)^{10} = 128.230\text{ đ} \implies P_{\text{Buy Mới}} = 128.230 \times (1 - 0,25) = 96.170\text{ đ}$ (Tương ứng vùng mua ở **$P/E = 19,2\text{x}$** và **$P/E\text{ dự phóng} = 16,7\text{x}$** — một vùng giá hoàn toàn khả thi xuất hiện đều đặn trong các nhịp điều chỉnh hàng năm trên sàn HOSE).

#### Mô-đun 3: Công thức Bắt Nhịp Điều chỉnh Hàng Năm (Annual 50% Volatility Capture) và Tỷ lệ Win-Loss

Vì mỗi cổ phiếu trên sàn chứng khoán Việt Nam thường dao động trong biên độ 50% mỗi năm quanh trục giá trị, Antigravity cần kết hợp Giá trị Nội tại với **Cận dưới Dải Độ lệch chuẩn 5 năm ($\mu - 1\sigma$)** của chính cổ phiếu đó để tạo ra điểm mua thực chiến hàng năm:

$$P_{\text{Dải Dưới Lịch sử (-1SD)}} = EPS_{\text{Dự phóng}} \times \left( \mu_{PE\text{ (5 năm)}} - 1,0 \times \sigma_{PE\text{ (5 năm)}} \right)$$

Đồng thời, thuật toán kiểm tra điều kiện an toàn qua **Tỷ lệ Thắng/Thua (Win-Loss Ratio)** và **Thời gian Hoàn vốn Linh hoạt (Adjusted Payback Time)**:

$$\text{Win-Loss Ratio} = \frac{P_{\text{Fair Value Hội tụ}} - P_{\text{Market}}}{P_{\text{Market}} - P_{\text{Worst}}} \ge 2,0$$

Trong đó, $P_{\text{Worst}}$ được xác định bằng cận dưới kịch bản xấu ($\mu_{PE} - 2\sigma_{PE}$ hoặc Giá trị Xác sống $P_{\text{Zombie}}$). Thay vì chỉ cho phép mua khi $\text{Payback Time} \le 8\text{ năm}$ cho mọi trường hợp, hệ thống mở rộng ngưỡng chấp nhận lên **$\text{Payback Time} \le 10\text{ năm}$** (tương đương chuẩn 10 Cap hoàn vốn 100% trong 10 năm) đối với các doanh nghiệp Hạng 1 có dòng tiền ổn định.

#### Mô-đun 4: Thuật toán Rải lệnh Giải ngân 3 Giai đoạn trong 6–9 Tháng (Time & Value Tranching)

Kinh nghiệm thực chiến khi đầu tư vào các doanh nghiệp chất lượng cao có con hào kinh tế (Quality Compounders) là không chờ đợi một điểm đáy tuyệt đối, mà **mua gom dần trong khoảng thời gian từ 6 đến 9 tháng** khi cổ phiếu đi vào vùng giá trị hợp lý, đồng thời kết hợp các chỉ báo kỹ thuật (như RSI phân kỳ dương, MACD cắt lên hoặc giá vượt MA20 sau nhịp rũ bỏ) như chính cách Phil Town sử dụng để tối ưu hóa điểm vào lệnh.

Bảng cấu hình luồng điều kiện (Logic Flow) dưới đây được thiết kế để bạn đưa thẳng vào mô-đun khuyến nghị hành động của Antigravity:

| **Vùng Giải ngân trên Antigravity**                                   | **Điều kiện Định giá Kích hoạt (Valuation Triggers)**                                                                                                                                           | **Bộ lọc Kỹ thuật & Chu kỳ Đi kèm**                                                                                                     | **Công thức Xác định Giá Mua & Tỷ trọng Giải ngân**                                                                     |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Tranche 1: Điểm Mua Tích lũy Hàng năm (Entry Zone - 30% Vốn)**      | Thị giá chiết khấu 15% – 20% so với Giá Hợp lý ($P_{\text{Fair}}$) HOẶC chạm đường $-1\text{SD}$ lịch sử; $\text{Win-Loss Ratio} \ge 1,8$; $\text{Payback Time} \le 10\text{ năm}$.             | Áp dụng cho Cổ phiếu Hạng 1 & 2; giải ngân chia làm 2–3 đợt cách nhau 4–6 tuần khi RSI(14) lùi về dưới 40 rồi vòng lên.                 | $P_{\text{Tranche 1}} = \max \left( P_{\text{Fair}} \times 0,80, \; P_{\text{Lịch sử (-1SD)}} \right)$                  |
| **Tranche 2: Điểm Mua Giá trị Chuẩn mực (Core Value Zone - 40% Vốn)** | Thị giá chiết khấu 30% – 35% so với $P_{\text{Fair}}$ (chuẩn Seth Klarman) HOẶC chạm Giá 10 Cap ($P_{\text{10Cap}}$); $\text{Win-Loss Ratio} \ge 2,8$; $\text{Payback Time} \le 8\text{ năm}$.  | Thường xuất hiện khi $PE_{\text{Core Market}}$ của VN-Index lùi về vùng 11,4x – 12,5x do khối ngoại bán ròng hoặc nhịp chỉnh trung hạn. | $P_{\text{Tranche 2}} = \max \left( P_{\text{Fair}} \times 0,65, \; P_{\text{10Cap}}, \; P_{\text{Payback 8Y}} \right)$ |
| **Tranche 3: Điểm Mua Khủng hoảng Chu kỳ (Deep MOS Zone - 30% Vốn)**  | Thị giá chiết khấu 50% theo công thức Rule #1 gốc ($MARR = 15\%$, $MOS = 50\%$) HOẶC chạm đường $-2\text{SD}$ / Giá trị Xác sống ($P_{\text{Zombie}}$); $\text{Payback Time} \le 6\text{ năm}$. | Xuất hiện trong các cú sốc thanh khoản toàn thị trường (chu kỳ 3–5 năm/lần); giải ngân toàn bộ phần tiền mặt dự phòng còn lại.          | $P_{\text{Tranche 3}} = \min \left( P_{\text{Sticker (15\%)}} \times 0,50, \; P_{\text{Lịch sử (-2SD)}} \right)$        |

### Tóm tắt Luồng Hoạt động Mới trên Giao diện Antigravity

Khi tích hợp 4 mô-đun này, công cụ của bạn sẽ vận hành theo một chu trình khép kín và thực tế hơn rất nhiều:

1. **Không bị đánh lừa bởi điểm số VN-Index:** Hệ thống tự động loại bỏ các cổ phiếu có $P/E$ đột biến (như VIC 73,1x, VPL 56,2x) để nhận diện đúng rằng mặt bằng $P/E$ lõi của thị trường (11,4x – 14,7x) đang ở vùng rất hợp lý để tìm kiếm cơ hội.

2. **Mở khóa điểm mua hàng năm cho cổ phiếu tốt:** Nhờ thay thế mức chiết khấu cố định $15\%$ bằng $K_e$ động ($10\% - 12\%$) và áp dụng $MOS$ co giãn ($20\% - 35\%$ cho nhóm Hạng 1 và Hạng 2), vùng mua **Tranche 1** và **Tranche 2** sẽ được kích hoạt đều đặn 1–2 lần mỗi năm khi cổ phiếu dao động trong biên độ 50%/năm của nó.

3. **Giữ vững kỷ luật phòng thủ của Buffett ở vùng đỉnh:** Khi cổ phiếu tăng vượt $P_{\text{Fair}}$ khiến tỷ lệ $\text{Win-Loss} < 0,5$ hoặc chạm dải trên $+1,5\text{SD}$, công cụ tự động phát tín hiệu chốt lời từng phần và chuyển vốn sang tiền gửi/trái phiếu hưởng lãi suất chờ nhịp chỉnh tiếp theo.
