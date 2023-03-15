import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.interpolate import make_interp_spline


#create an empty dataframe
df = pd.DataFrame(columns = ['politician', 'armonic_mean_normalized', 'date'])

politician = ['Berlusconi', 'Conte', 'Fratoianni', 'Salvini']#, 'Letta']#, 'Meloni']

#read the dataframes from the csv files
df_Berlusconi = pd.read_csv('Berlusconi_OnlyBots.csv', sep=',')
df_Conte = pd.read_csv('Conte_OnlyBots.csv', sep=',')
df_Fratoianni = pd.read_csv('Fratoianni_OnlyBots.csv', sep=',')
df_Salvini = pd.read_csv('Salvini_OnlyBots.csv', sep=',')
#df_Letta = pd.read_csv('Letta_OnlyBots.csv', sep=',')
#df_Meloni = pd.read_csv('Meloni_OnlyBots.csv', sep=',')

#convert the date column to datetime
df_Berlusconi['date'] = pd.to_datetime(df_Berlusconi['date'])
df_Conte['date'] = pd.to_datetime(df_Conte['date'])
df_Fratoianni['date'] = pd.to_datetime(df_Fratoianni['date'])
df_Salvini['date'] = pd.to_datetime(df_Salvini['date'])
#df_Letta['date'] = pd.to_datetime(df_Letta['date'])
#df_Meloni['date'] = pd.to_datetime(df_Meloni['date'])

df_politicians = [df_Berlusconi, df_Conte, df_Fratoianni, df_Salvini]#, df_Letta, df_Meloni]
#compute the frequencies of 'Ucraina' and 'Russia' for each party and for each date

frequencies = []

freq_Berlusconi_Ucraina_1 = df_Berlusconi.loc[df_Berlusconi['date'].between('2022-08-23', '2022-08-26')]['text'].str.contains('Ucraina').sum()
freq_Berlusconi_Ucraina_2 = df_Berlusconi.loc[df_Berlusconi['date'].between('2022-08-27', '2022-08-30')]['text'].str.contains('Ucraina').sum()
freq_Berlusconi_Ucraina_3 = df_Berlusconi.loc[df_Berlusconi['date'].between('2022-08-31', '2022-09-03')]['text'].str.contains('Ucraina').sum()
freq_Berlusconi_Ucraina_4 = df_Berlusconi.loc[df_Berlusconi['date'].between('2022-09-04', '2022-09-07')]['text'].str.contains('Ucraina').sum()
freq_Berlusconi_Ucraina_5 = df_Berlusconi.loc[df_Berlusconi['date'].between('2022-09-08', '2022-09-11')]['text'].str.contains('Ucraina').sum()
freq_Berlusconi_Ucraina_6 = df_Berlusconi.loc[df_Berlusconi['date'].between('2022-09-12', '2022-09-15')]['text'].str.contains('Ucraina').sum()
freq_Berlusconi_Ucraina_7 = df_Berlusconi.loc[df_Berlusconi['date'].between('2022-09-16', '2022-09-19')]['text'].str.contains('Ucraina').sum()
freq_Berlusconi_Ucraina_8 = df_Berlusconi.loc[df_Berlusconi['date'].between('2022-09-20', '2022-09-24')]['text'].str.contains('Ucraina').sum()

freq_Berlusconi_Russia_1 = df_Berlusconi.loc[df_Berlusconi['date'].between('2022-08-23', '2022-08-26')]['text'].str.contains('Russia').sum()
freq_Berlusconi_Russia_2 = df_Berlusconi.loc[df_Berlusconi['date'].between('2022-08-27', '2022-08-30')]['text'].str.contains('Russia').sum()
freq_Berlusconi_Russia_3 = df_Berlusconi.loc[df_Berlusconi['date'].between('2022-08-31', '2022-09-03')]['text'].str.contains('Russia').sum()
freq_Berlusconi_Russia_4 = df_Berlusconi.loc[df_Berlusconi['date'].between('2022-09-04', '2022-09-07')]['text'].str.contains('Russia').sum()
freq_Berlusconi_Russia_5 = df_Berlusconi.loc[df_Berlusconi['date'].between('2022-09-08', '2022-09-11')]['text'].str.contains('Russia').sum()
freq_Berlusconi_Russia_6 = df_Berlusconi.loc[df_Berlusconi['date'].between('2022-09-12', '2022-09-15')]['text'].str.contains('Russia').sum()
freq_Berlusconi_Russia_7 = df_Berlusconi.loc[df_Berlusconi['date'].between('2022-09-16', '2022-09-19')]['text'].str.contains('Russia').sum()
freq_Berlusconi_Russia_8 = df_Berlusconi.loc[df_Berlusconi['date'].between('2022-09-20', '2022-09-24')]['text'].str.contains('Russia').sum()

freq_Conte_Ucraina_1 = df_Conte.loc[df_Conte['date'].between('2022-08-23', '2022-08-26')]['text'].str.contains('Ucraina').sum()
freq_Conte_Ucraina_2 = df_Conte.loc[df_Conte['date'].between('2022-08-27', '2022-08-30')]['text'].str.contains('Ucraina').sum()
freq_Conte_Ucraina_3 = df_Conte.loc[df_Conte['date'].between('2022-08-31', '2022-09-03')]['text'].str.contains('Ucraina').sum()
freq_Conte_Ucraina_4 = df_Conte.loc[df_Conte['date'].between('2022-09-04', '2022-09-07')]['text'].str.contains('Ucraina').sum()
freq_Conte_Ucraina_5 = df_Conte.loc[df_Conte['date'].between('2022-09-08', '2022-09-11')]['text'].str.contains('Ucraina').sum()
freq_Conte_Ucraina_6 = df_Conte.loc[df_Conte['date'].between('2022-09-12', '2022-09-15')]['text'].str.contains('Ucraina').sum()
freq_Conte_Ucraina_7 = df_Conte.loc[df_Conte['date'].between('2022-09-16', '2022-09-19')]['text'].str.contains('Ucraina').sum()
freq_Conte_Ucraina_8 = df_Conte.loc[df_Conte['date'].between('2022-09-20', '2022-09-24')]['text'].str.contains('Ucraina').sum()

freq_Conte_Russia_1 = df_Conte.loc[df_Conte['date'].between('2022-08-23', '2022-08-26')]['text'].str.contains('Russia').sum()
freq_Conte_Russia_2 = df_Conte.loc[df_Conte['date'].between('2022-08-27', '2022-08-30')]['text'].str.contains('Russia').sum()
freq_Conte_Russia_3 = df_Conte.loc[df_Conte['date'].between('2022-08-31', '2022-09-03')]['text'].str.contains('Russia').sum()
freq_Conte_Russia_4 = df_Conte.loc[df_Conte['date'].between('2022-09-04', '2022-09-07')]['text'].str.contains('Russia').sum()
freq_Conte_Russia_5 = df_Conte.loc[df_Conte['date'].between('2022-09-08', '2022-09-11')]['text'].str.contains('Russia').sum()
freq_Conte_Russia_6 = df_Conte.loc[df_Conte['date'].between('2022-09-12', '2022-09-15')]['text'].str.contains('Russia').sum()
freq_Conte_Russia_7 = df_Conte.loc[df_Conte['date'].between('2022-09-16', '2022-09-19')]['text'].str.contains('Russia').sum()
freq_Conte_Russia_8 = df_Conte.loc[df_Conte['date'].between('2022-09-20', '2022-09-24')]['text'].str.contains('Russia').sum()

freq_Fratoianni_Ucraina_1 = df_Fratoianni.loc[df_Fratoianni['date'].between('2022-08-23', '2022-08-26')]['text'].str.contains('Ucraina').sum()
freq_Fratoianni_Ucraina_2 = df_Fratoianni.loc[df_Fratoianni['date'].between('2022-08-27', '2022-08-30')]['text'].str.contains('Ucraina').sum()
freq_Fratoianni_Ucraina_3 = df_Fratoianni.loc[df_Fratoianni['date'].between('2022-08-31', '2022-09-03')]['text'].str.contains('Ucraina').sum()
freq_Fratoianni_Ucraina_4 = df_Fratoianni.loc[df_Fratoianni['date'].between('2022-09-04', '2022-09-07')]['text'].str.contains('Ucraina').sum()
freq_Fratoianni_Ucraina_5 = df_Fratoianni.loc[df_Fratoianni['date'].between('2022-09-08', '2022-09-11')]['text'].str.contains('Ucraina').sum()
freq_Fratoianni_Ucraina_6 = df_Fratoianni.loc[df_Fratoianni['date'].between('2022-09-12', '2022-09-15')]['text'].str.contains('Ucraina').sum()
freq_Fratoianni_Ucraina_7 = df_Fratoianni.loc[df_Fratoianni['date'].between('2022-09-16', '2022-09-19')]['text'].str.contains('Ucraina').sum()
freq_Fratoianni_Ucraina_8 = df_Fratoianni.loc[df_Fratoianni['date'].between('2022-09-20', '2022-09-24')]['text'].str.contains('Ucraina').sum()

freq_Fratoianni_Russia_1 = df_Fratoianni.loc[df_Fratoianni['date'].between('2022-08-23', '2022-08-26')]['text'].str.contains('Russia').sum()
freq_Fratoianni_Russia_2 = df_Fratoianni.loc[df_Fratoianni['date'].between('2022-08-27', '2022-08-30')]['text'].str.contains('Russia').sum()
freq_Fratoianni_Russia_3 = df_Fratoianni.loc[df_Fratoianni['date'].between('2022-08-31', '2022-09-03')]['text'].str.contains('Russia').sum()
freq_Fratoianni_Russia_4 = df_Fratoianni.loc[df_Fratoianni['date'].between('2022-09-04', '2022-09-07')]['text'].str.contains('Russia').sum()
freq_Fratoianni_Russia_5 = df_Fratoianni.loc[df_Fratoianni['date'].between('2022-09-08', '2022-09-11')]['text'].str.contains('Russia').sum()
freq_Fratoianni_Russia_6 = df_Fratoianni.loc[df_Fratoianni['date'].between('2022-09-12', '2022-09-15')]['text'].str.contains('Russia').sum()
freq_Fratoianni_Russia_7 = df_Fratoianni.loc[df_Fratoianni['date'].between('2022-09-16', '2022-09-19')]['text'].str.contains('Russia').sum()
freq_Fratoianni_Russia_8 = df_Fratoianni.loc[df_Fratoianni['date'].between('2022-09-20', '2022-09-24')]['text'].str.contains('Russia').sum()

freq_Salvini_Ucraina_1 = df_Salvini.loc[df_Salvini['date'].between('2022-08-23', '2022-08-26')]['text'].str.contains('Ucraina').sum()
freq_Salvini_Ucraina_2 = df_Salvini.loc[df_Salvini['date'].between('2022-08-27', '2022-08-30')]['text'].str.contains('Ucraina').sum()
freq_Salvini_Ucraina_3 = df_Salvini.loc[df_Salvini['date'].between('2022-08-31', '2022-09-03')]['text'].str.contains('Ucraina').sum()
freq_Salvini_Ucraina_4 = df_Salvini.loc[df_Salvini['date'].between('2022-09-04', '2022-09-07')]['text'].str.contains('Ucraina').sum()
freq_Salvini_Ucraina_5 = df_Salvini.loc[df_Salvini['date'].between('2022-09-08', '2022-09-11')]['text'].str.contains('Ucraina').sum()
freq_Salvini_Ucraina_6 = df_Salvini.loc[df_Salvini['date'].between('2022-09-12', '2022-09-15')]['text'].str.contains('Ucraina').sum()
freq_Salvini_Ucraina_7 = df_Salvini.loc[df_Salvini['date'].between('2022-09-16', '2022-09-19')]['text'].str.contains('Ucraina').sum()
freq_Salvini_Ucraina_8 = df_Salvini.loc[df_Salvini['date'].between('2022-09-20', '2022-09-24')]['text'].str.contains('Ucraina').sum()

freq_Salvini_Russia_1 = df_Salvini.loc[df_Salvini['date'].between('2022-08-23', '2022-08-26')]['text'].str.contains('Russia').sum()
freq_Salvini_Russia_2 = df_Salvini.loc[df_Salvini['date'].between('2022-08-27', '2022-08-30')]['text'].str.contains('Russia').sum()
freq_Salvini_Russia_3 = df_Salvini.loc[df_Salvini['date'].between('2022-08-31', '2022-09-03')]['text'].str.contains('Russia').sum()
freq_Salvini_Russia_4 = df_Salvini.loc[df_Salvini['date'].between('2022-09-04', '2022-09-07')]['text'].str.contains('Russia').sum()
freq_Salvini_Russia_5 = df_Salvini.loc[df_Salvini['date'].between('2022-09-08', '2022-09-11')]['text'].str.contains('Russia').sum()
freq_Salvini_Russia_6 = df_Salvini.loc[df_Salvini['date'].between('2022-09-12', '2022-09-15')]['text'].str.contains('Russia').sum()
freq_Salvini_Russia_7 = df_Salvini.loc[df_Salvini['date'].between('2022-09-16', '2022-09-19')]['text'].str.contains('Russia').sum()
freq_Salvini_Russia_8 = df_Salvini.loc[df_Salvini['date'].between('2022-09-20', '2022-09-24')]['text'].str.contains('Russia').sum()

#freq_Letta_Ucraina_1 = df_Letta.loc[df_Letta['date'].between('2022-08-23', '2022-08-26')]['text'].str.contains('Ucraina').sum()
#freq_Letta_Ucraina_2 = df_Letta.loc[df_Letta['date'].between('2022-08-27', '2022-08-30')]['text'].str.contains('Ucraina').sum()
#freq_Letta_Ucraina_3 = df_Letta.loc[df_Letta['date'].between('2022-08-31', '2022-09-03')]['text'].str.contains('Ucraina').sum()
#freq_Letta_Ucraina_4 = df_Letta.loc[df_Letta['date'].between('2022-09-04', '2022-09-07')]['text'].str.contains('Ucraina').sum()
#freq_Letta_Ucraina_5 = df_Letta.loc[df_Letta['date'].between('2022-09-08', '2022-09-11')]['text'].str.contains('Ucraina').sum()
#freq_Letta_Ucraina_6 = df_Letta.loc[df_Letta['date'].between('2022-09-12', '2022-09-15')]['text'].str.contains('Ucraina').sum()
#freq_Letta_Ucraina_7 = df_Letta.loc[df_Letta['date'].between('2022-09-16', '2022-09-19')]['text'].str.contains('Ucraina').sum()
#freq_Letta_Ucraina_8 = df_Letta.loc[df_Letta['date'].between('2022-09-20', '2022-09-24')]['text'].str.contains('Ucraina').sum()

#freq_Letta_Russia_1 = df_Letta.loc[df_Letta['date'].between('2022-08-23', '2022-08-26')]['text'].str.contains('Russia').sum()
#freq_Letta_Russia_2 = df_Letta.loc[df_Letta['date'].between('2022-08-27', '2022-08-30')]['text'].str.contains('Russia').sum()
#freq_Letta_Russia_3 = df_Letta.loc[df_Letta['date'].between('2022-08-31', '2022-09-03')]['text'].str.contains('Russia').sum()
#freq_Letta_Russia_4 = df_Letta.loc[df_Letta['date'].between('2022-09-04', '2022-09-07')]['text'].str.contains('Russia').sum()
#freq_Letta_Russia_5 = df_Letta.loc[df_Letta['date'].between('2022-09-08', '2022-09-11')]['text'].str.contains('Russia').sum()
#freq_Letta_Russia_6 = df_Letta.loc[df_Letta['date'].between('2022-09-12', '2022-09-15')]['text'].str.contains('Russia').sum()
#freq_Letta_Russia_7 = df_Letta.loc[df_Letta['date'].between('2022-09-16', '2022-09-19')]['text'].str.contains('Russia').sum()
#freq_Letta_Russia_8 = df_Letta.loc[df_Letta['date'].between('2022-09-20', '2022-09-24')]['text'].str.contains('Russia').sum()

#freq_Meloni_Ucraina_1 = df_Meloni.loc[df_Meloni['date'].between('2022-08-23', '2022-08-26')]['text'].str.contains('Ucraina').sum()
#freq_Meloni_Ucraina_2 = df_Meloni.loc[df_Meloni['date'].between('2022-08-27', '2022-08-30')]['text'].str.contains('Ucraina').sum()
#freq_Meloni_Ucraina_3 = df_Meloni.loc[df_Meloni['date'].between('2022-08-31', '2022-09-03')]['text'].str.contains('Ucraina').sum()
#freq_Meloni_Ucraina_4 = df_Meloni.loc[df_Meloni['date'].between('2022-09-04', '2022-09-07')]['text'].str.contains('Ucraina').sum()
#freq_Meloni_Ucraina_5 = df_Meloni.loc[df_Meloni['date'].between('2022-09-08', '2022-09-11')]['text'].str.contains('Ucraina').sum()
#freq_Meloni_Ucraina_6 = df_Meloni.loc[df_Meloni['date'].between('2022-09-12', '2022-09-15')]['text'].str.contains('Ucraina').sum()
#freq_Meloni_Ucraina_7 = df_Meloni.loc[df_Meloni['date'].between('2022-09-16', '2022-09-19')]['text'].str.contains('Ucraina').sum()
#freq_Meloni_Ucraina_8 = df_Meloni.loc[df_Meloni['date'].between('2022-09-20', '2022-09-24')]['text'].str.contains('Ucraina').sum()

#freq_Meloni_Russia_1 = df_Meloni.loc[df_Meloni['date'].between('2022-08-23', '2022-08-26')]['text'].str.contains('Russia').sum()
#freq_Meloni_Russia_2 = df_Meloni.loc[df_Meloni['date'].between('2022-08-27', '2022-08-30')]['text'].str.contains('Russia').sum()
#freq_Meloni_Russia_3 = df_Meloni.loc[df_Meloni['date'].between('2022-08-31', '2022-09-03')]['text'].str.contains('Russia').sum()
#freq_Meloni_Russia_4 = df_Meloni.loc[df_Meloni['date'].between('2022-09-04', '2022-09-07')]['text'].str.contains('Russia').sum()
#freq_Meloni_Russia_5 = df_Meloni.loc[df_Meloni['date'].between('2022-09-08', '2022-09-11')]['text'].str.contains('Russia').sum()
#freq_Meloni_Russia_6 = df_Meloni.loc[df_Meloni['date'].between('2022-09-12', '2022-09-15')]['text'].str.contains('Russia').sum()
#freq_Meloni_Russia_7 = df_Meloni.loc[df_Meloni['date'].between('2022-09-16', '2022-09-19')]['text'].str.contains('Russia').sum()
#freq_Meloni_Russia_8 = df_Meloni.loc[df_Meloni['date'].between('2022-09-20', '2022-09-24')]['text'].str.contains('Russia').sum()

#compute the overall frequency of 'Ucraina' and 'Russia' for each party
#freq_Berlusconi_Ucraina = df_Berlusconi['text'].str.contains('Ucraina|Zelensky').sum()
#freq_Conte_Ucraina = df_Conte['text'].str.contains('Ucraina|Zelensky').sum()
#freq_Fratoianni_Ucraina = df_Fratoianni['text'].str.contains('Ucraina|Zelensky').sum()
#freq_Salvini_Ucraina = df_Salvini['text'].str.contains('Ucraina|Zelensky').sum()
#
#freq_Berlusconi_Russia = df_Berlusconi['text'].str.contains('Russia|Putin').sum()
#freq_Conte_Russia = df_Conte['text'].str.contains('Russia|Putin').sum()
#freq_Fratoianni_Russia = df_Fratoianni['text'].str.contains('Russia|Putin').sum()
#freq_Salvini_Russia = df_Salvini['text'].str.contains('Russia|Putin').sum()

len_Berlusconi = len(df_Berlusconi['text'])
len_Conte = len(df_Conte['text'])
len_Fratoianni = len(df_Fratoianni['text'])
len_Salvini = len(df_Salvini['text'])

#amonic_mean_normalized_Berlusconi = ((freq_Berlusconi_Ucraina*freq_Berlusconi_Russia)/(freq_Berlusconi_Ucraina+freq_Berlusconi_Russia))/len_Berlusconi
#amonic_mean_normalized_Conte = ((freq_Conte_Ucraina*freq_Conte_Russia)/(freq_Conte_Ucraina+freq_Conte_Russia))/len_Conte
#amonic_mean_normalized_Fratoianni = ((freq_Fratoianni_Ucraina*freq_Fratoianni_Russia)/(freq_Fratoianni_Ucraina+freq_Fratoianni_Russia))/len_Fratoianni
#amonic_mean_normalized_Salvini = ((freq_Salvini_Ucraina*freq_Salvini_Russia)/(freq_Salvini_Ucraina+freq_Salvini_Russia))/len_Salvini

armonic_mean_normalized_Berlusconi_1 = ((freq_Berlusconi_Ucraina_1*freq_Berlusconi_Russia_1)/(freq_Berlusconi_Ucraina_1+freq_Berlusconi_Russia_1))/len_Berlusconi
armonic_mean_normalized_Berlusconi_2 = ((freq_Berlusconi_Ucraina_2*freq_Berlusconi_Russia_2)/(freq_Berlusconi_Ucraina_2+freq_Berlusconi_Russia_2))/len_Berlusconi
armonic_mean_normalized_Berlusconi_3 = ((freq_Berlusconi_Ucraina_3*freq_Berlusconi_Russia_3)/(freq_Berlusconi_Ucraina_3+freq_Berlusconi_Russia_3))/len_Berlusconi
armonic_mean_normalized_Berlusconi_4 = ((freq_Berlusconi_Ucraina_4*freq_Berlusconi_Russia_4)/(freq_Berlusconi_Ucraina_4+freq_Berlusconi_Russia_4))/len_Berlusconi
armonic_mean_normalized_Berlusconi_5 = ((freq_Berlusconi_Ucraina_5*freq_Berlusconi_Russia_5)/(freq_Berlusconi_Ucraina_5+freq_Berlusconi_Russia_5))/len_Berlusconi
armonic_mean_normalized_Berlusconi_6 = ((freq_Berlusconi_Ucraina_6*freq_Berlusconi_Russia_6)/(freq_Berlusconi_Ucraina_6+freq_Berlusconi_Russia_6))/len_Berlusconi
armonic_mean_normalized_Berlusconi_7 = ((freq_Berlusconi_Ucraina_7*freq_Berlusconi_Russia_7)/(freq_Berlusconi_Ucraina_7+freq_Berlusconi_Russia_7))/len_Berlusconi
armonic_mean_normalized_Berlusconi_8 = ((freq_Berlusconi_Ucraina_8*freq_Berlusconi_Russia_8)/(freq_Berlusconi_Ucraina_8+freq_Berlusconi_Russia_8))/len_Berlusconi

armonic_mean_normalized_Conte_1 = ((freq_Conte_Ucraina_1*freq_Conte_Russia_1)/(freq_Conte_Ucraina_1+freq_Conte_Russia_1))/len_Conte
armonic_mean_normalized_Conte_2 = ((freq_Conte_Ucraina_2*freq_Conte_Russia_2)/(freq_Conte_Ucraina_2+freq_Conte_Russia_2))/len_Conte
armonic_mean_normalized_Conte_3 = ((freq_Conte_Ucraina_3*freq_Conte_Russia_3)/(freq_Conte_Ucraina_3+freq_Conte_Russia_3))/len_Conte
armonic_mean_normalized_Conte_4 = ((freq_Conte_Ucraina_4*freq_Conte_Russia_4)/(freq_Conte_Ucraina_4+freq_Conte_Russia_4))/len_Conte
armonic_mean_normalized_Conte_5 = ((freq_Conte_Ucraina_5*freq_Conte_Russia_5)/(freq_Conte_Ucraina_5+freq_Conte_Russia_5))/len_Conte
armonic_mean_normalized_Conte_6 = ((freq_Conte_Ucraina_6*freq_Conte_Russia_6)/(freq_Conte_Ucraina_6+freq_Conte_Russia_6))/len_Conte
armonic_mean_normalized_Conte_7 = ((freq_Conte_Ucraina_7*freq_Conte_Russia_7)/(freq_Conte_Ucraina_7+freq_Conte_Russia_7))/len_Conte
armonic_mean_normalized_Conte_8 = ((freq_Conte_Ucraina_8*freq_Conte_Russia_8)/(freq_Conte_Ucraina_8+freq_Conte_Russia_8))/len_Conte

armonic_mean_normalized_Fratoianni_1 = ((freq_Fratoianni_Ucraina_1*freq_Fratoianni_Russia_1)/(freq_Fratoianni_Ucraina_1+freq_Fratoianni_Russia_1))/len_Fratoianni
armonic_mean_normalized_Fratoianni_2 = ((freq_Fratoianni_Ucraina_2*freq_Fratoianni_Russia_2)/(freq_Fratoianni_Ucraina_2+freq_Fratoianni_Russia_2))/len_Fratoianni
armonic_mean_normalized_Fratoianni_3 = ((freq_Fratoianni_Ucraina_3*freq_Fratoianni_Russia_3)/(freq_Fratoianni_Ucraina_3+freq_Fratoianni_Russia_3))/len_Fratoianni
armonic_mean_normalized_Fratoianni_4 = ((freq_Fratoianni_Ucraina_4*freq_Fratoianni_Russia_4)/(freq_Fratoianni_Ucraina_4+freq_Fratoianni_Russia_4))/len_Fratoianni
armonic_mean_normalized_Fratoianni_5 = ((freq_Fratoianni_Ucraina_5*freq_Fratoianni_Russia_5)/(freq_Fratoianni_Ucraina_5+freq_Fratoianni_Russia_5))/len_Fratoianni
armonic_mean_normalized_Fratoianni_6 = ((freq_Fratoianni_Ucraina_6*freq_Fratoianni_Russia_6)/(freq_Fratoianni_Ucraina_6+freq_Fratoianni_Russia_6))/len_Fratoianni
armonic_mean_normalized_Fratoianni_7 = ((freq_Fratoianni_Ucraina_7*freq_Fratoianni_Russia_7)/(freq_Fratoianni_Ucraina_7+freq_Fratoianni_Russia_7))/len_Fratoianni
armonic_mean_normalized_Fratoianni_8 = ((freq_Fratoianni_Ucraina_8*freq_Fratoianni_Russia_8)/(freq_Fratoianni_Ucraina_8+freq_Fratoianni_Russia_8))/len_Fratoianni

armonic_mean_normalized_Salvini_1 = ((freq_Salvini_Ucraina_1*freq_Salvini_Russia_1)/(freq_Salvini_Ucraina_1+freq_Salvini_Russia_1))/len_Salvini
armonic_mean_normalized_Salvini_2 = ((freq_Salvini_Ucraina_2*freq_Salvini_Russia_2)/(freq_Salvini_Ucraina_2+freq_Salvini_Russia_2))/len_Salvini
armonic_mean_normalized_Salvini_3 = ((freq_Salvini_Ucraina_3*freq_Salvini_Russia_3)/(freq_Salvini_Ucraina_3+freq_Salvini_Russia_3))/len_Salvini
armonic_mean_normalized_Salvini_4 = ((freq_Salvini_Ucraina_4*freq_Salvini_Russia_4)/(freq_Salvini_Ucraina_4+freq_Salvini_Russia_4))/len_Salvini
armonic_mean_normalized_Salvini_5 = ((freq_Salvini_Ucraina_5*freq_Salvini_Russia_5)/(freq_Salvini_Ucraina_5+freq_Salvini_Russia_5))/len_Salvini
armonic_mean_normalized_Salvini_6 = ((freq_Salvini_Ucraina_6*freq_Salvini_Russia_6)/(freq_Salvini_Ucraina_6+freq_Salvini_Russia_6))/len_Salvini
armonic_mean_normalized_Salvini_7 = ((freq_Salvini_Ucraina_7*freq_Salvini_Russia_7)/(freq_Salvini_Ucraina_7+freq_Salvini_Russia_7))/len_Salvini
armonic_mean_normalized_Salvini_8 = ((freq_Salvini_Ucraina_8*freq_Salvini_Russia_8)/(freq_Salvini_Ucraina_8+freq_Salvini_Russia_8))/len_Salvini

#fill df with the results
df.loc[0] = ['Berlusconi', armonic_mean_normalized_Berlusconi_1*100, 1]
df.loc[1] = ['Berlusconi', armonic_mean_normalized_Berlusconi_2*100, 2]
df.loc[2] = ['Berlusconi', armonic_mean_normalized_Berlusconi_3*100, 3]
df.loc[3] = ['Berlusconi', armonic_mean_normalized_Berlusconi_4*100, 4]
df.loc[4] = ['Berlusconi', armonic_mean_normalized_Berlusconi_5*100, 5]
df.loc[5] = ['Berlusconi', armonic_mean_normalized_Berlusconi_6*100, 6]
df.loc[6] = ['Berlusconi', armonic_mean_normalized_Berlusconi_7*100, 7]
df.loc[7] = ['Berlusconi', armonic_mean_normalized_Berlusconi_8*100, 8]

df.loc[8] = ['Conte', armonic_mean_normalized_Conte_1*100, 1]
df.loc[9] = ['Conte', armonic_mean_normalized_Conte_2*100, 2]
df.loc[10] = ['Conte', armonic_mean_normalized_Conte_3*100, 3]
df.loc[11] = ['Conte', armonic_mean_normalized_Conte_4*100, 4]
df.loc[12] = ['Conte', armonic_mean_normalized_Conte_5*100, 5]
df.loc[13] = ['Conte', armonic_mean_normalized_Conte_6*100, 6]
df.loc[14] = ['Conte', armonic_mean_normalized_Conte_7*100, 7]
df.loc[15] = ['Conte', armonic_mean_normalized_Conte_8*100, 8]

df.loc[16] = ['Fratoianni', armonic_mean_normalized_Fratoianni_1*100, 1]
df.loc[17] = ['Fratoianni', armonic_mean_normalized_Fratoianni_2*100, 2]
df.loc[18] = ['Fratoianni', armonic_mean_normalized_Fratoianni_3*100, 3]
df.loc[19] = ['Fratoianni', armonic_mean_normalized_Fratoianni_4*100, 4]
df.loc[20] = ['Fratoianni', armonic_mean_normalized_Fratoianni_5*100, 5]
df.loc[21] = ['Fratoianni', armonic_mean_normalized_Fratoianni_6*100, 6]
df.loc[22] = ['Fratoianni', armonic_mean_normalized_Fratoianni_7*100, 7]
df.loc[23] = ['Fratoianni', armonic_mean_normalized_Fratoianni_8*100, 8]

df.loc[24] = ['Salvini', armonic_mean_normalized_Salvini_1*100, 1]
df.loc[25] = ['Salvini', armonic_mean_normalized_Salvini_2*100, 2]
df.loc[26] = ['Salvini', armonic_mean_normalized_Salvini_3*100, 3]
df.loc[27] = ['Salvini', armonic_mean_normalized_Salvini_4*100, 4]
df.loc[28] = ['Salvini', armonic_mean_normalized_Salvini_5*100, 5]
df.loc[29] = ['Salvini', armonic_mean_normalized_Salvini_6*100, 6]
df.loc[30] = ['Salvini', armonic_mean_normalized_Salvini_7*100, 7]
df.loc[31] = ['Salvini', armonic_mean_normalized_Salvini_8*100, 8]

df.fillna(0, inplace=True)

print(df)

#curved line
#temp = df[df['politician']=='Berlusconi']

#X_Y_Spline = scipy.interpolate.UnivariateSpline(temp.date, temp.armonic_mean_normalized, k=2, s=0)
#
#X_ = np.linspace(1, 3)
#Y_ = X_Y_Spline(X_)

#plt.plot(X_, Y_, label='Berlusconi')
#plt.show()

#politician = ['Berlusconi', 'Conte', 'Fratoianni', 'Salvini', 'Letta', 'Meloni']
color = ['c', 'y', 'm', 'g']#, 'r']#, 'b']


fig, ax = plt.subplots(1, figsize= (15,15))

for polit in politician:
    temp = df[df['politician']==polit]
    ax.plot(temp.date, temp.armonic_mean_normalized, label=polit, marker='o', markersize=8, linestyle='-', linewidth=2, color=color[politician.index(polit)])
    #start label
    ax.text(temp.date.iloc[0]-0.02, temp.armonic_mean_normalized.iloc[0], polit, fontsize=10, ha = 'right')
    ax.text(temp.date.iloc[-1]+0.02, temp.armonic_mean_normalized.iloc[-1], polit, fontsize=10, ha = 'left')
    #end label
    ax.legend()
    #position of the legend external to the plot
    #ax.legend(bbox_to_anchor=(1.05, 1), loc=2)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8], ['Period_1', 'Period_2', 'Period_3', 'Period_4', 'Period_5', 'Period_6', 'Period_7', 'Period_8'])
    plt.xlim(0.5, 8.5)
    #ax.set_xlabel('10-days period')
    ax.set_ylabel('Normalized armonic mean')
    ax.set_title('Normalized armonic mean evolution of the use of the words "Ukraine" and "Russia" in the tweets of the bots')

plt.show()

#save the plot
fig.savefig('Slope_Graph_Bots.png', dpi=500)
