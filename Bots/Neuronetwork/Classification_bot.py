import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer

from keras.models import load_model
#from Services import Stocks as st
#from audio import sttprogram as stt

class Classification_bot:

    def __init__(self):
        #creating all needed informations
        self.lemmatizer = WordNetLemmatizer()
        self.intents = json.loads(open('intents.json').read())

        self.words = pickle.load(open('words.pkl', 'rb'))
        self.classes = pickle.load(open('classes.pkl', 'rb'))
        self.model = load_model('Classification_bot.h5')

    def clean_up_sentence(self, sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [self.lemmatizer.lemmatize(word) for word in sentence_words]
        return sentence_words


    def bag_of_words(self, sentence):
        sentencewords = self.clean_up_sentence(sentence)
        bag = [0] * len(self.words)
        for w in sentencewords:
            for i, word in enumerate(self.words):
                if word == w:
                    bag[i] = 1
        return np.array(bag)


    def predict_class(self, sentence):
        bow = self.bag_of_words(sentence)
        res = self.model.predict(np.array([bow]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

        results.sort(key=lambda x: x[1], reverse=True)
        return_List = []
        for r in results:
            return_List.append({'intent': self.classes[r[0]], 'probability': str(r[1])})
        return return_List


    def get_response(self, intents_list, intents_json):
        tag = intents_list[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if i['tag'] == tag:
                result = random.choice(i['responses'])
                break

        return result


    def cutastringfromastring(self, text,s1, s2):
        l1 = text.split(s1)[0]
        l2 = l1.split(s2)[1]
        return l2


    def getanswertoquestion(self, question):
        ints = ""
        textints = ""

         #interpretation of the getting text
        try:
            ints = self.predict_class(question)
            res = self.get_response(ints, self.intents)
            textints = str(ints)
        except:
            print("hey")

        return textints, res

clas_bot = Classification_bot()
textints, response = clas_bot.getanswertoquestion("What is the weather today?")
print(textints)
print(response)
textints, response = clas_bot.getanswertoquestion("What is happening in the world?")
print(textints)
print(response)





