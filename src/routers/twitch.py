from typing import List, Dict

from fastapi import APIRouter

from src.di import container_controller
from src.models.twitch.streams import Streams, StreamsResponse, StreamsCreateUpdate

router = APIRouter(
    tags=['Twitch router'],
    prefix='/twitch'
)


@router.get('/get-list', response_model=StreamsResponse, description="Get list of streams")
def get_streams_list() -> List[Streams]:
    return container_controller.twitch.get_streams()


@router.get('/get/{_id}', response_model=Streams, description="Get one stream")
def get_sneaker(_id: str) -> Streams:
    return container_controller.twitch.get_stream_by_id(_id)


@router.post('/create', description="Create one stream")
def create_sneaker(stream: StreamsCreateUpdate) -> Dict[str, str]:
    return container_controller.twitch.create_stream(stream)


@router.put('/update/{_id}', response_model=Streams, description="Update one stream")
def update_sneaker(_id: str, stream: StreamsCreateUpdate):
    return container_controller.twitch.update_stream(_id, stream)


@router.delete('/delete/{_id}', description="Delete one stream")
def delete_sneaker(_id: str):
    return container_controller.twitch.delete_stream(_id)
