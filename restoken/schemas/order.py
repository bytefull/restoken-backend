import uuid
from datetime import datetime

from pydantic import BaseModel


class OrderBase(BaseModel):
    pass


class OrderCreate(OrderBase):
    amount: int
    meal_id: int


class Order(OrderCreate):
    id: int
    customer_id: uuid.UUID
    created_at: datetime

    class Config:
        from_attributes = True
