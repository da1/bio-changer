import tweepy
from modules.Config import Config
import random

def get_api(conf=None):
    if not conf:
        conf = Config()

    auth = tweepy.OAuthHandler(conf.CONSUMER_KEY,conf.CONSUMER_SECRET)
    auth.set_access_token(conf.ACCESS_TOKEN, conf.ACCESS_TOKEN_SECRET)
    return tweepy.API(auth_handler=auth)

def randomly_select(lists):
    return lists[random.randint(0,len(lists)-1)]

if __name__ == "__main__":
    pass
