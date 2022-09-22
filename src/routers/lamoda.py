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
    return container_controller.lamoda.get_sneakers()


@router.get('/get/{_id}', response_model=Sneakers, description="Get one sneaker")
def get_sneaker(_id: str) -> Sneakers:
    return container_controller.lamoda.get_sneaker_by_id(_id)


@router.post('/create', description="Create one sneaker")
def create_sneaker(sneaker: SneakersCreateUpdate) -> Dict[str, str]:
    return container_controller.lamoda.create_sneaker(sneaker)


@router.put('/update/{_id}', response_model=Sneakers, description="Update one sneaker")
def update_sneaker(_id: str, sneaker: SneakersCreateUpdate):
    return container_controller.lamoda.update_sneaker(_id, sneaker)


@router.delete('/delete/{_id}', description="Delete one sneaker")
def delete_sneaker(_id: str):
    return container_controller.lamoda.delete_sneaker(_id)