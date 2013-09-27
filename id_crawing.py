import tweepy
from modules import util
from optparse import OptionParser
import sys
from modules.db.users import Users

def get_followers_ids(api, user_id):
    user_obj = api.get_user(user_id)
    followers_ids = []
    try:
        followers_ids = user_obj.followers_ids()
        print user_obj.screen_name, "has", len(followers_ids), "follower"
    except tweepy.TweepError, e:
        pass
    return followers_ids

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-n", "--name",
            action="store", type="string", dest="name", default="")
    (options, args) = parser.parse_args()

    init_user_screen_name = options.name
    api = util.get_api()

    users = Users()
    if users.dbsize() == 0 and init_user_screen_name != "":
        followers_ids = get_followers_ids(api, init_user_screen_name)
        count = users.set_users(followers_ids)
        print "init_user set_ids", count

    users_keys = users.get_keys()
    for i in range(100):
        followers_ids = get_followers_ids(api, util.randomly_select(users_keys))
        if len(followers_ids) > 0:
            count = users.set_users(followers_ids)
            print "user set_ids", count
            break
    else:
        sys.stderr.write('cannot get followers_ids\n')
