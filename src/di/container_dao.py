import pymongo

from src.dao.mongo import Mongo
from src.di.container_general import ContainerGeneral


class ContainerDAO:
    def __init__(self, container_general: ContainerGeneral):
        self._config = container_general.config
        self._db = None

    @property
    def mongo_source(self) -> Mongo:
        dsn = f'mongodb://{self._config.mongodb.username}:' \
              f'{self._config.mongodb.password}@{self._config.mongodb.host}:' \
              f'{self._config.mongodb.port}'
        connection = pymongo.MongoClient(dsn)
        return Mongo(connection)
