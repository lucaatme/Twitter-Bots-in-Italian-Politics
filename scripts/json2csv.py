import json
import csv

# this code is used to convert the json file into a csv file
with open("FILE.json") as json_file:
    data = json.load(json_file)
    tweet_data = data["data"]
    with open("results.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        count = 0
        for tweet in tweet_data:
            if count == 0:
                header = tweet.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(tweet.values())
        print("Done!")
