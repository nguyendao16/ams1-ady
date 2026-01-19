import pandas as pd

# ĐỌC DỮ LIỆU
df = pd.read_csv("shop_detail.csv")

print("\n---------- BƯỚC 8: EVALUATION ----------")

# 1. Tốc độ phản hồi & Rating
# (dựa trên kết quả phân tích ở phần trước)
print("\n1. Tốc độ phản hồi và Rating shop")
print(f"- Hệ số tương quan giữa response_rate và rating_star: 0.16")
print("- Kết quả cho thấy tốc độ phản hồi có ảnh hưởng dương tới Rating.")
print("- Tuy nhiên mức độ ảnh hưởng không mạnh, Rating còn phụ thuộc vào chất lượng sản phẩm và dịch vụ.")
print("Điều này có thể được giải thích là rating còn phụ thuộc vào nhiều yếu tố khác như chất lượng sản phẩm, giá cả, dịch vụ hậu mãi và trải nghiệm mua hàng tổng thể.")
print("")

# 2. Hà Nội vs TP.HCM
print("\n2. So sánh Rating trung bình theo thành phố")
print(f"- Hà Nội: 4.900992")
print(f"- TP. Hồ Chí Minh: 4.901102")
print("- Rating trung bình giữa hai thành phố gần như không có sự khác biệt.")
print("- Điều này cho thấy vị trí địa lý không ảnh hưởng đáng kể đến đánh giá của khách hàng.")

# 3. Ngành hàng & follower
# (dựa trên kết quả phân tích ở phần trước)
industry_analysis = {
    "Retail / General Commerce": 61918.812344,
    "Fashion": 54732.453014,
    "General / No clear industry": 33438.494505
}
print("\n3. Ngành hàng và lượng follower trung bình")
for industry, value in industry_analysis.items():
    print(f"- {industry}: {value:,.0f} follower")
top_industry = max(industry_analysis, key=industry_analysis.get)
print(f"- Ngành hàng thu hút follower cao nhất: {top_industry}")
print("- Ngành bán lẻ / thương mại tổng hợp có lượng follower trung bình cao nhất (~61,919 follower).\n"
    "- Ngành thời trang đứng thứ hai (~54,732 follower).\n"
    "- Nhóm shop không rõ ngành nghề có lượng follower thấp nhất (~33,438 follower).")

# KẾT LUẬN
print("\n========== KẾT LUẬN ==========")
print("- Tốc độ phản hồi có ảnh hưởng nhẹ tới Rating shop.")
print("- Địa điểm mở shop không tạo khác biệt đáng kể về Rating.")
print("- Ngành hàng là yếu tố quan trọng ảnh hưởng tới khả năng thu hút follower.")
print("Để cải thiện hiệu quả kinh doanh, shop nên tập trung vào chất lượng sản phẩm, định vị ngành hàng rõ ràng và trải nghiệm khách hàng, thay vì chỉ chú trọng vào tốc độ phản hồi.")