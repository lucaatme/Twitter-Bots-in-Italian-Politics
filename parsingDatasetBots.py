import json
import csv

list_of_bots = []

# open the json file
with open('finalBotsNicolaFratoianni.json') as f:
    data = json.load(f)

    # load the usernames of the bots
    for bot in data:
        list_of_bots.append(bot['user']['user_data']['id_str'])

# open the corresponding csv file
with open('resultsNicolaFratoianni_edited_final.csv') as f:
    reader = csv.reader(f)
    # create a new csv file
    with open('resultsNicolaFratoianniWithoutBots.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        # iterate for each tweet
        for row in reader:
            # if the tweet is from a bot, write it in the new csv file
            if row[2] not in list_of_bots:
                writer.writerow(row)

print("Done")
