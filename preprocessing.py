import json
import numpy as np
import botometer
from config import *
import json
import time

with open('resultsMatteoSalvini.json') as f:
    data = json.load(f)

list_authors = []

print(len(data))

for i in range(len(data)):
    list_authors.append(data[i]['author_id'])

modified_list = np.unique(list_authors)

print(len(modified_list))

bots = []
not_bots = []
pre_parsed_bots = []
pre_parsed_not_bots = []

with open('FULL_LIST_BOTS.txt') as f:
    for line in f:
        bots.append(line.strip())

print("List of well known bots loaded")

with open('FULL_LIST_NOT_BOTS.txt') as f:
    for line in f:
        not_bots.append(line.strip())

print("List of well known not bots loaded")

modified_list = modified_list.tolist()

for element in modified_list:
    if element in bots:
        modified_list.remove(element)
        pre_parsed_bots.append(element)
    elif element in pre_parsed_not_bots:
        modified_list.remove(element)
        pre_parsed_not_bots.append(element)
    else:
        continue

print(len(modified_list))

with open('pre_parsed_bots_MatteoSalvini.json', 'w') as f:
    json.dump(pre_parsed_bots, f, indent=4)

with open('pre_parsed_not_bots_MatteoSalvini.json', 'w') as f:
    json.dump(pre_parsed_not_bots, f, indent=4)

# for author in modified_list:
#    print(author)

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

list_authors = []
counter = 0
for account in modified_list:
    counter = counter + 1
    try:
        result = bom.check_account(account)
        list_authors.append(result)
        print("Account: ", account, " checked! Counter is at ",
              counter, " out of ", len(modified_list), " accounts.")
    except Exception as e:
        continue
    if counter % 100 == 0 or counter == len(modified_list):
        print("Saving results...")
        with open('botometer_results_MatteoSalvini' + str(counter) + '.json', 'w') as f:
            json.dump(list_authors, f, indent=4)
        time.sleep(60)
        list_authors = []
