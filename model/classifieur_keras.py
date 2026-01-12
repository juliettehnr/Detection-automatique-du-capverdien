import pandas as pd
import pickle
from parse_tmx import create_dataset

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint


#Dataset
df = create_dataset()

label_encoder = LabelEncoder()
df["label"] = label_encoder.fit_transform(df["lang"])

#Split les données

TEST_RATIO = 0.1
TRAIN_RATIO = 0.8
VAL_RATIO = 0.1

X_temp, X_test, y_temp, y_test = train_test_split(
    df["text"],
    df["label"],
    test_size=TEST_RATIO,
    random_state=42,
    stratify=df["label"]
)

val_ratio_adjusted = VAL_RATIO / (TRAIN_RATIO + VAL_RATIO)

X_train, X_val, y_train, y_val = train_test_split(
    X_temp,
    y_temp,
    test_size=val_ratio_adjusted,  
    random_state=42,
    stratify=y_temp
)



#Tokenization
MAX_VOCAB = 10000
MAX_LEN = 50

tokenizer = Tokenizer(num_words=MAX_VOCAB, oov_token="<OOV>")
tokenizer.fit_on_texts(X_train)

def encode(texts):
    return pad_sequences(
        tokenizer.texts_to_sequences(texts),
        maxlen=MAX_LEN,
        padding="post"
    )

X_train_pad = encode(X_train)
X_val_pad = encode(X_val)
X_test_pad = encode(X_test)


#Modèle
model = Sequential([
    Embedding(MAX_VOCAB, 128, input_length=MAX_LEN),
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

#Training
checkpoint = ModelCheckpoint(
    "kea_pt_classifier.keras",
    monitor="val_loss",
    save_best_only=True
)

model.fit(
    X_train_pad,
    y_train,
    validation_data=(X_val_pad, y_val),
    epochs=5,
    batch_size=16,
    callbacks=[checkpoint]
)

#Sauvegarder modèle
with open("tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)

with open("label_encoder.pkl", "wb") as f:
    pickle.dump(label_encoder, f)


test_df = pd.DataFrame({
    "text": X_test,
    "label": y_test
})
test_df.to_csv("test_set.csv", index=False)

print("Training terminé, modèle sauvegardé") 
