import tweepy
import json
import random


data = json.load(open('all_tweets.json'))

random_tweet = random.choice(data)

# print(random_tweet)

consumer_key = "REPLACE-ME"
consumer_secret = "REPLACE-ME"
access_token = "REPLACE-ME"
access_token_secret = "REPLACE-ME"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

client = tweepy.Client(consumer_key='REPLACE-ME',
                       consumer_secret='REPLACE-ME',
                       access_token='REPLACE-ME',
                       access_token_secret='REPLACE-ME')

response = client.create_tweet(text=random_tweet)

# print(response)

# tweet_post_result = api.update_status(random_tweet)






