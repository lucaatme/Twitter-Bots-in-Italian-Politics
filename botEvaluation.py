import json
from matplotlib import pyplot as plt
import seaborn as sns

sns.set_theme(style="white", font_scale=2)

data = []

bots = []

for i in range(10):
    with open('botometer_results' + str(i) + '.json') as f:
        data += json.load(f)

bot_counter = 0

#for user in data:
#    if user['raw_scores']['universal']['overall'] >= user['cap']['universal']:
#        bot_counter += 1
#        bots.append(user)

# save bots to json file
with open('botsAzIv.json', 'w') as f:
    json.dump(bots, f, indent=4)


# print an histogram that compares the number of bots and non bots
print("Number of bots: ", bot_counter)
print("Number of non bots: ", len(data) - bot_counter)

final_data = [bot_counter, len(data) - bot_counter]

fig = plt.figure(figsize=(10, 7))

percentages = [bot_counter/len(data), (len(data) - bot_counter)/len(data)]

plt.pie(final_data, labels=["Bots", "Real"],
        autopct='%1.1f%%', startangle=90, explode=(0.1, 0), colors=['orange', 'lightblue'])

plt.show()

# save the figure
fig.savefig('botAzIv.png', dpi=300)
