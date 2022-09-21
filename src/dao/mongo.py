from typing import Dict

from bson.objectid import ObjectId
from fastapi import Body
from starlette.exceptions import HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from src.models.lamoda.sneakers import SneakersCreateUpdate, SneakersResponse, Sneakers
from src.models.twitch.streams import Streams, StreamsCreateUpdate, StreamsResponse


class Mongo:
    def __init__(self, db):
        self.__db = db

    # For Lamoda_parser methods

    def drop_collection(self):
        return self.__db.db.lamoda.drop()

    def count_documents(self):
        return self.__db.db.lamoda.count_documents({})

    def insert_sneakers(self, sneakers):
        return self.__db.db.lamoda.insert_many(sneakers)

    def create(self, sneaker: SneakersCreateUpdate = Body(...)) -> Dict[str, str]:
        new_shoe = self.__db.db.lamoda.insert_one(sneaker.dict())
        return {"_id": str(new_shoe.inserted_id), **sneaker.dict()}

    def get_sneakers(self) -> SneakersResponse:
        return SneakersResponse(sneakers=list(self.__db.db.lamoda.find()))

    def get_one(self, _id: str) -> Sneakers:
        data = self.__db.db.lamoda.find_one({'_id': ObjectId(_id)})
        if data is not None:
            data['_id'] = str(data['_id'])
            return data
        else:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'Sneaker with ID {_id} not found')

    def update_one(self, _id, sneaker: SneakersCreateUpdate = Body(...)):
        data = self.__db.db.lamoda.find_one({'_id': ObjectId(_id)})
        if data is not None:
            self.__db.db.lamoda.update_one({'_id': ObjectId(_id)}, {'$set': sneaker.dict()})
            return {'_id': _id, **sneaker.dict()}
        else:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'Sneaker with ID {_id} not found')

    def delete_one(self, _id):
        data = self.__db.db.lamoda.find_one({'_id': ObjectId(_id)})
        if data is not None:
            self.__db.db.lamoda.delete_one({'_id': ObjectId(_id)})
            return {"message": f"Sneaker with ID {_id} was deleted"}
        else:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'Sneaker with ID {_id} not found')

    # For Twich_parser methods

    def drop_twich_collection(self):
        return self.__db.db.twitch.drop()

    def count_twitch_documents(self):
        return self.__db.db.twitch.count_documents({})

    def insert_streams(self, streams):
        return self.__db.db.twitch.insert_many(streams)

    def get_streams(self) -> StreamsResponse:
        return StreamsResponse(streams=list(self.__db.db.twitch.find()))
