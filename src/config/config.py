from pydantic import BaseSettings

_CONFIG_PREFIX = 'FASTAPI_SERVICE_'


class Service(BaseSettings):
    host: str
    port: int

    class Config:
        env_prefix = _CONFIG_PREFIX + 'CONTAINER_'
        env_file = '.env'
        env_file_encoding = 'utf-8'


class Config(BaseSettings):
    service: Service = Service()

    class Config:
        env_prefix = _CONFIG_PREFIX
        env_file = '.env'
        env_file_encoding = 'utf-8'
