#packages
import time

import nltk
import numpy as np
import tflearn
import json
import random
import tkinter


#chatbot class
class ChatBotModel:
    def __init__(self):
        self.model = None
        self.stemmer =  nltk.PorterStemmer()
        self.data = None
        self.model_vocab =[]
        self.classes =[]
        print('model initalized')

    #preprocess the model
    #extracts the json objects from the intents.json file
    def preprocess(self):
        nltk.download('punkt')  # to help tokenize the words accurately will be downloaded relevant packages online
        nltk.download('wordnet')

        #opening the json file
        with open('intents.json') as intents:
            self.data = json.load(intents)

        # getting informations from intents.json--

        self.model_vocab = []   #this will be the model vocabulary for the chatbot
        self.classes = []    #this will be the labels that we will receive from the intents.json file

        x_docs = []     #training data is the words we receive from the "patterns" in the intents.json file
        y_docs = []     #target data is the label we receive from the "tag" in the intents.json file

        #getting the intents list and torkenize the in the "pattern" list
        for intent in self.data['intents']:
            for pattern in intent['patterns']:
                wrds = nltk.word_tokenize(pattern)
                self.model_vocab.extend(wrds)
                x_docs.append(wrds)
                y_docs.append(intent['tag'])

                #mapping the relevant label with the words that have been torkenized
                if intent['tag'] not in self.classes:
                    self.classes.append(intent['tag'])

        #removing the stopwords
        self.model_vocab = [self.stemmer.stem(w.lower()) for w in self.model_vocab if w not in "?"]

        #sorting the list
        self.model_vocab = sorted(list(set(self.model_vocab)))
        self.classes = sorted(self.classes)

        training = []
        output = []
        out_empty = [0 for _ in range(len(self.classes))]

        #neuaral network can be only read in numbers
        #converting the words in to numers at a fixed length so the length will be len(self.model_vocab)
        for x, doc in enumerate(x_docs):
            bag = []
            wrds = [self.stemmer.stem(w.lower()) for w in doc]
            for w in self.model_vocab:
                if w in wrds:
                    bag.append(1)
                else:
                    bag.append(0)

            #select the all data in the out_empty
            output_row = out_empty[:]
            output_row[self.classes.index(y_docs[x])] = 1

            training.append(bag)
            output.append(output_row)

        training = np.array(training)
        output = np.array(output)

        return [training,output]

    #invoke this function if the database has been updated otherwise dont invoke
    def intializeModel(self):

        training, output = self.preprocess()
        net = tflearn.input_data(shape=[None, len(training[0])])
        net = tflearn.fully_connected(net, 80)
        net = tflearn.fully_connected(net, 80)
        net = tflearn.fully_connected(net, 80)
        net = tflearn.fully_connected(net, len(output[0]), activation='softmax')
        net = tflearn.regression(net)

        self.model = tflearn.DNN(net)
        self.model.fit(training, output, n_epoch=25, batch_size=32, show_metric=True)
        self.model.save('./model_1/chatbot.tflearn')


    #loading the model and setting the architecture for the model
    def loadModel(self):
        print('loading model...')
        training,output = self.preprocess()

        #input layer
        net = tflearn.input_data(shape=[None, len(training[0])])

        #hidden layer
        net = tflearn.fully_connected(net, 80)
        net = tflearn.fully_connected(net, 80)
        net = tflearn.fully_connected(net, 80)

        #output layer
        net = tflearn.fully_connected(net, len(output[0]), activation='softmax')
        net = tflearn.regression(net)


        self.model = tflearn.DNN(net)
        self.model.load(model_file='model_1/chatbot.tflearn')
        print('Loaded and Ready to use')


    #preprocess the user data
    def torkenize_user_query(self,user_inpt, vocabulary):

        #setting the bag of words for the user input
        user_bag = [0 for _ in range(len(vocabulary))]
        user_wrds = nltk.word_tokenize(user_inpt)
        user_wrds = [self.stemmer.stem(word.lower()) for word in user_wrds]

        for s_word in user_wrds:
            for cls, wrd in enumerate(vocabulary):
                if wrd == s_word:
                    user_bag[cls] = 1

        return np.array(user_bag)


    #executes the chatbot
    def chat(self,input):
        inp = input

        # Porbability of correct response
        results = self.model.predict([self.torkenize_user_query(inp, self.model_vocab)])

        # Picking the greatest number from probability
        result_index = np.argmax(results)

        tag = self.classes[result_index]

        for tg in self.data['intents']:

            if tg['tag'] == tag:
                responses = tg['responses']
                return "U-CHAT : "+str(random.choice(responses))




