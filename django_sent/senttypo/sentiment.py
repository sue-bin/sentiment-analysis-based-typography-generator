#!/usr/bin/env python
# coding: utf-8

# In[7]:


import re
import pickle
import numpy as np
import pandas as pd
from ko_papago import ko_papago

from keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.text import text_to_word_sequence
from tensorflow.keras.preprocessing.sequence import pad_sequences

def sentiment(text):
    
    # text preprocessing
    text = ko_papago(text)
    text = text.lower()
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = [text]
    
    # predict
    with open('data.pickle', 'rb') as f:
        data = pickle.load(f)
    token = Tokenizer()
    token.fit_on_texts(data)

    model = load_model("model.h5")
    token.fit_on_texts(text)
    text_pre = pad_sequences(token.texts_to_sequences(text), padding='pre', maxlen=200)
    pre = model.predict(text_pre)
    sent_to_emotion = {0:'anger', 1:'disgust', 2:'fear', 3:'joy', 4:'sadness', 5:'surprise', 6:'no emotion'}
    emotion = pd.Series(np.argmax(np.round(pre))).map(sent_to_emotion).item()
    
    return str(emotion)

