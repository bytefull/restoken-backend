import uuid
from datetime import timedelta

from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED

import restoken.schemas.user as user_schema
import restoken.schemas.order as order_schema
import restoken.schemas.token as token_schema
import restoken.models.user as models
import restoken.crud.user as user_crud
import restoken.crud.order as order_crud
from restoken.database import get_db
from restoken.crud.user import get_current_user
from restoken.utils.security import authenticate_user, create_access_token
from restoken.utils.config import ACCESS_TOKEN_EXPIRE_MINUTES


user_router = APIRouter()


@user_router.post("", response_model=user_schema.User)
def create_user(
    user: user_schema.UserCreate,
    db: Session = Depends(get_db),
):
    db_user = user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create_user(db=db, user=user)


@user_router.get("", response_model=list[user_schema.User])
def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    user_data: models.User = Depends(get_current_user),
):
    users = user_crud.get_all_users(db, skip=skip, limit=limit)
    return users


@user_router.get("/me", response_model=user_schema.User)
def get_current_user(user_data: models.User = Depends(get_current_user)):
    return user_data


@user_router.get("/{user_id}", response_model=user_schema.User)
def read_user(
    user_id: uuid.UUID,
    db: Session = Depends(get_db),
    user_data: models.User = Depends(get_current_user),
):
    db_user = user_crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@user_router.put("/{user_id}", response_model=user_schema.User)
def update_user(
    user_id: uuid.UUID,
    user: user_schema.UserUpdate,
    db: Session = Depends(get_db),
    user_data: models.User = Depends(get_current_user),
):
    user_crud.update_user(db, user_id=user_id, user=user)
    user = user_crud.get_user_by_id(db, user_id=user_id)
    return user


@user_router.delete("", response_model=list[user_schema.User])
def delete_users(
    db: Session = Depends(get_db), user_data: models.User = Depends(get_current_user)
):
    users = user_crud.delete_all_users(db)
    return users


@user_router.delete("/{user_id}")
def delete_user(
    user_id: uuid.UUID,
    db: Session = Depends(get_db),
    user_data: models.User = Depends(get_current_user),
):
    db_user = user_crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_crud.delete_user(db, user_id=user_id)
    return {"delete": user_id}


@user_router.post("/login", response_model=token_schema.TokenSchema)
def login_for_access_token(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    user_data = authenticate_user(db, form_data.username, form_data.password)
    if not user_data:
        raise HTTPException(
            HTTP_401_UNAUTHORIZED,
            detail="invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token_expires_date = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user_data.email},
        expires_delta=token_expires_date,
    )
    return {"access_token": access_token, "token_type": "bearer"}


@user_router.post("/{user_id}/orders", response_model=order_schema.OrderCreateResponse)
def create_user_order(
    user_id: uuid.UUID,
    order: order_schema.OrderCreateRequest,
    db: Session = Depends(get_db),
    user_data: models.User = Depends(get_current_user),
):
    return order_crud.create_user_order(db=db, order=order, user_id=user_id)


@user_router.get("/{user_id}/orders", response_model=list[order_schema.OrderCreateResponse])
def read_user_orders(
    user_id: uuid.UUID,
    db: Session = Depends(get_db),
    user_data: models.User = Depends(get_current_user),
):
    orders = order_crud.get_user_orders(db, user_id=user_id)
    return orders
