# IN ORDER TO RUN THIS an Academic Researcher API profile is required.

import requests
import os
import json
from config import *
import time
import datetime

bearer_token = TWITTER_BEARER_TOKEN

start_time = "YYYY-MM-DDTHH:MM:SSZ"
end_time = "YYYY-MM-DDTHH:MM:SSZ"

search_url = "https://api.twitter.com/2/tweets/search/all"


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FullArchiveSearchPython"
    return r


# forgery of the GET request
def connect_to_endpoint(url, params):
    response = requests.request("GET", search_url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


# make the first API call, filtering out all the retweets with an appropriate flag
query_params = {
    "query": "(from:username -is:retweet)",
    "tweet.fields": "author_id,created_at,public_metrics",
    "max_results": 500,
    "start_time": start_time,
    "end_time": end_time,
}

json_response = connect_to_endpoint(search_url, query_params)

# extract the first set of results from the response
results = json_response["data"]

print("Initial results pulled")

# check if there is a next token
if "next_token" in json_response["meta"]:
    next_token = json_response["meta"]["next_token"]

    # make a subsequent API call with the next token
    query_params = {
        "query": "(from:username -is:retweet)",
        "tweet.fields": "author_id,created_at,public_metrics",
        "max_results": 500,
        "start_time": start_time,
        "end_time": end_time,
        "next_token": next_token,
    }
    json_response = connect_to_endpoint(search_url, query_params)

    # add the next set of results to the existing results
    results += json_response["data"]

    print("First additional pull: check")

# continue to make subsequent API calls with the next token until there are no more pages of results
while "next_token" in json_response["meta"]:
    next_token = json_response["meta"]["next_token"]
    query_params = {
        "query": "(from:username -is:retweet)",
        "tweet.fields": "author_id,created_at,public_metrics",
        "max_results": 500,
        "start_time": start_time,
        "end_time": end_time,
        "next_token": next_token,
    }
    json_response = connect_to_endpoint(search_url, query_params)
    results += json_response["data"]
    print("Additional pull: check once again!")

# save results in a json file
with open("results.json", "w") as f:
    json.dump(results, f, indent=4)

print("Done!")
