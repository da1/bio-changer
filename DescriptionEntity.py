#-*- coding:utf-8 -*-
from EntityBase import EntityBase

class DescriptionEntity(EntityBase):
    __descriptions = [u"だるい", u"にょわー", u"ねばねばー"]
    def get(self):
        return self._random_pickup(self.__descriptions)
