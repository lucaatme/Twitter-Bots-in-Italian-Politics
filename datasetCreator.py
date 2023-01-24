import tweepy
from config import *
import time
import pandas as pd
import pytz
from datetime import datetime
from tweepy import Cursor

auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

starting_date = "2022-02-24"
end_date = "2022-12-31"

starting_datetime = datetime.strptime(starting_date, "%Y-%m-%d").replace(tzinfo=pytz.UTC)
ending_datetime = datetime.strptime(end_date, "%Y-%m-%d").replace(tzinfo=pytz.UTC)

#center_left_wing_pE = ["@Piu_Europa", "@emmabonino", "@bendellavedova", "@riccardomagi", "@marcocappato"]
#center_right_wing_FI = ["@forza_italia", "@berlusconi", "@Antonio_Tajani", "@BerniniAM", "@gasparripdl"]
#right_wing_FdI = ["@FratellidItalia", "@GiorgiaMeloni", "@GuidoCrosetto", "@Ignazio_LaRussa", "@Francesco_Lollo1"]
#right_wing_L = ["@LegaSalvini", "@matteosalvinimi", "@Fontana3Lorenzo", "@borghi_claudio", "@SimoPillon"]
left_wing_PD = ["@pdnetwork", "@EnricoLetta", "@serracchiani", "@AndreaOrlandosp", "@lauraboldrini"]
left_wing_SiVe = ["@Si_sinistra", "@NFratoianni", "@AngeloBonelli1", "@aboubakar_soum", "@EleonoraEvi"]
center_AzIv = ["@Azione_it", "@CarloCalenda", "@matteorenzi", "@MatteoRichetti", "@meb"]
center_M5S = ["@Mov5Stelle", "@GiuseppeConteIT", "@Roberto_Fico", "@PaolaTavernaM5S", "@c_appendino"]
extremisms = ["@PartitComunista", "@gparagone", "@MarcoRizzoPC", "@DiegoFusaro", "@marioadinolfi"]

parties = [left_wing_PD, left_wing_SiVe, center_AzIv, center_M5S, extremisms]

user_dict = {}
df = pd.DataFrame(columns=['author_id', 'username', 'author_followers', 'author_tweets',
                           'author_description', 'author_location', 'text', 'created_at',
                           'retweets', 'likes'])
for party in parties:
    party_tweets = []
    for username in party:
        print("Collecting tweets from " + str(username))
        for tweet in Cursor(api.user_timeline, screen_name=username).items():
            if tweet.created_at < starting_datetime or tweet.created_at > ending_datetime:
                continue
            try:
                user = tweet.user
                user_dict[user.id] = {'username': user.screen_name, 
                                      'followers': user.followers_count,
                                      'tweets': user.statuses_count,
                                      'description': user.description,
                                      'location': user.location}
                author_info = user_dict[tweet.user.id]
                # Put all of the information we want to keep in a single dictionary for each tweet
                tweet_data = {'author_id': tweet.user.id, 
                          'username': author_info['username'],
                          'author_followers': author_info['followers'],
                          'author_tweets': author_info['tweets'],
                          'author_description': author_info['description'],
                          'author_location': author_info['location'],
                          'text': tweet.text,
                          'created_at': tweet.created_at,
                          'retweets': tweet.retweet_count,
                          'likes': tweet.favorite_count,
                          }
                party_tweets.append(tweet_data)
                df = pd.concat([df, pd.DataFrame(party_tweets)])
                print("Tweet collected at {}".format(tweet.created_at))

            except Exception as e:
                    print(f"An exception occurred: {e}")
                    continue
    print("Tweets from " + str(party[0]) + " collected")
    df.to_csv(str(party[0]) + ".csv", index=False)