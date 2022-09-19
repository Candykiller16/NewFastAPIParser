from src.di.container_dao import ContainerDAO
from src.di.container_general import ContainerGeneral

container_general = ContainerGeneral()
dao_container = ContainerDAO(container_general)
