from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

import restoken.schemas.restaurant as schemas
import restoken.crud.restaurant as crud
from restoken.database import get_db


restaurant_router = APIRouter()


@restaurant_router.post("", response_model=schemas.Restaurant)
def create_restaurant(
    restaurant: schemas.RestaurantCreate, db: Session = Depends(get_db)
):
    return crud.create_restaurant(db=db, restaurant=restaurant)


@restaurant_router.get("", response_model=list[schemas.Restaurant])
def read_restaurants(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    restaurants = crud.get_all_restaurants(db, skip=skip, limit=limit)
    return restaurants


@restaurant_router.get("/{restaurant_id}", response_model=schemas.Restaurant)
def read_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    db_restaurant = crud.get_restaurant_by_id(db, restaurant_id=restaurant_id)
    if db_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return db_restaurant


@restaurant_router.delete("", response_model=list[schemas.Restaurant])
def delete_restaurants(db: Session = Depends(get_db)):
    restaurants = crud.delete_all_restaurants(db)
    return restaurants


@restaurant_router.delete("/{restaurant_id}")
def delete_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    db_restaurant = crud.get_restaurant_by_id(db, restaurant_id=restaurant_id)
    if db_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    crud.delete_restaurant(db, restaurant_id=restaurant_id)
    return {"delete": restaurant_id}


# TODO: Add update restaurant
@restaurant_router.put("/{restaurant_id}")
def update_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    return {"message": "not implemented yet"}
