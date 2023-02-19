import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas import Series
import matplotlib as mpl

#NECESSARY FOR XTICKS OPTION, ETC.
from pylab import*
import seaborn as sns
# import all the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
sns.set_theme(style="darkgrid")
  
# create a dataframe  
df = pd.read_csv('right_wing_FdI.csv')

#remove time from date
df['date'] = df['date'].str.split(' ', expand=True)[0]

list = df['date'].unique().tolist()
#sort list from oldest to newest
list.sort()

#lower case all tweets
df['tweets'] = df['tweets'].str.lower()

#add a column in df
df['count'] = 0
df['count_russia'] = 0
df['count_ucraina'] = 0

#create a new column with 0 or 1 if ucraina or russia is in text of tweet
df['count_tot'] = df['tweets'].str.contains('ucraina|russia|ucraino|russo|ucraini|russi|putin|zelensky', case = True, na = 0).astype(int)

df['count_russia'] = df['tweets'].str.contains('guerra|russia|russo|russi|putin', case = True, na = 0).astype(int)

df['count_ucraina'] = df['tweets'].str.contains('guerra|ucraina|ucraino|ucraini|zelensky', case = True, na = 0).astype(int)


#group by date and sum the count column
df_russia = df.groupby('date')['count_russia'].sum().reset_index()
df_ucraina = df.groupby('date')['count_ucraina'].sum().reset_index()

print(df_russia, df_ucraina)

#plot the results in a area plot using seaborn
#define colors to use in chart
color_map = ['steelblue', 'green']
#    
#
#plot the results in a area plot using seaborn

#ax = sns.lineplot(x="date", y="count_russia", data=df_russia, color = color_map[0])
#ax = sns.lineplot(x="date", y="count_ucraina", data=df_ucraina, color = color_map[1])
#ax.set_title('Trend tweets')
#ax.set_ylabel('Number of tweets')
#ax.set_xlabel('Date')
#ax.set_xticks(np.arange(0, len(list), 1))
#ax.set_xticklabels(list, rotation=45)
#plt.show()
#set the size of the plot
#plt.figure(figsize=(10,7))
#plt.stackplot(list, df_russia['count_russia'], df_ucraina['count_ucraina'], labels=['Russia', 'Ucraina'])
#plt.legend(loc='upper left')
#plt.title('Trend tweets')
#plt.ylabel('Number of tweets')
#plt.xlabel('Date')
#plt.xticks(rotation=45)
#plt.show()

#plot the results in a area plot using matplotlib
plt.rcParams["figure.figsize"] = (20,20)
plt.rcParams["figure.autolayout"] = True
plt.rcParams["axes.labelsize"] = 12
fig, ax = plt.subplots()
ax.stackplot(list, df_russia['count_russia'], df_ucraina['count_ucraina'], labels=['Russia', 'Ucraina'])

ax.set_ylabel('Number of tweets')
ax.set_xlabel('Date')
ax.set_ylim(0, 25)
ax.set_yscale('linear')

ax.set_xticks(np.arange(0, len(list), 1))
ax.set_xticklabels(list, rotation=45)

every_nth = 14
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)
#
#plt.axvline(x='2022-04-07', color='black', linestyle='--', label='End of phase 1 of war: Invasion')
#plt.axvline(x='2022-09-11', color='black', linestyle='--', label='End of phase 2 of war: Southeastern front')
#plt.axvline(x='2022-11-09', color='black', linestyle='--', label='End of phase 3 of war: Ukrainian counterof.')
#
#plt.axvline(x='2022-12-12', color='black', linestyle='--', label='Zelensky appealed to the G7 for tanks')
#
#plt.axvspan('2022-07-21', '2022-09-25', color='red', alpha=0.2)
#plt.axvline(x='2022-07-21', color='red', linestyle='--', label='Start of political campaign in Italy')
#plt.axvline(x='2022-09-25', color='red', linestyle='--', label='Election_Day')

plt.axvline(x='2022-04-07', color='black', linestyle='--')
plt.axvline(x='2022-07-21', color='red', linestyle='--')
plt.axvline(x='2022-09-11', color='black', linestyle='--')
plt.axvline(x='2022-09-25', color='red', linestyle='--')
plt.axvline(x='2022-11-09', color='black', linestyle='--')
plt.axvline(x='2022-12-12', color='black', linestyle='--')

plt.text(x = '2022-04-07', y = 25, s = '1', fontsize = 19, color = 'black')
plt.text(x = '2022-07-21', y = 25, s = '2', fontsize = 19, color = 'black')
plt.text(x = '2022-09-11', y = 25, s = '3', fontsize = 19, color = 'black')
plt.text(x = '2022-09-25', y = 25, s = '4', fontsize = 19, color = 'black')
plt.text(x = '2022-11-09', y = 25, s = '5', fontsize = 19, color = 'black')
plt.text(x = '2022-12-12', y = 25, s = '6', fontsize = 19, color = 'black')
plt.axvspan('2022-07-21', '2022-09-25', color='red', alpha=0.2, label = 'Political campaign in Italy')
#set parameters for tick labels
plt.tick_params(axis='x', which='major', labelsize=12)

ax.legend(bbox_to_anchor = (1.0, 1),loc='best', fontsize=19)
plt.tight_layout()
plt.show()

#save the plot as pdf
fig.savefig('Trend_tweets_FdI.png', dpi=300)
