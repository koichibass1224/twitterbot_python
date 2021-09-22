import tweepy
# from config import CONFIG

import json
json_open = open('config.json', 'r')
json_load = json.load(json_open)

# print(json_load)

# CONSUMER_KEY = CONFIG["CONSUMER_KEY"]
# CONSUMER_SECRET = CONFIG["CONSUMER_SECRET"]
# ACCESS_TOKEN = CONFIG["ACCESS_TOKEN"]
# ACCESS_SECRET = CONFIG["ACCESS_SECRET"]

CONSUMER_KEY = json_load['CONSUMER_KEY']
CONSUMER_SECRET = json_load['CONSUMER_SECRET']
ACCESS_TOKEN = json_load['ACCESS_TOKEN']
ACCESS_SECRET = json_load['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

file_name = 'list.txt'

with open(file_name) as f:
    lines = f.readlines()
    # print(random.choice(lines))
    # api.update_status("Pythonから投稿!")
    api.update_status(random.choice(lines))