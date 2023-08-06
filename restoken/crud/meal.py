from sqlalchemy.orm import Session

import restoken.schemas.meal as schemas
import restoken.models.meal as models


def get_all_meals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Meal).offset(skip).limit(limit).all()


def get_meal_by_id(db: Session, meal_id: int):
    return db.query(models.Meal).filter(models.Meal.id == meal_id).first()


def create_meal(db: Session, meal: schemas.MealCreate):
    db_meal = models.Meal(**meal.model_dump())
    db.add(db_meal)
    db.commit()
    db.refresh(db_meal)
    return db_meal


def delete_all_meals(db: Session):
    db.query(models.Meal).delete()
    db.commit()
    meals: list[schemas.Meal] = []
    return meals


def delete_meal(db: Session, meal_id: int):
    meal = db.query(models.Meal).filter(models.Meal.id == meal_id).first()
    db.delete(meal)
    db.commit()
