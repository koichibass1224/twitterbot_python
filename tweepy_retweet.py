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

# 単体tweet
# search_results = api.search(q="メディアアート", count=1)

# for result in search_results:
#     tweet_id = result.id
#     user_id = result.user._json['id']  # ←追記
#     try:
#         api.create_favorite(tweet_id)
#         # api.retweet(tweet_id)          # ←追記
#         # api.create_friendship(user_id) # ←追記
#     except Exception as e:
#         print(e)

# 配列で連続
q_list = ["杉山学長","#メディアアート","デジハリ","#落合陽一","チームラボ"]
count  = 1

for q in q_list:
    search_results = api.search(q=q, count=count)
    for result in search_results:
        tweet_id = result.id
        user_id  = result.user._json['id']
        try:
            api.create_favorite(tweet_id)
            # api.retweet(tweet_id)
            # api.create_friendship(user_id)
        except Exception as e:
            print(e)