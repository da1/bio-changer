import ConfigParser
import os

class Config:
    """ twitter config """
    __FILE_NAME = "/config.ini"
    def __init__(self):
        conf = ConfigParser.SafeConfigParser()
        conf.read(os.path.dirname(__file__) + self.__FILE_NAME)
        self.__CONSUMER_KEY    = conf.get("config", "consumer_key")
        self.__CONSUMER_SECRET = conf.get("config", "consumer_secret")
        self.__CALLBACK_URL    = conf.get("config", "callback_url")
        self.__ACCESS_TOKEN    = conf.get("config", "access_token")
        self.__ACCESS_TOKEN_SECRET = conf.get("config", "access_token_secret")

    @property
    def CONSUMER_KEY(self):
        return self.__CONSUMER_KEY

    @property
    def CONSUMER_SECRET(self):
        return self.__CONSUMER_SECRET

    @property
    def CALLBACK_URL(self):
        return self.__CALLBACK_URL

    @property
    def ACCESS_TOKEN(self):
        return self.__ACCESS_TOKEN

    @property
    def ACCESS_TOKEN_SECRET(self):
        return self.__ACCESS_TOKEN_SECRET
