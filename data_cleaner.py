import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

# Stop words Türkçe olarak indir
turkish_stop_words = set(stopwords.words('turkish'))

# Yorumları yükle
comments_df = pd.read_csv('youtube_comments.csv')


# Yorum temizleme fonksiyonu
def clean_text(text):
    # Küçük harfe çevir
    text = text.lower()

    # Noktalama işaretlerini kaldır
    text = re.sub(r'[^\w\s]', '', text)

    # Türkçe stop words kaldır
    text = ' '.join([word for word in text.split() if word not in turkish_stop_words])

    return text


# Yorumları temizle
comments_df['Cleaned_Comment'] = comments_df['Comment'].apply(clean_text)

# Temizlenmiş yorumları kaydet
comments_df.to_csv('cleaned_youtube_comments.csv', index=False)
print("Yorumlar başarıyla temizlendi ve kaydedildi.")
