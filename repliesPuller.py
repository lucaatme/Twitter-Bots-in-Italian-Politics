import requests
import json
import pandas as pd
import time
from config import *

bearer_token = TWITTER_BEARER_TOKEN

headers = {
    'Authorization': "Bearer " + str(TWITTER_BEARER_TOKEN),
    'User-Agent': "v2FullArchiveSearchPython"
}

start_time = '2022-02-24T00:00:00Z'
end_time = '2022-04-01T23:59:59Z'

# search_url = "https://api.twitter.com/2/tweets/search/recent"
search_url = "https://api.twitter.com/2/tweets/search/all"


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


query_params = {'query': '(to:LegaSalvini -is:retweet)', 'tweet.fields': 'author_id,created_at,public_metrics',
                'max_results': 100, 'start_time': start_time, 'end_time': end_time}

json_response = connect_to_endpoint(search_url, query_params)

print("About to pull...")

results = json_response['data']

print("Initial results pulled")

# save results in a json file
with open('results.json', 'w') as f:
    json.dump(results, f, indent=4)

# check if there is a next token
if 'next_token' in json_response['meta']:
    time.sleep(10)
    next_token = json_response['meta']['next_token']

    # make a subsequent API call with the next token
    query_params = {'query': '(to:LegaSalvini -is:retweet)', 'tweet.fields': 'author_id,created_at,public_metrics',
                    'max_results': 100, 'start_time': start_time, 'end_time': end_time, 'next_token': next_token}
    json_response = connect_to_endpoint(search_url, query_params)

    # add the next set of results to the existing results
    results += json_response['data']

    print("First additional pull: check")

    # save results in the same json file (append)
    with open('results.json', 'w') as f:
        json.dump(results, f, indent=4)

# continue to make subsequent API calls with the next token until there are no more pages of results
while 'next_token' in json_response['meta']:
    time.sleep(10)
    next_token = json_response['meta']['next_token']
    query_params = {'query': '(to:LegaSalvini -is:retweet)', 'tweet.fields': 'author_id,created_at,public_metrics',
                    'max_results': 100, 'start_time': start_time, 'end_time': end_time, 'next_token': next_token}

    json_response = connect_to_endpoint(search_url, query_params)
    results += json_response['data']
    print("Additional pull: check once again!")

    with open('results.json', 'w') as f:
        json.dump(results, f, indent=4)

print("Done!")
