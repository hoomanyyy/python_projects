import json
import nltk
from nltk.stem import WordNetLemmatizer
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
import numpy as np
import keras
from keras.layers  import Dense , Dropout
from keras.models import Sequential
import numpy as np

def load_data():
    data_file = open("intents.json", encoding="utf8").read()
    data = json.loads(data_file)

    text = []
    label = []

    for intents in data["intents"]:
        tag = intents["tag"]
        for pattern in intents["patterns"]:
            text.append(pattern)
            label.append(tag)
            
    vect = CountVectorizer(binary=False, max_features=5000)
    x = vect.fit_transform(text).toarray()
    
    le = LabelEncoder()
    y_int = le.fit_transform(label)
    y = to_categorical(y_int)
    

    with open("vectorizer.pkl", "wb") as f:
        pickle.dump(vect, f)

    with open("label_encoder.pkl", "wb") as f:
        pickle.dump(le, f)
    
    return x, y

x, y = load_data()

def Build_model():
    model = Sequential()
    model.add(Dense(128, activation="relu", input_shape=(x.shape[1],)))
    model.add(Dropout(0.5))
    model.add(Dense(128, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(y.shape[1], activation="softmax"))  # اصلاح شده
    
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    model.fit(x, y, epochs=10, batch_size=8, verbose=1)
    model.save("model.h5")
    return model

Build_model()