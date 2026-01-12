import pandas as pd
import pickle
import numpy as np

from sklearn.metrics import confusion_matrix, classification_report

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import numpy as np
from sklearn.metrics import accuracy_score



model = load_model("../saved_model/kea_pt_classifier.keras")
print(model.summary()) 

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

test_df = pd.read_csv("test_set.csv")

MAX_LEN = 50


X_test_pad = pad_sequences(
    tokenizer.texts_to_sequences(test_df["text"]),
    maxlen=MAX_LEN,
    padding="post"
)

y_true = test_df["label"].values
y_probs = model.predict(X_test_pad).ravel()
y_pred = (y_probs > 0.5).astype(int)


#Résultats
print("\n Classification report\n")
print(classification_report(
    y_true,
    y_pred,
    target_names=label_encoder.classes_
))

print("\n Matrice de confusion\n")
cm = confusion_matrix(y_true, y_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=label_encoder.classes_
)

disp.plot(
    cmap="Blues",
    values_format="d"
)

plt.title("Matrice de confusion – KEA vs PT")
plt.show()



errors = test_df.copy()
errors["y_true"] = y_true
errors["y_pred"] = y_pred
errors["prob"] = y_probs

errors = errors[errors["y_true"] != errors["y_pred"]]

errors["true_lang"] = label_encoder.inverse_transform(errors["y_true"])
errors["pred_lang"] = label_encoder.inverse_transform(errors["y_pred"])



print("\n Exemples d'erreurs\n")
print(errors[["text", "true_lang", "pred_lang", "prob"]].head(10)) 
