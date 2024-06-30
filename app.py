from flask import Flask, render_template, request, jsonify
import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import random
import json
import pickle

stemmer = LancasterStemmer()

with open("intents.json") as file:
    data = json.load(file)

with open("career_data.pickle", "rb") as f:
    words, labels, training, output = pickle.load(f)

model = load_model("career_model.h5")

app = Flask(__name__)

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return np.array(bag)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get')
def get_bot_response():
    message = request.args.get('msg')
    if message:
        message = message.lower()
        results = model.predict(np.array([bag_of_words(message, words)]))[0]
        result_index = np.argmax(results)
        tag = labels[result_index]
        if results[result_index] > 0.5:
             
            for tg in data['intents']:
                if tg['tag'] == tag:
                    responses = tg['responses']
            response = random.choice(responses)

        
        else:
            response = "I didn't quite get that, please try again."
        return str(response)
    return "Missing Data!"

if __name__ == "__main__":
    app.run()
