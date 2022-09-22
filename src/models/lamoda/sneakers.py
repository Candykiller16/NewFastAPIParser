from typing import Optional, List

from pydantic import BaseModel, Field, validator

from src.models.validators.object_id_to_string import object_id_to_string


class Sneakers(BaseModel):
    id: str = Field(..., alias="_id")
    brand: str = Field(...)
    name: str = Field(...)
    price: str = Field(...)

    @validator('id', pre=True)
    def validate_id(cls, v) -> str:
        return object_id_to_string(v)

    class Config:
        schema_extra = {
            'example': {
                'id': '631f2241872934bd5f762efe',
                'brand': 'Geox',
                'name': 'Кроссовки',
                'price': '399.00'
            }
        }


class SneakersResponse(BaseModel):
    sneakers: List[Sneakers]


class SneakersCreateUpdate(BaseModel):
    brand: Optional[str]
    name: Optional[str]
    price: Optional[str]

    class Config:
        schema_extra = {
            'example': {
                'brand': 'Кроссовки Pacer Next SB WTR',
                'name': 'PUMA',
                'price': '349.00'
            }
        }
