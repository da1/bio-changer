#-*- coding:utf-8 -*-
from BaseModel import BaseModel

class DescriptionModel(BaseModel):
    __descriptions = [u"だるい", u"にょわー", u"ねばねばー"]
    def get(self):
        return self._random_pickup(self.__descriptions)
