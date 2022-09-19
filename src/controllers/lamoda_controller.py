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