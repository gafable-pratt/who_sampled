import tweepy
import json
import random

def lambda_handler(event, context):

	data = json.load(open('all_tweets.json'))

	random_tweet = random.choice(data)

	# print(random_tweet)

	consumer_key = "pKnIw50RyhNw6PXvdgnaupD4v"
	consumer_secret = "Bj4D3PCeKewhOAu7wDSjLHYfG1rF3xg3FhacBR75hZuZgfwqAp"
	access_token = "1590453249982726147-373V3Cqp1tCGkMT5YO5W7a8nO9Nszt"
	access_token_secret = "zR57ZBl1aAf08jOot9AAJp6euFNPixqapihXGj1tdKPVR"

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	client = tweepy.Client(consumer_key='pKnIw50RyhNw6PXvdgnaupD4v',
	                       consumer_secret='Bj4D3PCeKewhOAu7wDSjLHYfG1rF3xg3FhacBR75hZuZgfwqAp',
	                       access_token='1590453249982726147-373V3Cqp1tCGkMT5YO5W7a8nO9Nszt',
	                       access_token_secret='zR57ZBl1aAf08jOot9AAJp6euFNPixqapihXGj1tdKPVR')

	response = client.create_tweet(text=random_tweet)


	return {
		'statusCode': 200,
		'body': json.dumps('Hello from Lambda!')


