from src.dao.mongo import Mongo


class TwitchController:
    def __init__(self, db: Mongo):
        self._db = db

    def drop_twitch_collection(self):
        return self._db.drop_twich_collection()

    def insert_streams_to_mongo(self, streams):
        return self._db.insert_streams(streams)

    def count_documents(self):
        return self._db.count_twitch_documents()

    def get_streams(self):
        return self._db.get_streams()

