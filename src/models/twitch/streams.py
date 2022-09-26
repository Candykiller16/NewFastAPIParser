from typing import Optional, List

from pydantic import BaseModel, Field, validator

from src.models.validators.object_id_to_string import object_id_to_string


class Streams(BaseModel):
    id: str = Field(..., alias="_id")
    game_name: str = Field(...)
    language: str = Field(...)
    started_at: str = Field(...)
    title: str = Field(...)
    user_login: str = Field(...)
    user_name: str = Field(...)
    viewer_count: int = Field(...)
    type: str = Field(...)

    @validator('id', pre=True)
    def validate_id(cls, v) -> str:
        return object_id_to_string(v)

    class Config:
        schema_extra = {
            'example': {
                'id': '62f264f7705d3742932262ec',
                'game_name': 'Counter-Strike: Global Offensive',
                'language': 'en',
                'started_at': '2022-09-21T09:33:06Z',
                'title': 'LIVE: Eternal Fire vs FURIA Esports - ESL Pro League Season 16 - '
                         'Group D',
                'type': 'live',
                'user_login': 'esl_csgo',
                'user_name': 'ESL_CSGO',
                'viewer_count': 63855}
        }


class StreamsResponse(BaseModel):
    streams: List[Streams]


class StreamsCreateUpdate(BaseModel):

    game_name: Optional[str]
    language: Optional[str]
    started_at: Optional[str]
    title: Optional[str]
    user_login: Optional[str]
    user_name: Optional[str]
    viewer_count: Optional[int]
    type: Optional[str]

    class Config:
        schema_extra = {
            'example': {
                'game_name': 'Elden Ring',
                'language': 'en',
                "started_at": "2022-09-23T08:19:30Z",
                'title': 'I sucked and I was fucked',
                'type': 'live',
                'user_login': 'general_radan',
                'user_name': 'MARIKA_IS_WAIFU',
                'viewer_count': 169878
            }
        }
