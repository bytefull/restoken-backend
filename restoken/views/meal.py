from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

import restoken.schemas.meal as schemas
import restoken.crud.meal as crud
from restoken.database import get_db


meal_router = APIRouter()


@meal_router.post("", response_model=schemas.Meal)
def create_meal(meal: schemas.MealCreate, db: Session = Depends(get_db)):
    return crud.create_meal(db=db, meal=meal)


@meal_router.get("", response_model=list[schemas.Meal])
def read_meals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    meals = crud.get_all_meals(db, skip=skip, limit=limit)
    return meals


@meal_router.get("/{meal_id}", response_model=schemas.Meal)
def read_meal(meal_id: int, db: Session = Depends(get_db)):
    db_meal = crud.get_meal_by_id(db, meal_id=meal_id)
    if db_meal is None:
        raise HTTPException(status_code=404, detail="Meal not found")
    return db_meal


@meal_router.delete("", response_model=list[schemas.Meal])
def delete_meals(db: Session = Depends(get_db)):
    meals = crud.delete_all_meals(db)
    return meals


@meal_router.delete("/{meal_id}")
def delete_meal(meal_id: int, db: Session = Depends(get_db)):
    db_meal = crud.get_meal_by_id(db, meal_id=meal_id)
    if db_meal is None:
        raise HTTPException(status_code=404, detail="Meal not found")
    crud.delete_meal(db, meal_id=meal_id)
    return {"delete": meal_id}


# TODO: Add update meal
@meal_router.put("/{meal_id}")
def update_meal(meal_id: int, db: Session = Depends(get_db)):
    return {"message": "not implemented yet"}
