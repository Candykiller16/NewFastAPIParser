from src.controllers.lamoda_controller import LamodaController


class ContainerController:
    def __init__(self, db):
        self._lamoda = LamodaController(db)

    @property
    def lamoda(self):
        return self._lamoda
