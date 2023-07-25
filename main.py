from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    # Not needed if you setup a migration system like Alembic
    print('call await create_db_and_tables() here')

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def fetch_users():
    return []
