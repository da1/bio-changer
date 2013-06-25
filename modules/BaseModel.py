import random

class BaseModel:
    def _random_pickup(self, list):
        random.shuffle(list)
        if len(list) >= 1:
            return list[0]
        else:
            return ""

    def get(self):
        pass
