from fastapi import FastAPI, HTTPException
from models import User, Gender, Role
from uuid import UUID
from typing import List

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

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
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
