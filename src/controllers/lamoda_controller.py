from typing import Dict

from bson import ObjectId
from fastapi import Body
from starlette.exceptions import HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from src.models.lamoda.sneakers import SneakersCreateUpdate, Sneakers, SneakersResponse


class LamodaController:
    def __init__(self, db):
        self._db = db
        self._collection = db.lamoda

    @property
    def collection(self):
        return self._collection

    # CRUD operations for LamodaController to call them from ContainerController
    def create_list(self, product_list: list):
        return self.collection.insert_many(product_list)

    def create(self, sneaker: SneakersCreateUpdate = Body(...)) -> Dict[str, str]:
        new_shoe = self.collection.insert_one(sneaker.dict())
        return {"_id": str(new_shoe.inserted_id), **sneaker.dict()}

    def get_list(self) -> SneakersResponse:
        return SneakersResponse(sneakers=list(self.collection.find()))

    def get(self, _id: str) -> Sneakers:
        data = self.collection.find_one({'_id': ObjectId(_id)})
        if data is not None:
            data['_id'] = str(data['_id'])
            return data
        else:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'Sneaker with ID {_id} not found')
