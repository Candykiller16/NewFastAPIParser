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


class Kafka(BaseSettings):
    host: str
    port: int

    class Config:
        env_prefix = _CONFIG_PREFIX + 'KAFKA_'
        env_file = '.env'
        env_file_encoding = 'utf-8'


class LamodaUrl(BaseSettings):
    sneakers_url = "https://www.lamoda.by/c/5971/shoes-muzhkrossovki/?sitelink=topmenuM&l=5"


class Twitch(BaseSettings):
    streams = "https://api.twitch.tv/helix/streams"
    auth_url = "https://id.twitch.tv/oauth2/token"
    client_id = "ec1z6hfqa4kdyjk5j0fpg6z302plra"
    secret_key = "h4m186hey5c2648slx23kzmfic1d8s"

    # client_id =
    # secret_key =

    class Config:
        env_prefix = _CONFIG_PREFIX + 'TWITCH_'
        env_file = '.env'
        env_file_encoding = 'utf-8'


class Config(BaseSettings):
    service: Service = Service()
    mongodb: MongoDB = MongoDB()
    kafka: Kafka = Kafka()
    lamoda_url: LamodaUrl = LamodaUrl()
    twitch: Twitch = Twitch()

    class Config:
        env_prefix = _CONFIG_PREFIX
        env_file = '.env'
        env_file_encoding = 'utf-8'
