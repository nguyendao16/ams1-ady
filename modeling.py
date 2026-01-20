import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from k_means import k_means

# 1. Đọc dữ liệu
data = pd.read_csv('shop_detail.csv')

# --- PHÂN TÍCH 1: Tương quan giữa Response Rate và Rating Star ---
plt.figure(figsize=(8, 6))
correlation_data = data[['rating_star', 'response_rate']].dropna()
sns.heatmap(correlation_data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Heatmap: Correlation between Rating Star and Response Rate')
plt.show()

# --- PHÂN TÍCH 2: So sánh Hà Nội vs TP. Hồ Chí Minh ---
# Lọc dữ liệu cho 2 thành phố chính
city_comparison = data[data['shop_location'].isin(['Hà Nội', 'TP. Hồ Chí Minh'])]
avg_rating_city = city_comparison.groupby('shop_location')['rating_star'].mean()

print("Rating trung bình theo thành phố:")
print(avg_rating_city)

# Vẽ biểu đồ so sánh
avg_rating_city.plot(kind='bar', color=['skyblue', 'orange'])
plt.ylabel('Average Rating Star')
plt.title('Average Rating: Hanoi vs TP.HCM')
plt.show()

# --- PHÂN TÍCH 3: Phân tích ngành hàng (sử dụng K-means từ k_means.py) ---
# Bước này sử dụng hàm k_means đã định nghĩa để phân loại shop dựa trên mô tả
descriptions = data['description'].fillna('').astype(str).tolist()
data['cluster_label'] = k_means(descriptions)

# Ở đây ta phân tích follower_count trung bình cho mỗi nhóm
category_analysis = data.groupby('cluster_label')['follower_count'].mean().sort_values(ascending=False)
print("\nFollower trung bình theo nhóm ngành hàng (Cluster):")
print(category_analysis)