from pydantic import BaseModel


class MealBase(BaseModel):
    name: str


class MealCreate(MealBase):
    description: str
    image_url: str


class Meal(MealCreate):
    id: int

    class Config:
        from_attributes = True
