import json
import requests

all_tweets = []

with open('sample_data.json', 'r') as jsondatafile:

	jsondata = json.load(jsondatafile)

	for entry in jsondata:
		
		tweet_string = f"Did You Know?\n{entry['track_artist']}'s \"{entry['track_name']}\" samples {entry['sampled_artist']}'s \"{entry['sample_name']}\"\n{entry['sample_url']}"

		print(tweet_string)
		all_tweets.append(tweet_string)
		

json.dump(all_tweets, open('all_tweets.json', 'w'),indent=2)


