#-*- coding:utf-8 -*-
from BaseModel import BaseModel
from Config import Config
import codecs

class SlashDescriptionModel(BaseModel):
    __descriptions = []
    __filepath = Config().OUTPUT_FILE;
    def __init__(self):
        with codecs.open(self.__filepath, 'r', 'utf-8') as f:
            self.__descriptions = f.readlines()
    def get(self):
        return self._random_pickup(self.__descriptions).rstrip("\n")
    def slash_gets(self, n=10):
        words = [self.darui()] + map((lambda x:self.get()), range(n))
        return '/'.join(words)
    def darui(self):
        darui = [u"だるい", u"にょわー", u"ねばねばー"]
        return self._random_pickup(darui)

if __name__ == "__main__":
    model = SlashDescriptionModel()
    print model.slash_gets(10)
