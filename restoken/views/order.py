import uuid

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

import restoken.schemas.order as schemas
import restoken.models.user as models
import restoken.crud.order as crud
from restoken.database import get_db
from restoken.crud.user import get_current_user


order_router = APIRouter()


@order_router.get("", response_model=list[schemas.OrderCreateResponse])
def read_orders(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    user_data: models.User = Depends(get_current_user),
):
    orders = crud.get_all_orders(db, skip=skip, limit=limit)
    return orders


@order_router.delete("", response_model=list[schemas.OrderBase])
def delete_orders(
    db: Session = Depends(get_db), user_data: models.User = Depends(get_current_user)
):
    orders = crud.delete_all_orders(db)
    return orders

@order_router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order_by_id(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    crud.delete_order(db, order_id=order_id)
    return {"delete": order_id}

