from src.di.container_dao import ContainerDAO
from src.di.container_general import ContainerGeneral
from src.di.container_parser import ContainerParser

container_general = ContainerGeneral()
dao_container = ContainerDAO(container_general)
container_parser = ContainerParser(container_general)
