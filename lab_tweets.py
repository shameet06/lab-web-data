# Load master_2009.json through master_2018.json, analyze the tweets, and make a bar chart.
# Follow the linked course assignment in README.md.
import json
import matplotlib.pyplot as plt

phrases = ['Obama', 'Trump', 'Mexico', 'Russia', 'Fake News', 'freedom', 'America', 'jobs']

tweets = []
for year in range(2009, 2019):
    filename = 'master_' + str(year) + '.json'

    with open(filename, encoding='utf-8') as f:
        jsontext = f.read()

    year_tweets = json.loads(jsontext)

    for tweet in year_tweets:
        tweets.append(tweet)

print("Total tweets:", len(tweets))

counts = {}
for phrase in phrases:
    counts[phrase] = 0

for tweet in tweets:
    if "full_text" in tweet:
        text = tweet["full_text"]
    else:
        text = tweet["text"]

    text = text.lower()

    for phrase in phrases:
        if phrase.lower() in text:
            counts[phrase] = counts[phrase] + 1


for phrase in phrases:
    print(phrase, counts[phrase])

percentages = {}

for phrase in phrases:
    percentages[phrase] = counts[phrase] / len(tweets) * 100

print()
print("| phrase            | percent of tweets |")
print("| ----------------- | ----------------- |")

for phrase in sorted(phrases):
    spaces = ' ' * (17 - len(phrase))
    name = spaces + phrase

    hundredths = int(round(percentages[phrase] * 100))
    whole = str(hundredths // 100)
    decimal = str(hundredths % 100)

    if len(whole) < 2:
        whole = '0' + whole

    if len(decimal) < 2:
        decimal = '0' + decimal

    percent_text = whole + '.' + decimal

    print('| ' + name + ' | ' + percent_text + '             |')

labels = []
values = []

for phrase in sorted(phrases):
    labels.append(phrase)
    values.append(percentages[phrase])


plt.bar(labels, values)
plt.xlabel("Phrase")
plt.ylabel("Percent of tweets")
plt.title("Mentions of Selected Phrases in the Tweet Archive")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("tweets.png")
plt.show()