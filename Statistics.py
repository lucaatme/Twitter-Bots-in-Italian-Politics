#concatenate all datasets
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import datetime
import seaborn as sns



# Load the CSV file
path = "/home/kdf/Scrivania/Advanced Cyber/Phase3_SNA/Code/ACNS-Project/Final_Dataset/"
df_az = pd.read_csv(path + "center_AzIv.csv")
df_pE = pd.read_csv(path + "center_left_wing_pE.csv")
df_m5s = pd.read_csv(path + "center_M5S.csv")
df_fi = pd.read_csv(path + "center_right_wing_FI.csv")
df_pd = pd.read_csv(path + "left_wing_PD.csv")
df_si = pd.read_csv(path + "left_wing_SiVe.csv")
df_fdi = pd.read_csv(path + "right_wing_FdI.csv")
df_L = pd.read_csv(path + "right_wing_L.csv")

list_parties = ['AzIv', 'pE', 'M5S', 'FI', 'PD', 'SiVe', 'FdI', 'L']
i = 0
sns.set(rc={'figure.figsize':(14,8)})
sns.set_style("whitegrid")
sns.set_palette("Set2")

for party in [df_az, df_pE, df_m5s, df_fi, df_pd, df_si, df_fdi, df_L]:
    party = party.groupby('username').count()

    #plot username x number of tweets and order by number of tweets
    party = party.sort_values(by=['tweets'], ascending=True)
    sns.barplot(x="tweets", y=party.index, data=party, palette="Set2")
    #save the sns plot
    plt.savefig(path + str(list_parties[i])+ "_histogramTweets.pdf", dpi = 300)
    i = i+1
    plt.clf()