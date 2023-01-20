import tweepy
from config import *
import time
import pandas as pd

client = tweepy.Client(bearer_token = TWITTER_BEARER_TOKEN, wait_on_rate_limit=True)

hoax_tweets = []
for response in tweepy.Paginator(client.search_all_tweets, 
                                 query = 'PUTIN hoax -is:retweet lang:en',
                                 user_fields = ['username', 'public_metrics', 'description', 'location'],
                                 tweet_fields = ['created_at', 'geo', 'public_metrics', 'text'],
                                 expansions = 'author_id',
                                 start_time = '2021-01-20T00:00:00Z',
                                 end_time = '2021-01-21T00:00:00Z',
                              max_results=500):
    time.sleep(1)
    hoax_tweets.append(response)

#convert hoax_tweets to a dataframe
hoax_tweets_df = pd.DataFrame(hoax_tweets)