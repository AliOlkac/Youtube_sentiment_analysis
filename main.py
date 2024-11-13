import pandas as pd
import streamlit as st
from keras.src.saving import load_model
from keras.src.utils import pad_sequences
from _0_comment_pull import pull_comments, get_video_id
from _1_data_cleaner import clean_text
from _3_predict_sentiment import predict_sentiment
import joblib


# Model ve tokenizer dosyalarını yükleyin
model = load_model('my_model.keras')
tokenizer = joblib.load('tokenizer.joblib')
label_encoder = joblib.load('label_encoder.joblib')

def main():
    # Arayüz başlığı ve açıklama
    st.title("Eğitim Videoları Yorum Analizi")
    st.write("Bu uygulama, seçtiğiniz bir eğitim videosunun yorumlarını analiz ederek pozitif ve negatif yorumları ayırır.")

    # Kullanıcıdan eğitim konusu al
    query = st.text_input("Eğitim Konusu Girin:")

    if query:
        st.write(f"Aranan Konu: **{query}**")

        # Yorumları çekme ve temizleme işlemi
        comments = pull_comments(get_video_id(query))
        comments['Cleaned_Comment'] = comments['Comment'].apply(clean_text)
        comments_df = pd.DataFrame(comments)


        # Yorumları analiz etme
        predictions = predict_sentiment(model,comments_df, tokenizer, label_encoder)


        # Sonuçları ekrana daha estetik şekilde yazdırma

        st.subheader("Yorumların Duygu Analizi:")
        st.write(predictions)


    else:
        st.write("Lütfen bir eğitim konusu girin.")



if __name__ == "__main__":
    main()
