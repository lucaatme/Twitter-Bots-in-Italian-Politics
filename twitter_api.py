import tweepy
from config import *
import csv

# Authenticate
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

right_wing_FdI = ["@FratellidItalia", "@GiorgiaMeloni", "@GuidoCrosetto", "@Ignazio_LaRussa", "@Francesco_Lollo1"]  #santanchè
right_wing_L = ["@LegaSalvini", "@matteosalvinimi", "@Fontana3Lorenzo", "@borghi_claudio", "@SimoPillon"] #bagnai
left_wing_PD = ["@pdnetwork", "@EnricoLetta", "@serracchiani", "@AndreaOrlandosp", "@lauraboldrini"] #gentiloni
left_wing_SiVe = ["@Si_sinistra", "@NFratoianni", "@AngeloBonelli1", "@aboubakar_soum", "@EleonoraEvi"]
center_right_wing_FI = ["@forzaitalia", "@berlusconi", "@Antonio_Tajani", "@BerniniAM", "@gasparripdl"]
center_left_wing_pE = ["@Piu_Europa", "@emmabonino", "@bendellavedova", "@riccardomagi", "@marcocappato"]
center_AzIv = ["@Azione_it", "@CarloCalenda", "@matteorenzi", "@MatteoRichetti", "@meb"]
center_M5S = ["@Mov5Stelle", "@GiuseppeConteIT", "@Roberto_Fico", "@PaolaTavernaM5S", "@c_appendino"]
extremisms = ["@PartitComunista", "@gparagone", "@MarcoRizzoPC", "@DiegoFusaro", "@marioadinolfi"]

parties = [right_wing_FdI, right_wing_L, left_wing_PD, left_wing_SiVe, center_right_wing_FI, center_left_wing_pE, center_AzIv, extremisms]

for party in parties:
    for user in party:
        all_tweets = []
        new_tweets = api.user_timeline(screen_name=user, count=200)
        all_tweets.extend(new_tweets)
        oldest_tweet = all_tweets[-1].id - 1
    
            
        # Keep paginating through the results
        while len(new_tweets) > 0:
            new_tweets = api.user_timeline(screen_name=user, count=200, max_id=oldest_tweet)
            all_tweets.extend(new_tweets)
            oldest_tweet = all_tweets[-1].id - 1


    #save the tweets in a csv file
    with open( + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id","created_at","text"])
        for tweet in all_tweets:
            writer.writerow([tweet.id, tweet.created_at, tweet.text.encode('utf-8')])