import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from k_means import k_means

df = pd.read_csv('shop_detail.csv')

plt.figure(figsize=(8, 6))
correlation_data = df[['rating_star', 'response_rate']].dropna()
sns.heatmap(correlation_data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Heatmap: Correlation between Rating Star and Response Rate')
plt.show()

city_comparison = df[df['shop_location'].isin(['Hà Nội', 'TP. Hồ Chí Minh'])]
avg_rating_city = city_comparison.groupby('shop_location')['rating_star'].mean()

print("Rating trung bình theo thành phố:")
print(avg_rating_city)

avg_rating_city.plot(kind='bar', color=['skyblue', 'orange'])
plt.ylabel('Average Rating Star')
plt.title('Average Rating: Hanoi vs TP.HCM')
plt.show()

descriptions = df['description'].fillna('').astype(str).tolist()
df['cluster_label'] = k_means(descriptions)

category_analysis = df.groupby('cluster_label')['follower_count'].mean().sort_values(ascending=False)
print("\nFollower trung bình theo nhóm ngành hàng (Cluster):")
print(category_analysis)