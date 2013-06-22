#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
from optparse import OptionParser

import tweepy
from DescriptionEntity import DescriptionEntity
from LocationEntity import LocationEntity
from Config import Config

def getApi(conf):
    auth = tweepy.OAuthHandler(conf.CONSUMER_KEY,conf.CONSUMER_SECRET)
    auth.set_access_token(conf.ACCESS_TOKEN, conf.ACCESS_TOKEN_SECRET)
    return tweepy.API(auth_handler=auth)

def update(api=None):
    desc = DescriptionEntity().get()
    loc = LocationEntity().get()
    if api:
        api.update_profile(description=desc, location=loc)
    return {"description": desc, "location": loc }

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-d", "--debug",
        action="store_true", dest="debug", default=False,
        help="debug mode: twitter api no use")
    (options, args) = parser.parse_args()

    api = None
    if not options.debug:
        api = getApi(Config())

    log = update(api)
    print "debug" if options.debug else "normal"
    print log["description"]
    print log["location"]
