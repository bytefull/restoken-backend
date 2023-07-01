from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel, EmailStr
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    student = "student"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    firstname: str
    lastname: str
    email: EmailStr
    username: str
    password: str
    gender: Gender
    roles: List[Role]
