from keras.models import load_model
import numpy as np
import pickle

model = load_model("model.h5")
with open("vectorizer.pkl", "rb") as f:
    vect = pickle.load(f)
with open("label_encoder.pkl", "rb") as f:
    le = pickle.load(f)

def result(text):
    seq = vect.transform([text]).toarray()
    pre = model.predict(seq)
    idx = np.argmax(pre)
    result_pre = le.inverse_transform([idx])
    return result_pre[0]

print(result(""))