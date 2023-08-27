import uuid
from datetime import datetime

from pydantic import BaseModel


class OrderBase(BaseModel):
    amount: int
    restaurant_id: int


class OrderCreateRequest(OrderBase):
    pass


class OrderUpdateRequest(BaseModel):
    pass


class OrderCreateResponse(OrderBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
