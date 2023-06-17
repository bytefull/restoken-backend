from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Volatile users list to mock database users table
users = []

class User(BaseModel):
    id: int
    username: str
    email: str
    password: str

@app.get("/")
async def root():
    return {"message": "Welcome to resto API"}

@app.get("/users")
async def get_users():
    return users

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return users[user_id - 1]

@app.post("/users")
async def add_user(user: User):
    users.append(user)
    return users[-1]

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    users.pop(user_id - 1)
    return {}
