import uuid

from typing import Optional
from pydantic import BaseModel


class RestaurantBase(BaseModel):
    name: str
    location: str
    owner_id: uuid.UUID


class RestaurantCreateRequest(RestaurantBase):
    pass


class RestaurantUpdateRequest(RestaurantBase):
    id: Optional[int] = None
    name: Optional[str] = None
    location: Optional[str] = None


class RestaurantCreateResponse(RestaurantBase):
    class Config:
        from_attributes = True
