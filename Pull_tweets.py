import tweepy
from config import *
import time
import pandas as pd
import pytz
from datetime import datetime
from tweepy import Cursor
import datetime


# Twitter API credentials
TWITTER_CONSUMER_KEY = "TWITTER_CONSUMER_KEY"
TWITTER_CONSUMER_SECRET = "TWITTER_CONSUMER_SECRET"
TWITTER_ACCESS_TOKEN = "TWITTER_ACCESS_TOKEN"
TWITTER_ACCESS_TOKEN_SECRET = "TWITTER_ACCESS_TOKEN_SECRET"
# Twitter API setup
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
#setting the timezone window and converting for filtering
starting_date = '2022-02-24'
ending_date = '2023-01-01'
starting_datetime = datetime.datetime.strptime(starting_date, "%Y-%m-%d").replace(tzinfo=pytz.UTC)
ending_datetime = datetime.datetime.strptime(ending_date, "%Y-%m-%d").replace(tzinfo=pytz.UTC)

# Get tweets from a specific party
center_left_wing_pE = ["@Piu_Europa", "@emmabonino", "@bendellavedova", "@riccardomagi", "@marcocappato"]#DONE WITH RT
center_right_wing_FI = ["@forza_italia", "@berlusconi", "@Antonio_Tajani", "@BerniniAM", "@gasparripdl"]#DONE WITH RT
right_wing_FdI = ["@FratellidItalia", "@GiorgiaMeloni", "@GuidoCrosetto", "@Ignazio_LaRussa", "@FrancescoLollo1"]#DONE NO RT
right_wing_L = ["@LegaSalvini", "@matteosalvinimi", "@Fontana3Lorenzo", "@borghi_claudio", "@SimoPillon"]
left_wing_PD = ["@pdnetwork", "@EnricoLetta", "@serracchiani", "@AndreaOrlandosp", "@lauraboldrini"]
left_wing_SiVe = ["@Si_sinistra", "@NFratoianni", "@AngeloBonelli1", "@aboubakar_soum", "@EleonoraEvi"]
center_AzIv = ["@Azione_it", "@CarloCalenda", "@matteorenzi", "@MatteoRichetti", "@meb"] 
center_M5S = ["@Mov5Stelle", "@GiuseppeConteIT", "@Roberto_Fico", "@PaolaTavernaM5S", "@c_appendino"] 
extremisms = ["@PartitComunista", "@gparagone", "@MarcoRizzoPC", "@DiegoFusaro", "@marioadinolfi"]

parties = [center_M5S]
df = pd.DataFrame(columns=['username', 
                           'tweets', 
                           'date',
                           'likes',
                           'retweets'])

# First you get the tweets in a json object
for party in parties:
    print('Entering party '+ str(party))
    for username in party:
        print('Collecting for user: ' + str(username))
        results = [status._json for status in tweepy.Cursor(api.user_timeline, 
                                                            screen_name = username, 
                                                            count=500000, 
                                                            tweet_mode='extended', 
                                                            include_rts=False).items()]
        # Now you can iterate over 'results' and store the complete message from each tweet.
        politician = []
        tweets = []
        date = []
        likes = []
        retweets = []
        for result in results:
            #creating values for df_pol
            politician.append(result['user']['screen_name'])
            tweets.append(result['full_text'])
            date.append(result['created_at'])
            likes.append(result['favorite_count'])
            retweets.append(result['retweet_count'])
        print('Formalizing dataframes of tweets scraped from user: ' + str(username))
        df_pol = pd.DataFrame({'username': politician, 
                   'tweets': tweets, 
                   'date': date, 
                   'likes': likes, 
                   'retweets': retweets})
    # Create a dataframe
        print('Concatecating dataframes df_pol_'+str(username)+' and df')
    # Save the dataframe to a csv file
        df = pd.concat([df, df_pol])
    # Remove duplicates
        print('Removing duplicates and filtering by date')
        df = df.drop_duplicates()
        df['date'] = pd.to_datetime(df['date'], utc = True)
        df = df[(df['date'].between(starting_date, ending_date))]
        print('Success!')
    print('Creating dataset in .csv format')
    df.to_csv(str(parties[0][0]) + '.csv', index=False)
    print("Created dataset " + str(parties[0][0])+".csv")

print(df)

