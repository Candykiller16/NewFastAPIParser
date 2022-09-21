from typing import List, Dict

from fastapi import APIRouter

from src.di import container_controller
from src.models.twitch.streams import Streams, StreamsCreateUpdate, StreamsResponse

router = APIRouter(
    tags=['Twitch router'],
    prefix='/twitch'
)


@router.get('/get-list', response_model=StreamsResponse, description="Get list of streams")
def get_streams_list() -> List[Streams]:
    return container_controller.twitch.get_streams()

