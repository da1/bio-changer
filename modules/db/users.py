import redis

class Users:
    def __init__(self):
        self.db = redis.StrictRedis(host="localhost", port=6379, db=0)

    def set_user(self, user_id):
        self.db.set(user_id, 'no')

    def set_users(self, user_ids):
        count = 0
        for i in user_ids:
            if self.db.get(i) == None:
                self.set_user(i)
                count+=1
        return count

    def set_miss(self, user_id):
        self.db.set(user_id, 'miss')

    def set_slash(self, user_id):
        self.db.set(user_id, 'slash')

    def dbsize(self):
        return self.db.dbsize()

    def get_keys(self):
        return self.db.keys()

    def count(self, keyword):
        return len(filter(lambda k:self.db.get(k) == keyword, self.get_keys()))
