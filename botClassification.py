import json
from matplotlib import pyplot as plt
import seaborn as sns

sns.set_theme(style="white", font_scale=1.0)


# read the json file
with open('file.json') as f:
    data = json.load(f)

financial_bots = 0
fake_followers_bots = 0
spammers_bots = 0
self_declared_bots = 0
other_bots = 0
astroturf_bots = 0

for bot in data:
    # find the max value between the categories
    max_value = max(bot['raw_scores']['universal']['astroturf'], bot['raw_scores']['universal']['financial'], bot['raw_scores']['universal']['fake_follower'],
                    bot['raw_scores']['universal']['other'], bot['raw_scores']['universal']['self_declared'], bot['raw_scores']['universal']['spammer'])

    # check which category has the max value
    if max_value == bot['raw_scores']['universal']['astroturf']:
        astroturf_bots += 1
    elif max_value == bot['raw_scores']['universal']['financial']:
        financial_bots += 1
    elif max_value == bot['raw_scores']['universal']['fake_follower']:
        fake_followers_bots += 1
    elif max_value == bot['raw_scores']['universal']['self_declared']:
        self_declared_bots += 1
    elif max_value == bot['raw_scores']['universal']['spammer']:
        spammers_bots += 1
    else:
        other_bots += 1

# plot the pie chart of the categories
final_data = [financial_bots, fake_followers_bots, spammers_bots,
              self_declared_bots, other_bots, astroturf_bots]

fig = plt.figure(figsize=(10, 7))

percentages = [financial_bots/len(data)*100, fake_followers_bots/len(data)*100, spammers_bots/len(
    data)*100, self_declared_bots/len(data)*100, other_bots/len(data)*100, astroturf_bots/len(data)*100]

# plot the pie chart without showing the percentages

plt.pie(final_data, startangle=90, colors=[
        'orange', 'lightblue', 'green', 'red', 'purple', 'yellow'], )

# plt.legend(loc="best", bbox_to_anchor=(1.2, 1), labels=['%s: %1.2f %%' % (
#    l, s) for l, s in zip(["Financial", "Fake Followers", "Spammers", "Self Declared", "Astroturf", "Other"], percentages)])


# add the legend with a bigger font size
plt.legend(loc="best", bbox_to_anchor=(1.2, 1), labels=['%s: %1.2f %%' % (
    l, s) for l, s in zip(["Financial", "Fake Followers", "Spammers", "Self Declared", "Astroturf", "Other"], percentages)], prop={'size': 23})


plt.show()

fig.savefig('figure.png', dpi=300)
