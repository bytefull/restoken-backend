from pydantic import BaseModel


class RestaurantBase(BaseModel):
    name: str


class RestaurantCreate(RestaurantBase):
    location: str


class Restaurant(RestaurantBase):
    id: int

    class Config:
        from_attributes = True
