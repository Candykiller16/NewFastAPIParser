from src.dao.mongo import Mongo
from src.models.twitch.streams import StreamsCreateUpdate


class TwitchController:
    def __init__(self, db: Mongo):
        self._db = db

    def drop_twitch_collection(self):
        return self._db.drop_twich_collection()

    def list_of_collections(self):
        return self._db.list_of_collections()

    def insert_streams_to_mongo(self, streams):
        return self._db.insert_streams(streams)

    def count_documents(self):
        return self._db.count_twitch_documents()

    def get_streams(self):
        return self._db.get_streams()

    def get_stream_by_id(self, _id):
        return self._db.get_one_stream(_id)

    def create_stream(self, stream: StreamsCreateUpdate):
        return self._db.create_stream(stream)

    def update_stream(self, _id, stream: StreamsCreateUpdate):
        return self._db.update_one_stream(_id, stream)

    def delete_stream(self, _id):
        return self._db.delete_one_stream(_id)
