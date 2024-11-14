import pandas as pd
import streamlit as st
from keras.src.saving import load_model
from keras.src.utils import pad_sequences
from _0_comment_pull import pull_comments, get_video_id
from _1_data_cleaner import clean_text
from _3_predict_sentiment import predict_sentiment
import joblib
import matplotlib.pyplot as plt

# Sayfa başlığını ve simgesini ayarla
st.set_page_config(page_title="AliOlkac202113709053", page_icon="♣️")

# Model ve tokenizer dosyalarını yükleyin
model = load_model('my_model.keras')
tokenizer = joblib.load('tokenizer.joblib')
label_encoder = joblib.load('label_encoder.joblib')


def main():
    # Arayüz başlığı ve açıklama
    st.title("Eğitim Videoları Yorum Analizi")
    st.write("Bu uygulama, seçtiğiniz bir eğitim videosunun yorumlarını analiz ederek pozitif ve negatif yorumları ayırır.")

    # Yan menü oluşturma
    with st.sidebar:
        theme = st.radio("Tema Seçimi", ("Koyu", "Açık"))
        query = st.text_input("Eğitim Konusu Girin:")

        # Tema değişikliği için ayar
        if theme == "Koyu":
            st.markdown(
                """
                <style>
                .stApp { background-color: #262730; color: white; }
                </style>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                """
                <style>
                .stApp { background-color: white; color: black; }
                </style>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            """
            <style>
            input[type="text"]::placeholder { color: blue; }
            </style>
            """,
            unsafe_allow_html=True
        )

    if query:
        st.write(f"Aranan Konu: **{query}**")

        # Yükleme animasyonu ekleme
        with st.spinner("Yorumlar analiz ediliyor..."):
            # Yorumları çekme ve temizleme işlemi
            comments = pull_comments(get_video_id(query))
            comments['Cleaned_Comment'] = comments['Comment'].apply(clean_text)
            comments_df = pd.DataFrame(comments)


            # Yorumları analiz etme
            predictions = predict_sentiment(model,comments_df, tokenizer, label_encoder)

        # Sonuçları daha estetik bir tablo şeklinde gösterme
        st.subheader("🚀 Analiz Sonuçları")
        st.write(predictions)





        # Duygu Dağılımı Grafiği
        st.subheader("Duygu Dağılımı:")
        sentiment_counts = predictions["Predicted_Sentiment"].value_counts()
        fig, ax = plt.subplots()
        ax.bar(sentiment_counts.index, sentiment_counts.values)
        st.pyplot(fig)



    else:
        st.write("Lütfen bir eğitim konusu girin.")



if __name__ == "__main__":
    main()
