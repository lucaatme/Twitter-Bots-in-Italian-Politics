import json
from matplotlib import pyplot as plt

data = []

for i in range(4):
    with open('botometer_results_FdI_' + str(i) + '.json') as f:
        data += json.load(f)

bot_counter = 0

for user in data:
    if user['raw_scores']['universal']['overall'] >= user['cap']['universal']:
        bot_counter += 1


# print an histogram that compares the number of bots and non bots
print("Number of bots: ", bot_counter)
print("Number of non bots: ", len(data) - bot_counter)

final_data = [bot_counter, len(data) - bot_counter]

fig = plt.figure(figsize=(10, 7))

percentages = [bot_counter/len(data), (len(data) - bot_counter)/len(data)]

plt.pie(final_data, labels=["Bots", "Real"],
        autopct='%1.1f%%', startangle=90, explode=(0.1, 0), colors=['lightgreen', 'lightblue'])

plt.show()
