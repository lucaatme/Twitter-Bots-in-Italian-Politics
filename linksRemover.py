import csv
import re

csv_list = []  # Insert here the list of csv files to edit

for party in csv_list:
    with open(party, 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    # iterate for each row and print the content of the field "tweets"
    for row in your_list:
        # print(row[1])
        # substitute a string with a space
        row[1] = re.sub(r"https://t\.co/\w+", "", row[1])
    print("Party " + party + " edited")
    # save the new list in a csv file
    with open(party[:-4] + "_edited.csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerows(your_list)
