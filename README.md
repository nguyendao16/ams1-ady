# PHẦN 1: MÔ TẢ BÀI TOÁN GỐC (BUSINESS UNDERSTANDING)

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


# PHẦN 2: HƯỚNG DẪN KỸ THUẬT (README)

## PROJECT: E-commerce Shop Success Analysis (ASM1)

### I. GIỚI THIỆU
   Dự án này sử dụng dữ liệu lịch sử các shop trên sàn TMĐT để giúp người bán mới tối ưu hóa vận hành. 
   Mục tiêu: Trả lời câu hỏi về sự ảnh hưởng của "Response Rate" và "Location" tới "Rating".

### II. CẤU TRÚC THƯ MỤC DỰ ÁN (ASM1/)
   
   1. Dữ liệu:
      - shop_detail.csv: File dữ liệu gốc chứa thông tin các shop.

   2. Notebooks (Dành cho chạy thử nghiệm và báo cáo):
      - shop.ipynb: Phân tích dữ liệu (EDA), làm sạch dữ liệu và trực quan hóa cơ bản.
      - prediction.ipynb: Quy trình chính để chạy các mô hình máy học.

   3. Source Code (Modules):
      - text_processer.py: Xử lý dữ liệu văn bản (tên shop, mô tả...).
      - k_means.py: Thuật toán phân cụm shop.
      - modeling.py: Xây dựng và huấn luyện mô hình (Regression/Classification).
      - evaluation.py: Đánh giá độ chính xác của mô hình.

   4. Khác:
      - .gitignore: Cấu hình git.
      - README.txt: File hướng dẫn này.

### III. YÊU CẦU HỆ THỐNG
   - Ngôn ngữ: Python >= 3.11.0
   - Thư viện cần thiết: pandas, numpy, scikit-learn, matplotlib, seaborn, jupyter.
   - Cài đặt: pip install pandas numpy scikit-learn matplotlib seaborn

### IV. HƯỚNG DẪN SỬ DỤNG

   Bước 1: Khám phá dữ liệu
   - Mở file 'shop.ipynb'.
   - Chạy các cell để xem phân bố dữ liệu, biểu đồ tương quan giữa Tốc độ phản hồi và Rating.

   Bước 2: Chạy mô hình (Phân cụm & Dự đoán)
   - Mở file 'prediction.ipynb'.
   - Notebook này sẽ gọi các hàm từ các file .py (text_processer, k_means, modeling) để thực hiện:
     + Tiền xử lý dữ liệu thô.
     + Phân nhóm các shop (K-Means Clustering).
     + Huấn luyện mô hình dự đoán Rating.

### V. PHƯƠNG PHÁP TIẾP CẬN (METHODOLOGY)
   1. Data Preprocessing: Xử lý giá trị thiếu (NaN), chuẩn hóa dữ liệu số, mã hóa dữ liệu văn bản.
   2. Clustering: Sử dụng K-Means để tìm ra các nhóm shop đặc trưng (VD: Nhóm shop VIP, Nhóm shop mới...).
   3. Modeling: Sử dụng các thuật toán học có giám sát để dự đoán Rating dựa trên:
      - response_rate (Tỷ lệ phản hồi)
      - shop_location (Vị trí)
      - item_count (Số lượng sản phẩm)
      - join_time (Thâm niên)

### VI. KẾT QUẢ MONG ĐỢI
   Cung cấp bằng chứng định lượng để khuyên Client nên tập trung vào việc cải thiện tốc độ phản hồi hay mở rộng kho hàng để đạt được đánh giá 5 sao.

### PHẦN 3: KẾT QUẢ

## Kết quả sau khi lọc dữ liệu:
<img width="1772" height="601" alt="image" src="https://github.com/user-attachments/assets/8c63276b-3550-48a2-957e-2f706ff97b53" />
Đảm bảo rằng các cột đã được đưa về đúng kiểu giữ liệu:
<img width="1791" height="523" alt="image" src="https://github.com/user-attachments/assets/1d896281-c91b-4b31-bfe8-51a102c8a629" />

