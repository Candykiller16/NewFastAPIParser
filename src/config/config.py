from pydantic import BaseSettings

_CONFIG_PREFIX = 'FASTAPI_SERVICE_'


class Service(BaseSettings):
    host: str
    port: int

    class Config:
        env_prefix = _CONFIG_PREFIX + 'CONTAINER_'
        env_file = '.env'
        env_file_encoding = 'utf-8'


class MongoDB(BaseSettings):
    host: str
    port: int
    username: str
    password: str

    class Config:
        env_prefix = _CONFIG_PREFIX + 'MONGO_'
        env_file = '.env'
        env_file_encoding = 'utf-8'


class LamodaUrl(BaseSettings):
    sneakers_url = "https://www.lamoda.by/c/5971/shoes-muzhkrossovki/?sitelink=topmenuM&l=5"


class Config(BaseSettings):
    service: Service = Service()
    mongodb: MongoDB = MongoDB()
    lamoda_url: LamodaUrl = LamodaUrl()

    class Config:
        env_prefix = _CONFIG_PREFIX
        env_file = '.env'
        env_file_encoding = 'utf-8'
