import json
import csv

users = ["CarloCalenda", "EmmaBonino", "EnricoLetta", "GiorgiaMeloni",
         "GiuseppeConte", "MatteoSalvini", "NicolaFratoianni", "SilvioBerlusconi"]

for user in users:
    # get the json file
    with open('results' + user + '.json') as f:
        data = json.load(f)

    # create the header row
    header = ['text', 'created_at', 'author_id', 'id']

    # open the csv file
    with open('results' + user + '.csv', 'w', newline='') as f:
        # create a writer object
        writer = csv.writer(f)
        # write the header row
        writer.writerow(header)

        # iterate for each tweet
        for tweet in data:
            # write the tweet as a row in the csv file
            writer.writerow([tweet['text'], tweet['created_at'],
                            tweet['author_id'], tweet['id']])

    print("User " + user + " converted to csv")
