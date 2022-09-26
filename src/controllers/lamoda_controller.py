from typing import Dict

from src.dao.mongo import Mongo
from src.models.lamoda.sneakers import SneakersCreateUpdate


class LamodaController:
    def __init__(self, db: Mongo):
        self._db = db

    def drop_collection(self):
        return self._db.drop_collection()

    def insert_sneaker_to_mongo(self, sneakers):
        return self._db.insert_sneakers(sneakers)

    def count_documents(self):
        return self._db.count_documents()

    # CRUD operations for LamodaController to call them from ContainerController
    def get_sneakers(self):
        return self._db.get_sneakers()

    def get_sneaker_by_id(self, _id):
        return self._db.get_one(_id)

    def create_sneaker(self, sneaker: SneakersCreateUpdate) -> Dict[str, str]:
        return self._db.create(sneaker)

    def update_sneaker(self, _id, sneaker: SneakersCreateUpdate):
        return self._db.update_one(_id, sneaker)

    def delete_sneaker(self, _id):
        return self._db.delete_one(_id)
