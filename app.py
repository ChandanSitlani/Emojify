import string
import random
#import keras
import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow import keras

 
 
f=open("index.html")
ic=f.read()
print(ic)

import cherrypy
word_to_index={}
def load():
    words=pd.read_csv('w2i (1).csv')
    print("read")
    print(words.iloc[1][0])
    for i in range(int(words.shape[0]/20)):
        word_to_index[words.iloc[i][0]]=words.iloc[i][1]
    print(word_to_index["the"]);
    
def sentence_to_indices(sentences):
    ind=np.zeros((len(sentences),10))
    i=0
    for sentence in sentences:
        j=0
        ss=sentence.split(' ')
        for s in ss:
            if s in word_to_index.keys():
                ind[i][j]=word_to_index[s]
            else:
                ind[i][j]=0
            j+=1
        i+=1
    return ind
            
load()
class EmojifyModel():
    
    model=2
    Model=keras.models.load_model('emojify.h5')
    #emojifyModel=keras.load_model('emojify.h5')
    def predict(self,sentence=[0,0,0,0,0,0,0,0,0,0]):

        return np.argmax(self.Model.predict(sentence))
    
    def __init__(self):

        print(self.Model.summary)
        p=np.argmax(self.Model.predict([1,5,9,0,0,0,0,0,0,0]))
        print(p.shape)
        print(p)
        print(self.model)
n2e={
    0:"🧡",
    1:"⚽",
    2:"👍",
    3:"😩",
    4:"🍽️"
    }

class Emojify(object):
    @cherrypy.expose
    def index(self):

        f=open("index.html")
        ic=f.read()
        return ic

    @cherrypy.expose
    def generate(self, data):


        model=EmojifyModel()
        a="<html> <head></head><body><center>"+data+' '+n2e[model.predict(sentence_to_indices([data]))]+"</center>"
        print(model.predict(sentence_to_indices(["i want to play"])))
        print(data)
        print(sentence_to_indices([data]))
        
        return a


if __name__ == '__main__':
    cherrypy.quickstart(Emojify())