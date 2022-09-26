from src.dao.mongo import Mongo
from src.di.container_general import ContainerGeneral
from src.parsers.lamoda_parser import LamodaParser
from src.parsers.twich_api import TwitchParser


class ContainerParser:
    def __init__(self, container_general: ContainerGeneral):
        self._container_general = container_general
        self._lamoda_parser = LamodaParser(container_general)
        self._twitch_parser = TwitchParser(container_general)

    @property
    def lamoda(self):
        return self._lamoda_parser

    @property
    def twitch(self):
        return self._twitch_parser
