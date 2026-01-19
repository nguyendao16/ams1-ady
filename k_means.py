import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

stop_words_raw = [
    '...', '..', '-', '_', '/', '|', '(', ')', '[', ']', '{', '}', '!', '?', ',', '.', ':', ';',
    'và', 'của', 'là', 'các', 'có', 'được', 'cho', 'với', 'này', 'đã', 'trong', 'từ', 'hay',
    'để', 'những', 'một', 'khi', 'đến', 'tại', 'về', 'trên', 'do', 'ra', 'sẽ', 'còn', 'đang',
    'hoặc', 'như', 'đều', 'đó', 'nếu', 'rất', 'đây', 'cũng', 'theo', 'nhiều', 'thì', 'nhưng',
    'chúng', 'bị', 'vì', 'nên', 'mà', 'lại', 'vẫn', 'thường', 'cả', 'mọi', 'mỗi', 'ít',
    'hơn', 'kém', 'tôi', 'ta', 'chúng tôi', 'chúng ta', 'bạn', 'anh', 'chị', 'em', 'khách',
    'người', 'ai', 'gì', 'nào', 'sao', 'đâu', 'đấy', 'kia', 'khá', 'cực', 'siêu', 'hơi', 'quá',
    'lắm', 'vô cùng', 'thật', 'thực sự', 'ok', 'oke', 'okay', 'good', 'nice', 'perfect',
    'hôm nay', 'hôm qua', 'ngày mai', 'hiện tại', 'bây giờ', 'lúc này', 'sắp', 'vừa', 'mới',
    'xong', 'shop', 'store', 'cửa hàng', 'bán', 'mua', 'order', 'đặt hàng', 'giao', 'ship',
    'vận chuyển', 'liên hệ', 'ib', 'inbox', 'comment', 'cam kết', 'đảm bảo', 'uy tín',
    'vn', 'com', 'https', 'www', 'facebook', 'zalo', 'hotline', 'sđt', 'chính hãng', 'sản phẩm'
]

stop_words = set()
for w in stop_words_raw:
    stop_words.update(w.split())
stop_words = list(stop_words)

clothing_keywords = [
    'thời trang', 'fashion', 'brand', 'hiệu', 'áo phông'
    'áo', 'quần', 'váy', 'đầm', 'khoác', 'jacket', 'coat', 'vest', 'len', 'sweater',
    'hoodie', 'polo', 'suit', 'bikini', 'swimwear', 'bra', 'lót',
    'jeans', 'kaki', 'short', 'legging', 'skirt',
    'giày', 'dép', 'sandal', 'boot', 'sneaker', 'guốc',
    'túi', 'balo', 'ví', 'thắt lưng', 'mũ', 'nón', 'khăn'
]

def k_means(data: list):
    tfidf = TfidfVectorizer(
        max_features=2000, 
        stop_words=stop_words, 
        ngram_range=(1, 2), 
        min_df=0.005
    )
    X_text = tfidf.fit_transform(data)

    k = 3 
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_text)

    order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]
    terms = tfidf.get_feature_names_out()
    
    for i in range(k):
        top_terms = [terms[ind] for ind in order_centroids[i, :15]]
        print(f"\nCluster {i}:")
        print(f"Top keywords: {', '.join(top_terms)}")

        matches = [kw for kw in clothing_keywords if any(kw in term for term in top_terms)]
        
        if len(matches) >= 2:
            print(f"=> Cụm này CHẮC CHẮN là Shop Thời Trang (Khớp: {', '.join(matches)})")
        elif len(matches) == 1:
            print(f"=> Cụm này CÓ THỂ là Shop Thời Trang (Khớp: {', '.join(matches)})")
        else:
            print("❌ => Cụm này KHÔNG PHẢI Shop Thời Trang")

    print("-" * 50)
    return kmeans.labels_.tolist()