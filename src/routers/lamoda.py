from typing import List

from fastapi import APIRouter

from src.di import container_controller
from src.models.lamoda.sneakers import Sneakers

router = APIRouter(
    tags=['Lamoda router'],
    prefix='/lamoda'
)


@router.get('/get-list', response_model=List[Sneakers])
def get_sneakers_list() -> List[Sneakers]:
    return container_controller.lamoda.get_list()
