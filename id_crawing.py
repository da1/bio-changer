import tweepy
from modules import util
import redis
from optparse import OptionParser
import sys

def set_ids(redis_cli, ids):
    count = 0
    for i in ids:
        if redis_cli.get(i) == None:
            redis_cli.set(i, 'no')
            count+=1
    return count

def get_followers_ids(api, user_id):
    user_obj = api.get_user(user_id)
    followers_ids = user_obj.followers_ids()
    print user_obj.screen_name, "has", len(followers_ids), "follower"
    return followers_ids

if __name__ == "__main__":
    init_user_screen_name = ''
    api = util.get_api()
    redis_cli = redis.StrictRedis(host="localhost", port=6379, db=0)
    if redis_cli.dbsize() == 0 and init_user_screen_name != "":
        followers_ids = get_followers_ids(api, init_user_screen_name)
        count = set_ids(redis_cli, followers_ids)
        print "init_user set_ids", count

    redis_keys =  redis_cli.keys()
    for i in range(100):
        followers_ids = get_followers_ids(api, util.randomly_select(redis_keys))
        if len(followers_ids) > 0:
            count = set_ids(redis_cli, followers_ids)
            print "user set_ids", count
            break
    else:
        sys.stderr.write('cannot get followers_ids\n')
