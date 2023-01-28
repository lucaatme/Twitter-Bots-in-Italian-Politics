import tweepy
from config import *
import time
import pandas as pd
import pytz
from datetime import datetime
from tweepy import Cursor
import datetime

 
# Twitter API credentials
TWITTER_CONSUMER_KEY = "API_KEY"#api_key
TWITTER_CONSUMER_SECRET = "API_KEY_SECRET "#api_secret_key
TWITTER_ACCESS_TOKEN = "ACCESS_TOKEN"#access_token
TWITTER_ACCESS_TOKEN_SECRET = "ACCESS_TOKEN_SECRET"#access_token_secret
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
center_left_wing_pE = ["@Piu_Europa", "@emmabonino", "@bendellavedova", "@riccardomagi", "@marcocappato"]#Done no RT, Tot. = 2511
                                                                                                         #Done with RT, Tot. = 3914

center_right_wing_FI = ["@forza_italia", "@berlusconi", "@Antonio_Tajani", "@BerniniAM", "@gasparripdl"]#Done no RT, Tot. = 2957
                                                                                                         #Done with RT, Tot. = 5797

right_wing_FdI = ["@FratellidItalia", "@GiorgiaMeloni", "@Ignazio_LaRussa", "@DSantanche", "@FrancescoLollo1"]#Done no RT, Tot. = 2918
                                                                                                         #Done with RT, Tot. = 4146

right_wing_L = ["@LegaSalvini", "@matteosalvinimi", "@Fontana3Lorenzo", "@arrigoni_paolo", "@SimoPillon"]#Done no RT, Tot. = 5194
                                                                                                         #Done with RT, Tot. = 5439

left_wing_PD = ["@pdnetwork", "@EnricoLetta", "@serracchiani", "@peppeprovenzano", "@lauraboldrini"]#Done no RT, Tot. = 3106
                                                                                                    #Done with RT, Tot. = 6750

left_wing_SiVe = ["@Si_sinistra", "@NFratoianni", "@AngeloBonelli1", "@aboubakar_soum", "@EleonoraEvi"]#Done no RT, Tot. = 2994
                                                                                                       #Done with RT, Tot. = 10440

center_AzIv = ["@Azione_it", "@CarloCalenda", "@matteorenzi", "@MatteoRichetti", "@meb"] #Done no RT, Tot. = 3769
                                                                                         #Done with RT, Tot. = 6678

center_M5S = ["@Mov5Stelle", "@GiuseppeConteIT", "@Roberto_Fico", "@PaolaTavernaM5S", "@c_appendino"] #Done no RT, Tot. = 2979
                                                                                                      #Done with RT, Tot. = 3563

extremisms = ["@PartitComunista", "@gparagone", "@MarcoRizzoPC", "@demagistris", "@marioadinolfi"] #Done no RT, Tot. = 4720
                                                                                                   #Done with RT, Tot. = 5538
#Tot. NO RT = 31.148
#Tot. with RT = 52.265

parties = [extremisms]
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
                                                            count=20000, 
                                                            tweet_mode='extended',
                                                            #since='2022-12-31', until='2022-02-24', 
                                                            include_rts=True).items(limit = 20000)]
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
        print('Success! Now sleeping for 1 minutes')
        time.sleep(60)
    print('Creating dataset in .csv format')
    df.to_csv(str(parties[0][0]) + '.csv', index=False)
    print("Created dataset " + str(parties[0][0])+".csv")

print(df)

