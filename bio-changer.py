#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
from optparse import OptionParser

import tweepy
from modules.DescriptionModel import DescriptionModel
from modules.SlashDescriptionModel import SlashDescriptionModel
from modules.LocationModel import LocationModel
from modules import util

def update(api=None, models=[]):
    desc = '/'.join(map((lambda m:m.get()), models))
    loc = LocationModel().get()
    if api:
        api.update_profile(description=desc, location=loc)
    return {"description": desc, "location": loc }

def outputLog(mode, log):
    print "mode", mode
    print "description", log["description"].encode('utf-8')
    print "location", log["location"].encode('utf-8')

def modeStr(options):
    return "debug" if options.debug else "normal"

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-d", "--debug",
        action="store_true", dest="debug", default=False,
        help="debug mode: twitter api no use")
    (options, args) = parser.parse_args()

    api = None
    if not options.debug:
        api = util.get_api()

    log = update(api, [DescriptionModel(), SlashDescriptionModel()])
    outputLog(modeStr(options), log)
