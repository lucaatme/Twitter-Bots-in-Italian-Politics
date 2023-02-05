import requests
import os
import json
from config import *
import time
import datetime

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = TWITTER_BEARER_TOKEN

# start_time = int(time.mktime(datetime.datetime(2022, 2, 23).timetuple())) * 1000
# end_time = int(time.mktime(datetime.datetime(2022, 8, 11).timetuple())) * 1000

start_time = '2022-02-24T00:00:00Z'
end_time = '2022-12-31T23:59:59Z'

search_url = "https://api.twitter.com/2/tweets/search/all"
# query_params = {'query': '(from:CarloCalenda)', 'tweet.fields': 'author_id', 'tweet.fields': 'created_at', 'tweet.fields': 'public_metrics',
#                'max_results': 500, 'start_time': start_time, 'end_time': end_time}

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FullArchiveSearchPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request(
        "GET", search_url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


# make the first API call
query_params = {'query': '(from:NFratoianni -is:retweet)', 'tweet.fields': 'author_id,created_at,public_metrics',
                'max_results': 500, 'start_time': start_time, 'end_time': end_time}

json_response = connect_to_endpoint(search_url, query_params)

# extract the first set of results from the response
results = json_response['data']

print("Initial results pulled")

# check if there is a next token
if 'next_token' in json_response['meta']:
    next_token = json_response['meta']['next_token']

    # make a subsequent API call with the next token
    query_params = {'query': '(from:NFratoianni -is:retweet)', 'tweet.fields': 'author_id,created_at,public_metrics',
                    'max_results': 500, 'start_time': start_time, 'end_time': end_time, 'next_token': next_token}
    json_response = connect_to_endpoint(search_url, query_params)

    # add the next set of results to the existing results
    results += json_response['data']

    print("First additional pull: check")

# continue to make subsequent API calls with the next token until there are no more pages of results
while 'next_token' in json_response['meta']:
    next_token = json_response['meta']['next_token']
    query_params = {'query': '(from:NFratoianni -is:retweet)', 'tweet.fields': 'author_id,created_at,public_metrics',
                    'max_results': 500, 'start_time': start_time, 'end_time': end_time, 'next_token': next_token}
    json_response = connect_to_endpoint(search_url, query_params)
    results += json_response['data']
    print("Additional pull: check once again!")

# save results in a json file
with open('results.json', 'w') as f:
    json.dump(results, f, indent=4)

print("Done!")
