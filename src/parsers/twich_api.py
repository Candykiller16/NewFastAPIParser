import requests
from src.di.container_general import ContainerGeneral


class TwitchParser:
    def __init__(self, container_general: ContainerGeneral):
        self.streams = container_general.config.twitch.streams
        self.client_id = container_general.config.twitch.client_id
        self.client_secret = container_general.config.twitch.secret_key
        self.auth_url = container_general.config.twitch.auth_url

    def get_data_from_twich_api(self):
        response = requests.post(
            f"{self.auth_url}"
            f"?client_id={self.client_id}"
            f"&client_secret={self.client_secret}"
            f"&grant_type=client_credentials"
        )

        data = requests.get(
            self.streams,
            headers={
                "Authorization": f'Bearer {response.json()["access_token"]}',
                "Client-Id": self.client_id,
            },
        )
        list_of_stream_data = []
        for stream in data.json()["data"]:
            data_from_stream = {
                "game_name": stream["game_name"],
                "language": stream["language"],
                "started_at": stream["started_at"],
                "title": stream["title"],
                "type": stream["type"],
                "user_login": stream["user_login"],
                "user_name": stream["user_name"],
                "viewer_count": stream["viewer_count"],
            }
            list_of_stream_data.append(data_from_stream)
        return list_of_stream_data

    # async def parse(self):
    #
    #     data = self.get_data_from_twich_api()
    #     for stream in data:
    #         self.kafka.producer.send("topic_twitch", value=stream)
    #         print(f"send {stream}")
    #
    #     await self.mongo.insert_streams(self.kafka.consumer_twitch)
