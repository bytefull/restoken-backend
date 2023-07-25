from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from models import User, Gender, Role
from uuid import UUID
from typing import List
from models import UserUpdateRequest
from utils import (
    get_hashed_password,
    create_access_token,
    create_refresh_token,
    verify_password
)

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("d76afafa-bb02-4498-9581-d02691728e9b"),
        firstname="Bayrem",
        lastname="Gharsellaoui",
        email="garssallaoui.bayrem@gmail.com",
        username="bayrem",
        password="supersecret",
        gender=Gender.male,
        roles=[Role.student, Role.admin]
    ),
    User(
        id=UUID("11045555-7a83-4ae7-8f27-ec3e3edff67e"),
        firstname="Lorem",
        lastname="Ipsum",
        email="lorem.ipsum@gmail.com",
        username="lorem",
        password="supersecret123",
        gender=Gender.male,
        roles=[Role.student]
    )
]

@app.on_event("startup")
async def on_startup():
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    user.password = get_hashed_password(user.password)
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.firstname is not None:
                user.firstname = user_update.firstname
            if user_update.lastname is not None:
                user.lastname = user_update.lastname
            if user_update.username is not None:
                user.username = user_update.username
            if user_update.password is not None:
                user.password = user_update.password
            if user_update.gender is not None:
                user.gender = user_update.gender
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )

@app.post('/api/v1/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # user = db.get(form_data.username, None)
    user = None

    for user_to_find in db:
        if user_to_find.username == form_data.username:
            user = user_to_find
            break

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    hashed_pass = user.password
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    
    return {
        "access_token": create_access_token(user.email),
        "refresh_token": create_refresh_token(user.email),
    }