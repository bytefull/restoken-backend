import uuid

from sqlalchemy.orm import Session

import restoken.schemas.order as schemas
import restoken.models.order as models


def get_all_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Order).offset(skip).limit(limit).all()


def get_order_by_id(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()


def get_user_orders(db: Session, user_id: uuid.UUID):
    return db.query(models.Order).filter(models.Order.customer_id == user_id).all()


def create_user_order(db: Session, order: schemas.OrderCreate, user_id: uuid.UUID):
    db_order = models.Order(**order.model_dump(), customer_id=user_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def delete_all_orders(db: Session):
    db.query(models.Order).delete()
    db.commit()
    orders: list[schemas.Order] = []
    return orders


def delete_order(db: Session, order_id: int):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    db.delete(order)
    db.commit()
