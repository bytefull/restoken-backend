from fastapi import FastAPI
from contextlib import asynccontextmanager

from restoken.views.user import user_router
from restoken.views.order import order_router
from restoken.views.restaurant import restaurant_router
from restoken.views.payment import payment_router
from restoken.database import Base, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application starting...")

    print("Create database tables from the SQL Alchemy models")
    Base.metadata.create_all(bind=engine)

    yield

    print("Application shutting down...")


app = FastAPI(openapi_url="/openapi.json", lifespan=lifespan)


@app.get("/")
def root():
    return {"message": "Welcome to restoken API!"}


app.router.prefix = "/api/v1"

app.include_router(user_router, prefix="/users")
app.include_router(order_router, prefix="/orders")
app.include_router(restaurant_router, prefix="/restaurants")
app.include_router(payment_router, prefix="/payment")
