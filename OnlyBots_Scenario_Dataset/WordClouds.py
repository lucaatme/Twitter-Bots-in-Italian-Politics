#concatenate all datasets
import pandas as pd
import numpy as np
import csv
import wordcloud
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import datetime
import nltk



# Load the CSV file
path = "/home/kdf/Scrivania/OnlyBots_Scenario_Dataset/"
#df_az = pd.read_csv(path + "center_AzIv.csv")
df_pE = pd.read_csv(path + "Bonino_OnlyBots.csv")
df_m5s = pd.read_csv(path + "Conte_OnlyBots.csv")
df_fi = pd.read_csv(path + "Berlusconi_OnlyBots.csv")
#df_pd = pd.read_csv(path + "left_wing_PD.csv")
df_si = pd.read_csv(path + "Fratoianni_OnlyBots.csv")
#df_fdi = pd.read_csv(path + "right_wing_FdI.csv")
df_L = pd.read_csv(path + "Salvini_OnlyBots.csv")

##get tweets if they are in date range
#start = datetime.datetime(2022, 2, 24, 0, 0, 0)
#end = datetime.datetime(2022, 3, 24, 0, 0, 0)
## pandas.Series.between() function Using two dates
#df = df_az.loc[df_az["date"].between("2022-02-24", "2022-03-24")]
#text = df['tweets'].to_string()

list_parties = ['pE', 'M5S', 'FI', 'SiVe','L']
# stop words
stopwords = set(STOPWORDS)
# create a list of italian stopwords to be removed
#read stopwords from file
with open('stopwords.txt', 'r') as f:
    list = f.readlines()
#remove \n from each word
list = [x.strip() for x in list]
stopwords = set(STOPWORDS).union(list)

# Generate a word cloud image for each party
i = 0
for party in [df_pE, df_m5s, df_fi,df_si, df_L]:
    
    #df = party.loc[party["created_at"].between("2022-08-23", "2022-09-23")]
    text = party['text'].to_string()
    wordcloud = WordCloud(stopwords=stopwords, background_color='white').generate(text)
    
    # save the image with the name of the party
    wordcloud.to_file('Bots_WC' + list_parties[i] + ".png")
    i = i+1
