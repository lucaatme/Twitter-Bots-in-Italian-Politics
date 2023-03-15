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
import time

#create  alist of csv files
file = 'Salvini_CompleteScenario.csv'
df = pd.read_csv(file)

#preprocessing
tweets_FdI = df['text'].to_string()
corpus = tweets_FdI.lower()
corpus = clean(corpus, no_emoji=True, no_line_breaks=True, no_punct=True,no_numbers=True, no_digits=True, no_currency_symbols=True, replace_with_punct="", replace_with_number= "", lang="it")

#tokenization
tokenized_corpus = simple_preprocess(corpus)

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
                 window=5, #window size, important no to be too big
                 sg = 1, #skip-gram
                 min_count=1, #min number of times a word must appear to be included in the model
                 workers=4 #number of threads to use during training
                 ) #to change default params

print(model)
print('')

list_words_columns = ['gas', 'armi', 'conflitto', 'nato', 'europa', 'usa', 'italia', 'invasione', 'aggressione', 'ue']
list_words_rows = ['russia', 'ucraina', 'guerra']

matrix = np.zeros((len(list_words_rows), len(list_words_columns)))

for i in range(len(list_words_rows)):
    for j in range(len(list_words_columns)):
        try:
            matrix[i][j] = model.wv.similarity(list_words_rows[i], list_words_columns[j])
        except:
            matrix[i][j] = 0
        
matrix = np.where(matrix < 0, 0, matrix)

print(matrix)

#create df
df = pd.DataFrame(matrix, columns=list_words_columns, index=list_words_rows)

#save df to csv
df.to_csv('Gephi_'+file)