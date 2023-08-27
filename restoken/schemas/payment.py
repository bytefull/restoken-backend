from datetime import datetime

from pydantic import BaseModel


class PaymentBase(BaseModel):
    pass


class PaymentCreate(PaymentBase):
    card_id: int
    amount: int
    created_at: datetime


class Payment(PaymentCreate):
    pass

    class Config:
        from_attributes = True
