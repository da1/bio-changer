import tweepy
from modules import util
import sys
from optparse import OptionParser
import re
from modules.db.users import Users
import logging

def remove_url(text):
    pattern = re.compile('https?:.+?[ \n]')
    return pattern.sub('', text)

def word_length(word):
    return 0 < len(word) < 10

def char_type(word):
    pattern = re.compile(u'[\x00-\x7F\u30A0-\u30FF\u3040-\u309F\u4E00-\u9FFF]+')
    return pattern.match(word)

def word_filter(word):
    return word_length(word) and char_type(word)

def split_slash(description):
    no_url_description = remove_url(description)
    if no_url_description.find('/') < 0:
        return []
    return [x for x in no_url_description.split('/') if word_filter(x)]

def split_descriptions(description):
    desc = reduce(lambda a,b:a+b,
            map(lambda x:split_slash(x), description.split('\n')))
    if len(desc) < 5:
        return []
    return desc

def get_user(users=None):
    if users == None:
        users = Users()
    if users.dbsize() == 0:
        raise Exception, "redis key is empty"
    return util.randomly_select(users.get_keys())

def showDescriptions(screen_name, descriptions):
    for d in descriptions:
        print d.encode('utf-8')
        logging.info("screen_name:%s\tdescription:%s"%(screen_name, d))

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-d", "--debug",
        action="store_true", dest="debug", default=False,
        help="debug mode: twitter api no use")
    parser.add_option("-n", "--name",
            action="store", type="string", dest="name", default="")
    parser.add_option("-r", "--no-redis",
            action="store_true", dest="no_redis", default=False)
    (options, args) = parser.parse_args()

    LOG_FILENAME = 'bio-changer/log/update.log'
    formatter = "time:%(asctime)s\tname:%(name)s\tlevelname:%(levelname)s\t%(message)s"
    logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO,format=formatter)

    users = None
    user_id = options.name
    if not options.no_redis:
        users = Users()
        user_id = get_user(users)

    api = util.get_api()
    screen_name = ""
    description = ""
    try:
        user = api.get_user(user_id)
        screen_name = user.screen_name
        description = user.description
    except tweepy.error.TweepError, e:
        pass

    logging.info("user_id:%s\tscreen_name:%s"%(user_id, screen_name))

    if options.debug:
        print "=== debug ==="
        print description.encode('utf-8')
        print "============="

    descriptions = split_descriptions(description)
    if not options.no_redis:
        if len(descriptions) == 0:
            users.set_miss(user_id)
        else:
            users.set_slash(user_id)

    showDescriptions(screen_name, descriptions)
