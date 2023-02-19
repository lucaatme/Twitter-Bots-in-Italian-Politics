import gensim
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from gensim.models import LdaModel, LdaMulticore
from gensim.utils import simple_preprocess
from gensim import corpora
import pandas as pd
import nltk
import re
from nltk.corpus import wordnet
from cleantext import clean
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns
import time

#create  alist of csv files
df = pd.read_csv('right_wing_FdI.csv')

#preprocessing
tweets_FdI = df['tweets'].to_string()
corpus = tweets_FdI.lower()
corpus = clean(corpus, no_emoji=True, no_numbers=True, no_digits=True, no_currency_symbols=True, replace_with_punct="", lang="it")

#tokenization
tokenized_corpus = nltk.word_tokenize(corpus)

#create dictionary
dictionary = list(tokenized_corpus)


#filter using stopwords italy
stop_words = list(nltk.corpus.stopwords.words('italian'))

#read stopwords from file
with open('stopwords.txt', 'r') as f:
    list = f.readlines()
#remove \n from each word
list = [x.strip() for x in list]
stop_words = set(stop_words).union(list)

dictionary = [word for word in dictionary if word not in stop_words]

#word2vec
model = Word2Vec([dictionary], #list of sentences
                 window=140, #window size, important no to be too big
                 sg = 1, #skip-gram
                 min_count=1, #min number of times a word must appear to be included in the model (try 9 or 6)
                 workers=2 #number of threads to use during training
                 ) #to change default params
model.save('w2v_All_FdI.model')
#model = Word2Vec.load('w2v_All_AzIv.model')
print(model)
print('')

#word2vec most similar
v1 = 'guerra'
val1 = model.wv.most_similar(v1, topn=30)
print(val1)

list = []
val = [val1]
for vali in val:
    for i in range(len(vali)):
        list.append(vali[i][0])

val1 = ['russia', 'ucraina', 'difesa'] #per FdI no armi, mai usato

#get all vocab from model
#vocab = model.wv.index_to_key
#vocab = set(vocab)
#remove stopwords from vocab
vocab = [word for word in list if word not in stop_words]

df = pd.DataFrame(index = val1, columns = vocab)
column_headers = df.columns.values.tolist()
#fill the df with similarity values
for i in range(len(val1)):
    for j in range(len(column_headers)):
        #if (model.wv.similarity(val1[i], column_headers[j])):
        df.iloc[i,j] = model.wv.similarity(val1[i], column_headers[j])
        #else:
        #    df.iloc[i,j] = 0
        

df = df.loc[:, (df != 0).any(axis=0)]

print(df)
#save df to csv
df.to_csv('w2v_FdI.csv')




