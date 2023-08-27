from sqlalchemy.orm import Session

import restoken.schemas.restaurant as schemas
import restoken.models.restaurant as models


def get_all_restaurants(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Restaurant).offset(skip).limit(limit).all()


def get_restaurant_by_id(db: Session, restaurant_id: int):
    return (
        db.query(models.Restaurant)
        .filter(models.Restaurant.id == restaurant_id)
        .first()
    )


def create_restaurant(db: Session, restaurant: schemas.RestaurantCreateRequest):
    db_restaurant = models.Restaurant(**restaurant.model_dump())
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant


def delete_all_restaurants(db: Session):
    db.query(models.Restaurant).delete()
    db.commit()
    restaurants: list[schemas.RestaurantBase] = []
    return restaurants


def delete_restaurant(db: Session, restaurant_id: int):
    restaurant = (
        db.query(models.Restaurant)
        .filter(models.Restaurant.id == restaurant_id)
        .first()
    )
    db.delete(restaurant)
    db.commit()
