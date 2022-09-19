from typing import List, Dict

from fastapi import APIRouter

from src.di import container_controller
from src.models.lamoda.sneakers import Sneakers, SneakersCreateUpdate, SneakersResponse

router = APIRouter(
    tags=['Lamoda router'],
    prefix='/lamoda'
)


@router.get('/get-list', response_model=SneakersResponse, description="Get list of sneakers")
def get_sneakers_list() -> List[Sneakers]:
    return container_controller.lamoda.get_list()


@router.get('/get/{_id}', response_model=Sneakers, description="Get one sneaker")
def get_sneaker(_id: str) -> Sneakers:
    return container_controller.lamoda.get(_id)


@router.post('/create', description="Create one sneaker")
def create_product(sneaker: SneakersCreateUpdate) -> Dict[str, str]:
    return container_controller.lamoda.create(sneaker)
