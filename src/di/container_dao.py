from src.dao.mongo import Mongo
from src.di.container_general import ContainerGeneral


class ContainerDAO:
    def __init__(self, container_general: ContainerGeneral):
        self._config = container_general.config
        self._db = Mongo(self._config).db

    @property
    def db(self) -> Mongo:
        return self._db
