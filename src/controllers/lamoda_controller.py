from bson import ObjectId


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

    def get_list(self):
        data_list = []

        for data in self.collection.find():
            data['_id'] = str(data['_id'])
            data_list.append(data)

        return data_list

    def get(self, _id: str):
        data = self.collection.find_one({'_id': ObjectId(_id)})
        data['_id'] = str(data['_id'])
        return data
