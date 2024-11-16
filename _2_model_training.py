import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.src.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM
from keras.src.legacy.preprocessing.text import Tokenizer
from keras.src.utils.sequence_utils import pad_sequences
def train_model():
    # Veriyi yükle
    data = pd.read_csv('test_cleaned.csv')

    # Yorumları ve etiketleri ayır
    texts = data['Cleaned_Comment'].astype(str).fillna('').values
    labels = data['label'].values

    # Etiketleri sayısal değerlere çevir
    label_encoder = LabelEncoder()
    labels = label_encoder.fit_transform(labels)
    joblib.dump(label_encoder, 'label_encoder.joblib')

    # Eğitim ve test verilerini ayır
    X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

    # Metinleri tokenize et
    tokenizer = Tokenizer(num_words=5000)
    tokenizer.fit_on_texts(X_train)
    X_train = tokenizer.texts_to_sequences(X_train)
    X_test = tokenizer.texts_to_sequences(X_test)
    joblib.dump(tokenizer, 'tokenizer.joblib')

    # Dizileri aynı uzunlukta yap
    maxlen = 100
    X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)
    X_test = pad_sequences(X_test, padding='post', maxlen=maxlen)

    # Modeli oluştur
    model = Sequential([
        Embedding(input_dim=5000, output_dim=128, input_length=maxlen),
        LSTM(128, dropout=0.2, recurrent_dropout=0.2),
        Dense(3, activation='softmax')
    ])

    # Modeli derle
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Modeli eğit
    model.fit(X_train, y_train, epochs=5, batch_size=64, validation_data=(X_test, y_test))

    # Modeli değerlendir
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f'Test Loss: {loss}')
    print(f'Test Accuracy: {accuracy}')

    # Modeli kaydet
    model.save('my_model.keras')
    print("Model başarıyla kaydedildi.")

