# Nhóm 5: 
### HE2001148 - Đào Khôi Nguyên: Xử lý dữ liệu, Mô hình phân loại K-means
### HE200237 - Nguyễn Quốc Bảo: Phân tích và đánh giá dữ liệu
### HE200456 - Nguyễn Xuân Khang: Mô hình dự đoán Linear Regession
### HE200566 - Đỗ Trọng Quốc: Phân tích và đánh giá dữ liệu

## Bài báo cáo này có 3 phần
### PHẦN 1: MÔ TẢ BÀI TOÁN GỐC
### PHẦN 2: HƯỚNG DẪN KỸ THUẬT
### PHẦN 3: QUÁ TRÌNH & KẾT QUẢ
### File Chính chứa toàn bộ code: shop.ipynb

# PHẦN 1: MÔ TẢ BÀI TOÁN GỐC

### 1. TÊN DỰ ÁN
   Phân tích và Dự đoán Yếu tố Thành công của Gian hàng Thương mại Điện tử (E-commerce Shop Analysis)

### 2. BỐI CẢNH (CONTEXT)
   Thị trường thương mại điện tử (Shopee, Lazada...) đang cạnh tranh khốc liệt. Các nhà bán hàng mới (New Sellers) thường gặp khó khăn trong việc định hình chiến lược vận hành để đạt được sự uy tín và thu hút khách hàng ngay từ đầu.

### 3. CÁC BÊN LIÊN QUAN (STAKEHOLDERS)
   - Client (Khách hàng): Nhà đầu tư cá nhân hoặc chủ doanh nghiệp nhỏ chuẩn bị mở shop thời trang online.
   - Data Scientist (Nhóm phân tích): Chịu trách nhiệm xử lý dữ liệu để đưa ra insight và mô hình dự báo.

### 4. VẤN ĐỀ KINH DOANH (BUSINESS PROBLEM)
   Client đặt câu hỏi: "Tôi muốn mở shop bán hàng online. Nhưng tôi không biết yếu tố nào quyết định sự thành công (uy tín) của một shop? Liệu việc trả lời tin nhắn nhanh, có ảnh hưởng đến việc khách hàng đánh giá 5 sao cho tôi không?"

### 5. MỤC TIÊU KHOA HỌC DỮ LIỆU (DATA SCIENCE GOALS)
   - Phân tích khám phá (EDA): Tìm ra mối tương quan giữa các biến số (Tốc độ phản hồi, Vị trí shop, Số lượng hàng...) với biến mục tiêu (Rating Star, Lượng người theo dõi).
   - Phân cụm (Clustering): Nhóm các shop có đặc điểm tương đồng để định vị phân khúc.
   - Dự báo (Prediction): Xây dựng mô hình ước tính độ uy tín dựa trên thông số vận hành.


# PHẦN 2: HƯỚNG DẪN KỸ THUẬT

## PROJECT: Optimizing E-commerce Reputation (ASM1)

### I. GIỚI THIỆU
   Dự án này sử dụng dữ liệu lịch sử các shop trên sàn TMĐT để giúp người bán mới tối ưu hóa vận hành. 
   Mục tiêu: Trả lời câu hỏi về sự ảnh hưởng của "Response Rate" và "Location" tới "Rating".

### II. CẤU TRÚC THƯ MỤC DỰ ÁN (ASM1/)
   1. Dữ liệu:
      - shop_detail.csv: File dữ liệu gốc chứa thông tin các shop.

   2. Notebooks:
      - shop.ipynb: Phân tích dữ liệu (EDA), làm sạch dữ liệu và trực quan hóa cơ bản, chứa toàn bộ phần code toàn project.
      
   3. Modules:
      - text_processer.py: Xử lý dữ liệu văn bản (tên shop, mô tả...).
      - k_means.py: Thuật toán phân cụm shop.
      - modeling.py: Xây dựng phân tích dữ liệu.
      - evaluation.py: Đánh giá độ chính xác của mô hình.
      - prediction.ipynb: Quy trình chính để chạy các mô hình máy học.

   4. Khác:
      - .gitignore: Cấu hình git.
      - README.txt: Bài báo cáo này.

### III. YÊU CẦU HỆ THỐNG
   - Ngôn ngữ: Python >= 3.11.0
   - Thư viện cần thiết: pandas, numpy, scikit-learn, matplotlib, seaborn, jupyter.
   - Cài đặt: pip install pandas numpy scikit-learn matplotlib seaborn

### V. PHƯƠNG PHÁP TIẾP CẬN (METHODOLOGY)
   1. Data Preprocessing: Xử lý giá trị thiếu (Nall), chuẩn hóa dữ liệu số, mã hóa dữ liệu văn bản.
   2. Clustering: Sử dụng K-Means để tìm ra các nhóm shop đặc trưng (VD: Nhóm shop VIP, Nhóm shop mới...).
   3. Modeling: Sử dụng các thuật toán học có giám sát để dự đoán Rating dựa trên:
      - response_rate (Tỷ lệ phản hồi)
      - shop_location (Vị trí)
      - item_count (Số lượng sản phẩm)
      - join_time (Thâm niên)

### VI. KẾT QUẢ MONG ĐỢI
   Cung cấp bằng chứng định lượng để khuyên Client nên tập trung vào việc cải thiện tốc độ phản hồi hay mở rộng kho hàng để đạt được đánh giá 5 sao.

## PHẦN 3: QUÁ TRÌNH & KẾT QUẢ

### Xử lý dữ liệu:
**Nhìn qua dữ liệu**
<img width="1795" height="704" alt="image" src="https://github.com/user-attachments/assets/f973499c-6573-4f44-a9ad-e2a112801c9a" />
**Loại bỏ các cột không cần thiết**
<img width="1777" height="375" alt="image" src="https://github.com/user-attachments/assets/e55352f0-b98c-4bc8-ab4e-b80b2aeb7d86" />
**Kiểm tra số lượng Null của các cột và kiểm tra kiểu dữ liệu, nhận thấy rằng có các giá trị Null và kiểu dữ liệu của các cột đã chính xác**
<img width="1765" height="513" alt="image" src="https://github.com/user-attachments/assets/3ba36477-a344-455c-81d3-e68de0a0541b" />
**Xử lý các giá trị Null, suy đoán rằng các cột Null là các shop ảo do đa phần Null ở 'description', 'rating_star', 'response_rate', đồng thời xoá các shop không bán item nào (item_count = 0)**
<img width="1774" height="536" alt="image" src="https://github.com/user-attachments/assets/fb46ec12-ed66-4da6-9254-e0a297eebdbd" />
**Kết quả**
<img width="1772" height="601" alt="image" src="https://github.com/user-attachments/assets/8c63276b-3550-48a2-957e-2f706ff97b53" />
<img width="1791" height="523" alt="image" src="https://github.com/user-attachments/assets/1d896281-c91b-4b31-bfe8-51a102c8a629" />

## Mô hình Phân cụm K-means (k_means.py)

### 1. Mục tiêu áp dụng
Dữ liệu thu thập từ sàn thương mại điện tử (TMĐT) có đặc điểm là hỗn tạp, bao gồm rất nhiều ngành hàng khác nhau (Sách, Điện tử, Thú cưng, Thời trang...).

Thay vì gán nhãn thủ công (tốn kém thời gian và nhân lực), nhóm sử dụng thuật toán học máy không giám sát **K-Means Clustering** kết hợp với kỹ thuật **Xử lý ngôn ngữ tự nhiên (NLP)** để tự động gom nhóm và định danh các shop dựa trên phần mô tả (`description`).

### 2. Phương pháp kỹ thuật (Methodology)
Quy trình thực hiện trong file `k_means.py` bao gồm 3 bước chính:

**Bước 1: Vector hóa (Text Vectorization)**
* **Làm sạch dữ liệu:** Nhóm đã xây dựng một bộ từ điển `stop_words` tùy chỉnh (bao gồm tiếng Việt và các ký tự đặc biệt, các từ chung chung như `...`, `và`, `là`, `https`, `shopee`...) để loại bỏ nhiễu.
* **Vector hóa:** Sử dụng kỹ thuật **TF-IDF (Term Frequency - Inverse Document Frequency)** để chuyển đổi dữ liệu văn bản (cột `description`) thành các vector số học.
* **Cấu hình:** Sử dụng tham số `ngram_range=(1, 2)` để mô hình hiểu được cả cụm từ (ví dụ: "áo thun", "thời trang") thay vì chỉ từ đơn lẻ, giúp tăng độ chính xác ngữ nghĩa.

**Bước 2: Phân cụm (Clustering)**
* Sử dụng thuật toán **K-Means** từ thư viện `scikit-learn`.
* **Số lượng cụm (K):** Sau quá trình thử nghiệm với các giá trị K khác nhau, nhóm quyết định chọn **K=3**. Lý do là dữ liệu thực tế thường phân tách thành 3 nhóm lớn: 
    1. Nhóm shop nước ngoài/mô tả tiếng Anh.
    2. Nhóm shop tạp hóa/ngành hàng khác (Sách, Sim thẻ...).
    3. Nhóm shop Thời trang chuyên biệt (Mục tiêu).

**Bước 3: Định danh cụm tự động (Cluster Labeling)**
* Đây là cải tiến quan trọng của nhóm so với phương pháp thông thường. Sau khi phân cụm, thuật toán sẽ trích xuất **Top Keywords** (các từ khóa xuất hiện nhiều nhất và có trọng số cao nhất) của từng cụm.
* Hệ thống tự động so khớp Top Keywords này với bộ từ điển chuyên ngành `clothing_keywords` (gồm: *thời trang, fashion, brand, áo, quần, váy...*).
* Cụm nào chứa nhiều từ khóa trùng khớp nhất sẽ được hệ thống **tự động gán nhãn là Shop Thời trang** để đưa vào mô hình dự đoán.

**Kết quả thực nghiệm**
Sau khi chạy mô hình trên tập dữ liệu đã làm sạch, thuật toán K-Means đã phân tách dữ liệu thành 3 cụm với các đặc điểm từ khóa rõ rệt:
<img width="1282" height="533" alt="image" src="https://github.com/user-attachments/assets/6d5b0dd1-66d6-44f8-9f26-c4c78ea879f7" />

## Phân tích và đánh giá dữ liệu (modleing.py và evaluation.py)

### 1. Mục tiêu
   - Xác định các yếu tố ảnh hưởng đến hiệu quả của shop
   - Đánh giá mối quan hệ giữa:
      + Hành vi shop (tốc độ phản hồi)
      + Vị trí địa lý
      + Ngành hàng
   - Với các chỉ số kết quả:
      + Rating
      + Follower

### 2. Lý do chọn Modeling mô tả
   - Dữ liệu mang tính thống kê & quan sát
   - Không có biến mục tiêu rõ ràng để dự đoán
   - Mục tiêu chính là:
      + So sánh
      + Đánh giá xu hướng
      + Rút ra insight
### 3. Các kỹ thuật Modeling được sử dụng
   - Correlation Analysis
      + Đo lường mối quan hệ giữa (response_rate và rating_star)
   - Group-based Aggregation
      + Gom nhóm shop theo (Thành phố và Ngành hàng)
      + Tính (Rating trung bình và Follower trung bình)
   - Comparative Analysis
      + So sánh kết quả giữa các nhóm
      + Xác định nhóm nổi bật

### 4. Kết quả
* Tương quan giữa Tỉ lệ phản hồi vs Rating:
  - Hệ số tương quan dương nhưng thấp
  - Cho thấy:
       + Phản hồi nhanh giúp cải thiện hình ảnh shop
       + Nhưng không quyết định hoàn toàn rating
-> Chất lượng sản phẩm/dịch vụ vẫn là yếu tố cốt lõi
<img width="775" height="659" alt="Screenshot 2026-01-23 105426" src="https://github.com/user-attachments/assets/dce29d0f-010b-4818-acf2-d5bd5b73416b" />

* So sánh theo khu vực
  - Rating trung bình:
       + Hà Nội ≈ TP.HCM ≈ 4,9
  - Chênh lệch không đáng kể
-> Địa điểm mở shop không tạo lợi thế rõ ràng về đánh giá (rating)
<img width="961" height="555" alt="Screenshot 2026-01-23 105524" src="https://github.com/user-attachments/assets/fe91ce35-24fd-47aa-b1d7-8e6dd77e9eda" />

*Phân tích theo ngành hàng
   - Thời trang~61,900 follower
   - Bán lẻ / Thương mại tổng hợp:~54,700 follower
   - Không rõ ngành: ~33,400 follower
-> Ngành hàng có ảnh hưởng mạnh đến khả năng thu hút người theo dõi

### 5. Bài học và lời khuyên rút ra từ Modeling
   - Mặt hàng là yếu tố ảnh hưởng mạnh nhất
   - Tốc độ phản hồi chỉ hỗ trợ, không quyết định
   - Vị trí địa lý không phải lợi thế cạnh tranh
