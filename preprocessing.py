import json
import numpy as np
import botometer
from config import *
import json

with open('nameFile.json') as f:
    data = json.load(f)

list_authors = []

print(len(data))

for i in range(len(data)):
    list_authors.append(data[i]['author_id'])

modified_list = np.unique(list_authors)

print(len(modified_list))

list_authors = []

rapidapi_key = RAPID_API_KEY
twitter_app_auth = {
    'consumer_key': TWITTER_CONSUMER_KEY,
    'consumer_secret': TWITTER_CONSUMER_SECRET,
    'access_token': TWITTER_ACCESS_TOKEN,
    'access_token_secret': TWITTER_ACCESS_TOKEN_SECRET,
}
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

for account in modified_list:
    result = bom.check_account(account)
    list_authors.append(result)
    print("Account: ", account, " checked!")

with open('botometerResult.json', 'w') as f:
    json.dump(list_authors, f, indent=4)
