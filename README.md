# TWIPOL: Twitter Italian Politics

### Natural Language Processing and Bot Detection Analysis on Italian political tweeps during the Russian-Ukrainian conflict.


## Topics of the project

The main objective for this project is to analyze how the **Russian-Ukrainian war** has impacted the content posted on Twitter by the main figures in the Italian political scene. In order to do so, we picked the **8** most important Italian political parties, chose some of the more active users in terms of posted tweets, pulled those tweets and processed them. The second part of this analysis regards the presence of bots: how many of them can be found replying to the very same tweets we analyzed before, and under which category these accounts can be classified as being.

# Dataset
After selecting the  8 main parties  we created a **.csv** file for each party. The structure is as follows:

*D<sub>i</sub>* = *[P, L, p<sub>1</sub>, ..., p<sub>6</sub>]*

where:

- *D<sub>i</sub>* is the Dataset, *i=1,...,8*, one for each party.
- *P* is the "Party account".
- *L* is the "Leader account".
- *p<sub>1, ..., 6</sub>* are six "politician accounts" in that party.

In the end, the definitive dataset can be found in the table below.
| Party / Coalition          | Amount of Tweets |
|---------------------------|-----------------|
| Lega                      | 15797           |
| Azione - Italia Viva      | 7272            |
| Fratelli d'Italia         | 6610            |
| Sinistra Italiana - Verdi | 5003            |
| +Europa                   | 4383            | 
| Partito Democratico       | 4357            |
| Forza Italia              | 4172            |
| Movimento 5 Stelle        | 3672            |
| **Total**                 | **51266**       |


# Analysis
After the dataset creation, all the **.csv** files have been cleaned up, and an Italian stop words list has been used in order to obtain better results during the Word2Vec phase of the analysis.

### For all that follows we only report the results for the “Azione-Italia Viva” coalition

Here we can see a brief recap of who tweeted the most among all users, and how much they posted.

![Alt text](/Histograms_userXtweets/AzIv_histogramTweets-1.png)



## Word Clouds
![Alt text](/First_month_Wordclouds/First_monthAzIv.png)

This word cloud refers to the tweets posted during the first month of the war. We can see that words like `Ucraina`, `Putin`, `Guerra` and `Russia` are quite big in size, meaning that they were mentioned many times in the tweets. 



## Trends
![Alt text](/Trends/Trends_Tweets/Trend_center_AzIv.png)


## 2-Hops Graphs

After analyzing the content posted by the chosen set of profiles, we took 3 keywords `russia`, `ucraina` and `armi` and we built a *two-hops graph* to gather the words that appeared in the tweets and that had the highest degree of similarity with them. The results can be seen in the image below.

![Alt text](/Gephi_Graph_Results/AzIv_final_ArchiGrossi.png)

# Bot Analysis
We took the usernames of whoever replied under a tweet posted by [Carlo Calenda](https://twitter.com/CarloCalenda) in the last 4 days of propaganda, before the General Elections that took place in September, 2022 and we run [botometer](https://github.com/IUNetSci/botometer-python) on them. The results are the following:

![Alt text](/Trends/botAzIv.png)

As we can see, it appears that 7.5% of the users that replied has been classified as a bot. One interesting feature from botometer is that the object returned by the API call consists in a series of attributes, values and a threshold, and this allows not only to classify a profile as fake or not, but also to classify it as being a certain type of bot rather than another. In the graph below it can be seen to which category each profile belongs to.

![Alt text](/Trends/classifiedBotsAzIv.png)

# References
- The Internet Archive - WayBack Machine. https://archive.org/web/.
- Schild, L., Ling, C., Blackburn, J., Stringhini, G., Zhang, Y., & Zannettou, S. (2020). "Go eat a bat, chang!": An early look on the emergence of sinophobic behavior on web communities in the face of covid-19. arXiv preprint arXiv:2004.04046.
- Rodríguez-Ruiz, J., Mata-Sánchez, J. I., Monroy, R., Loyola-Gonzalez, O., & López-Cuevas, A. (2020). A one-class classification approach for bot detection on Twitter. Computers & Security, 91, 101715.
- Weber, I., Garimella, V. R. K., & Batayneh, A. (2013). Secular vs. islamist polarization in egypt on twitter. In Proceedings of the 2013 IEEE/ACM international conference on advances in social networks analysis and mining (pp. 290-297).
- Naseem, U., Razzak, I., Khushi, M., Eklund, P. W., & Kim, J. (2021). COVIDSenti: A large-scale benchmark Twitter data set for COVID-19 sentiment analysis. IEEE Transactions on Computational Social Systems, 8(4), 1003-1015.
- Antonakaki, D., Fragopoulou, P., & Ioannidis, S. (2021). A survey of Twitter research: Data model, graph structure, sentiment analysis and attacks. Expert Systems with Applications, 164, 114006.
- Camacho, D., Panizo-LLedot, Á., Bello-Orgaz, G., Gonzalez-Pardo, A., & Cambria, E. (2020). The four dimensions of social network analysis: An overview of research methods, applications, and software tools. Information Fusion, 63, 88-120.
- Twitter API. https://github.com/twitterdev/
- IU Network Science Institute. (n.d.). Botometer python project. https://github.com/IUNetSci/botometer-python
- Bohacek, S. (n.d.). Botwiki project. https://www.botwiki.org
- Wikipedia. (n.d.). Russian-Ukrainian timeline. https://en.wikipedia.org/wiki/Timeline_of_the_2022_Russian_invasion_of_Ukraine
- Business Insider. Percentage of Bots on Twitter. https://www.businessinsider.com/twitter-bots-comprise-less-than-\linebreaks5-but-tweet-more-2022-9
- Gephi. Graph Visualization Software. https://gephi.org/
