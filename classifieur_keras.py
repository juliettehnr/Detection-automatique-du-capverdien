import pandas as pd
import numpy as np
from parse_tmx import make_dataset
import pickle


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout 

df = make_dataset()

label_encoder = LabelEncoder()
df["label"] = label_encoder.fit_transform(df["lang"])

X_train, X_test, y_train, y_test = train_test_split(
    df["text"],
    df["label"],
    test_size=0.2,
    random_state=42,
    stratify=df["label"]
)


MAX_VOCAB = 10000
MAX_LEN = 50

tokenizer = Tokenizer(num_words=MAX_VOCAB, oov_token="<OOV>")
tokenizer.fit_on_texts(X_train)

X_train_seq = tokenizer.texts_to_sequences(X_train)
X_test_seq = tokenizer.texts_to_sequences(X_test)

X_train_pad = pad_sequences(X_train_seq, maxlen=MAX_LEN, padding="post")
X_test_pad = pad_sequences(X_test_seq, maxlen=MAX_LEN, padding="post")


model = Sequential([
    Embedding(input_dim=MAX_VOCAB, output_dim=128, input_length=MAX_LEN),
    LSTM(64),
    Dropout(0.5),
    Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.summary()

history = model.fit(
    X_train_pad,
    y_train,
    validation_split=0.2,
    epochs=5,
    batch_size=16
)

loss, acc = model.evaluate(X_test_pad, y_test)
print(f"Accuracy test : {acc:.3f}")

model.save("kea_pt_classifier.keras")

with open("tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)


def predict_language(sentence):
    seq = tokenizer.texts_to_sequences([sentence])
    pad = pad_sequences(seq, maxlen=MAX_LEN, padding="post")
    prob = model.predict(pad)[0][0]
    
    lang = "pt" if prob > 0.5 else "kea"
    return lang, prob

print(predict_language("N ta gosta di bo"))
print(predict_language("Eu gosto de você"))