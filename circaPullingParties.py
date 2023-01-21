import tweepy
from config import *
import time
import pandas as pd
import csv

client = tweepy.Client(bearer_token = TWITTER_BEARER_TOKEN, wait_on_rate_limit=True)

center_left_wing_pE = ["@Piu_Europa", "@emmabonino", "@bendellavedova", "@riccardomagi", "@marcocappato"]
center_right_wing_FI = ["@forzaitalia", "@berlusconi", "@Antonio_Tajani", "@BerniniAM", "@gasparripdl"]
right_wing_FdI = ["@FratellidItalia", "@GiorgiaMeloni", "@GuidoCrosetto", "@Ignazio_LaRussa", "@Francesco_Lollo1"]
right_wing_L = ["@LegaSalvini", "@matteosalvinimi", "@Fontana3Lorenzo", "@borghi_claudio", "@SimoPillon"]
left_wing_PD = ["@pdnetwork", "@EnricoLetta", "@serracchiani", "@AndreaOrlandosp", "@lauraboldrini"]
left_wing_SiVe = ["@Si_sinistra", "@NFratoianni", "@AngeloBonelli1", "@aboubakar_soum", "@EleonoraEvi"]
center_AzIv = ["@Azione_it", "@CarloCalenda", "@matteorenzi", "@MatteoRichetti", "@meb"]
center_M5S = ["@Mov5Stelle", "@GiuseppeConteIT", "@Roberto_Fico", "@PaolaTavernaM5S", "@c_appendino"]
extremisms = ["@PartitComunista", "@gparagone", "@MarcoRizzoPC", "@DiegoFusaro", "@marioadinolfi"]

parties = [center_left_wing_pE, center_right_wing_FI, right_wing_FdI, right_wing_L, left_wing_PD, left_wing_SiVe, center_AzIv, center_M5S, extremisms]

for party in parties:
    full_party = []
    for user in party:
        #tweets = []
        for response in tweepy.Paginator(client.search_all_tweets,           
                                         query = f'{user} lang:it',
                                         user_fields = ['username', 'public_metrics', 'description', 'location'],
                                         tweet_fields = ['created_at', 'geo', 'public_metrics', 'text'],
                                         start_time = '2022-02-24T00:00:00Z',
                                         end_time = '2022-12-31T00:00:00Z',
                                         max_results = 500):
            time.sleep(1)
            #tweets.append(response)
            full_party.append(response)
            print("Processed tweets from: " + user + "\n")
            

        with open(str(party) + '.csv', 'w', newline='') as csvfile:
            # Create a DictWriter object with the necessary fieldnames
            fieldnames = ["tweet_id", "username", "text", "created_at", "num_likes", "num_retweets", "num_replies"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # Write the headers to the file
            writer.writeheader()

            for response in full_party:
                # Extract the necessary information from the tweet
                try:
                    tweet_id = response.data['id']
                    username = response.data['author_id']
                    text = response.data['text']
                    created_at = response.data['created_at']
                    num_likes = response.data['public_metrics']['like_count']
                    num_retweets = response.data['public_metrics']['retweet_count']
                    num_replies = response.data['public_metrics']['reply_count']
                    # Write the tweet information to the file as a row
                    writer.writerow({'tweet_id': tweet_id,
                                    'username': username,
                                    'text': text,
                                    'created_at': created_at,
                                    'num_likes': num_likes,
                                    'num_retweets': num_retweets,
                                    'num_replies': num_replies})
                except:
                    continue

    print("Done with: " + party + "\n")