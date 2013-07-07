import yaml
import os

class Config:
    """ twitter config """
    __FILE_NAME = "/config.yaml"
    def __init__(self):
        conf = yaml.load(open(os.path.dirname(__file__) + self.__FILE_NAME).read())
        self.__CONSUMER_KEY    = conf["config"]["consumer_key"]
        self.__CONSUMER_SECRET = conf["config"]["consumer_secret"]
        self.__ACCESS_TOKEN    = conf["config"]["access_token"]
        self.__ACCESS_TOKEN_SECRET = conf["config"]["access_token_secret"]
        self.__OUTPUT_FILE     = conf["config"]["output_file"]

    @property
    def CONSUMER_KEY(self):
        return self.__CONSUMER_KEY

    @property
    def CONSUMER_SECRET(self):
        return self.__CONSUMER_SECRET

    @property
    def ACCESS_TOKEN(self):
        return self.__ACCESS_TOKEN

    @property
    def ACCESS_TOKEN_SECRET(self):
        return self.__ACCESS_TOKEN_SECRET

    @property
    def OUTPUT_FILE(self):
        return self.__OUTPUT_FILE
