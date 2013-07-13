#-*- coding:utf-8 -*-
from BaseModel import BaseModel
from Config import Config
import codecs

class SlashDescriptionModel(BaseModel):
    __descriptions = []
    __filepath = Config().OUTPUT_FILE;
    __WORD_COUNT = 10
    def __init__(self):
        with codecs.open(self.__filepath, 'r', 'utf-8') as f:
            self.__descriptions = f.readlines()
    def __get(self):
        return self._random_pickup(self.__descriptions).rstrip("\n")
    def get(self):
        return '/'.join(map((lambda x:self.__get()), range(self.__WORD_COUNT)))

if __name__ == "__main__":
    model = SlashDescriptionModel()
    print model.slash_gets(10)
