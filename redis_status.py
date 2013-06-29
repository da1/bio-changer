import redis
from modules.db.users import Users

if __name__ == "__main__":
    users = Users()
    print 'dbsize',users.dbsize()
    keys = users.get_keys()
    print 'keys', len(keys)
    for key in ['no', 'miss', 'slash']:
        print key, users.count(key)
