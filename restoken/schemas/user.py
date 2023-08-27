import uuid
from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str
    role: str


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    id: Optional[uuid.UUID] = None
    email: Optional[str] = None
    username: Optional[str] = None
    role: Optional[str] = None
    balance: Optional[int] = None
    password: Optional[str] = None


class User(UserBase):
    id: uuid.UUID
    balance: int

    class Config:
        from_attributes = True
