# this script is used to create a list of bots from a json file
import json


with open('finalBotsNicolaFratoianni.json') as f:
    data = json.load(f)
    # load the usernames of the bots
#    for bot in data:
#        print(bot['user']['user_data']['id_str'])

full_content = []

for i in range(1, 31):
    with open('botometer_results_NicolaFratoianni' + str(i) + '.json') as f:
        data1 = json.load(f)
        full_content.append(data1)

full_bots = []
# open the txt file and insert each bot in full_bots
with open('botsIdNicolaFratoianni.txt') as f:
    for line in f:
        full_bots.append(line.strip())

not_bots = []

for comment in full_content:
    for user in comment:
        if (user['user']['user_data']['id_str']) not in full_bots:
            not_bots.append(user)
        else:
            continue

with open('not_bots_NicolaFratoianni.json', 'w') as f:
    json.dump(not_bots, f, indent=4)


with open('not_bots_NicolaFratoianni.json') as f:
    data = json.load(f)
    # load the usernames of the bots
    for bot in data:
        print(bot['user']['user_data']['id_str'])
