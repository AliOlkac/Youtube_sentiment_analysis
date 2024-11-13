import joblib
import pandas as pd
from keras.src.saving import load_model
from keras.src.legacy.preprocessing.text import Tokenizer
from keras.src.utils.sequence_utils import pad_sequences
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
import keras.src.models
"""
MODEL_PATH = 'my_model.keras'

# Modeli yükleme
model = keras.models.load_model(MODEL_PATH)"""


def predict_sentiment(model, comments, tokenizer, label_encoder):
    # `comments`'in DataFrame olup olmadığını kontrol edin
    if not isinstance(comments, pd.DataFrame):
        raise ValueError("`comments` bir DataFrame olmalıdır.")

    # `Cleaned_Comment` sütununun varlığını kontrol edin
    if 'Cleaned_Comment' not in comments.columns:
        raise ValueError("`comments` DataFrame'i `Cleaned_Comment` sütununu içermiyor.")

    # Yorumları metin olarak alın ve varsa eksik değerleri boş metinle doldurun
    texts = comments['Cleaned_Comment'].astype(str).fillna('')

    # Tokenizer'ı yükle

    sequences = tokenizer.texts_to_sequences(texts)
    maxlen = 100
    X = pad_sequences(sequences, padding='post', maxlen=maxlen)

    # Tahmin yap
    predictions = model.predict(X)
    predicted_labels = predictions.argmax(axis=1)

    # LabelEncoder'ı yükle

    predicted_labels = label_encoder.inverse_transform(predicted_labels)

    return pd.DataFrame({'Cleaned_Comment': texts, 'Predicted_Sentiment': predicted_labels})

"""
print("Predict Sentiment fonksiyonu başarı")
# Test
# Yorumları yükle
comments_df = pd.read_csv('cleaned_youtube_comments.csv')

# Model ve tokenizer dosyalarını yükle
model = load_model('my_model.keras')
tokenizer = joblib.load('tokenizer.joblib')
label_encoder = joblib.load('label_encoder.joblib')

# Yorumları tahmin et ve csv dosyasına kaydet
predictions = predict_sentiment(model, comments_df, tokenizer, label_encoder)
predictions.to_csv('predicted_sentiments.csv', index=False)
"""



