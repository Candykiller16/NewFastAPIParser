from json import dumps, loads
from typing import List, Dict

from fastapi import APIRouter
from kafka import KafkaProducer, KafkaConsumer

from src.di import container_controller, container_parser
from src.models.twitch.streams import Streams, StreamsCreateUpdate, StreamsResponse

router = APIRouter(
    tags=['Twitch router'],
    prefix='/twitch'
)


@router.get('/get-list', response_model=StreamsResponse, description="Get list of streams")
def get_streams_list() -> List[Streams]:
    return container_controller.twitch.get_streams()

