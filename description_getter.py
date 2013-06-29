import tweepy
from modules import util
import sys
from optparse import OptionParser
import re
from modules.db.users import Users

def remove_url(text):
    pattern = re.compile('https?:\S+$')
    return pattern.sub('', text)

def word_filter(word):
    return 0 < len(word) < 10

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

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-d", "--debug",
        action="store_true", dest="debug", default=False,
        help="debug mode: twitter api no use")
    (options, args) = parser.parse_args()

    users = Users()
    if users.dbsize() == 0:
        sys.stderr.write("redis key is empty\n")
        sys.exit(0)

    api = util.get_api()
    user_id = util.randomly_select(users.get_keys())
    user = api.get_user(user_id)

    if options.debug:
        print "=== debug ==="
        print user.description.encode('utf-8')
        print "============="

    descriptions = split_descriptions(user.description)
    if len(descriptions) == 0:
        users.set_miss(user_id)
    else:
        users.set_slash(user_id)

    for d in descriptions:
        print d.encode('utf-8')
