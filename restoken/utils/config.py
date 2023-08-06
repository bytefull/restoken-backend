import os

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 15))
ALGORITHM = os.environ.get("ALGORITHM", "HS256")
SECRET_KEY = os.environ.get(
    "SECRET_KEY", "97b2ae585c5fe999a5b01def058c20b6498535785403bcf92f6896f5b1ab2d60"
)
SQLALCHEMY_DATABASE_URL = os.environ.get(
    "SQLALCHEMY_DATABASE_URL", "postgresql://postgres:postgres@127.0.0.1/resto"
)
