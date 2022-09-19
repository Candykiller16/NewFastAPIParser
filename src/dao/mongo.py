import pymongo

from src.config.config import Config


class Mongo:
    def __init__(self, config: Config):
        self.__client = pymongo.MongoClient(
            host=config.mongodb.host,
            port=config.mongodb.port,
            username=config.mongodb.username,
            password=config.mongodb.password
        )
        self._db = None

    @property
    def db(self):
        return self.__client.db
