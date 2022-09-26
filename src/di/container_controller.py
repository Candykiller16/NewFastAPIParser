from src.controllers.lamoda_controller import LamodaController
from src.controllers.twitch_controller import TwitchController


class ContainerController:
    def __init__(self, db):
        self._lamoda = LamodaController(db)
        self._twitch = TwitchController(db)

    @property
    def lamoda(self) -> LamodaController:
        return self._lamoda

    @property
    def twitch(self) -> TwitchController:
        return self._twitch
