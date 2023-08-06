import uuid
from typing import Optional
from pydantic import BaseModel

from restoken.schemas.order import Order


class UserBase(BaseModel):
    email: str
    username: str
    is_admin: bool = False


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    id: Optional[uuid.UUID] = None
    email: Optional[str] = None
    username: Optional[str] = None
    is_admin: Optional[bool] = None
    balance: Optional[int] = None
    password: Optional[str] = None
    orders: Optional[list[Order]] = None


class User(UserBase):
    id: uuid.UUID
    balance: int
    orders: list[Order] = []

    class Config:
        from_attributes = True
