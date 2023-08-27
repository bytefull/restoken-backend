import uuid

from pydantic import BaseModel


class PaymentBase(BaseModel):
    pass


class PaymentResult(PaymentBase):
    status: str


class PaymentCreate(PaymentBase):
    customer_id: uuid.UUID
    restaurant_id: int
    amount: int
    timestamp: int


class Payment(PaymentCreate):
    pass

    class Config:
        from_attributes = True
