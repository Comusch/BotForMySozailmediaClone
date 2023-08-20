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
        self.model = load_model('chatbotmodel.h5')
        self.dooropen = False
        self.lighton = True
        self.changelight = False
        self.step = 1
        self.search = ""


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
        if question.replace(" ","")[0].isnumeric():
            res = str(cl.calculate(question))
        else:
            #interpretation of the getting text
            try:
                ints = self.predict_class(question)
                res = self.get_response(ints, self.intents)
                textints = str(ints)
            except:
                print("hey")
            #Desicion finder, what should the programm do
            if textints.find('thanks') != -1 or textints.find('shutdown') != -1:
                gl.setszero()
                self.step = 1

            if self.step == 1:
                if textints.find('door') != -1:
                    if self.dooropen == False:
                        self.dooropen = True
                        res = "I open the door for you."
                    else:
                        self.dooropen = False
                        res = "I close the door, so nobody can go now inside the room."

                if textints.find('light') != -1:
                    if self.lighton == False:
                        self.lighton = True
                        res = "I have switch the light on"
                    else:
                        self.lighton = False
                        res = "I switch the light off, I hope that is ok for you"
                    self.changelight = True

                if textints.find('weather') != -1:
                    res = "In which city?"
                    self.step = 2
                    # res = "I don't have any information"

                if textints.find('Websearch') != -1:
                    res = "about what?"
                    self.step = 3
                    # res = "I don't have any information"

                if textints.find('musik') != -1:
                    mk.stopvideo()
                    res = "Video was started"
                    # res = "I don't have any information"

                if textints.find('time') != -1:
                    res = "It is " + dt.gettime()

                if textints.find('date') != -1:
                    res = "The date is " + dt.getdata()
                if textints.find('State') != -1:
                    res = "The light is " + self.lighton +". The door is " + self.dooropen+"."
                if textints.find('Stocks') != -1:
                    res = "Which Stock"
                    self.step = 4
                if textints.find('tasklist') != -1:
                    res = "which should I save for you?"
                    self.step = 6
                    return res
                if textints.find('calculator') != -1:
                    res = "Now I'm ready to answer your mathe questions"
                if textints.find('cleaninglist') != -1:
                    sh.deleteallElements()
                    res = "I delete every Element from the tasklist"
                if textints.find('whatshouldido') != -1:
                    res = "You should do these tasks: "+ sh.readallElemts()
                if textints.find('deleteoneElement') != -1:
                    res = "Which task do you finish?"
                    self.step = 7
            elif self.step == 2:
                city = question
                weather = wt.whichweathertoday(str(city))
                res = "Today the sky is " + str(weather.detailed_status) + "." + " The tempeture is " + self.cutastringfromastring(str(weather.temperature('celsius')), ',', ':') + " degree high today."
                self.step = 1

            elif self.step == 3:
                self.search = question
                gl.setszero()
                res = gl.searchweb(self.search)
                self.step = 5

            elif self.step == 4:
                #res = str(st.getStockprice(question))
                res = "At the moment the function is not avalible"
                self.step = 1

            elif self.step == 5:
                if textints.find('nextunittothistheam') != -1:
                    res = gl.searchweb(self.search)
                else:
                    self.search = question
                    gl.setszero()
                    res = gl.searchweb(self.search)

            elif self.step == 6:
                sh.addontasklist(str(question))
                res = "Save it for you in your Tasklist"
                self.step = 1

            elif self.step == 7:
                sh.deleteoneElements(str(question))
                res = "I delete the task for your tasklist"
                self.step = 1

        return res




