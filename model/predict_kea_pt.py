from tensorflow.keras.models import load_model
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

model = load_model("../saved_model/kea_pt_classifier.keras")

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)
    
MAX_LEN = 50

def predict_language(sentence):
    seq = tokenizer.texts_to_sequences([sentence])
    pad = pad_sequences(seq, maxlen=MAX_LEN, padding="post")
    prob = model.predict(pad)[0][0]
    
    lang = "pt" if prob > 0.5 else "kea"
    return lang, prob

print(predict_language("N ta gosta di bo"))
print(predict_language("Eu gosto de você")) 
