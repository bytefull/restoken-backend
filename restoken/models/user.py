import uuid

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from restoken.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4
    )
    email = Column(String, unique=True, index=True)
    username = Column(String)
    hashed_password = Column(String)
    role = Column(String)
    balance = Column(Integer)

    # Establish the relationship: User to Restaurants (one-to-many)
    # A user (owner) can have many restaurants
    restaurants = relationship("Restaurant", back_populates="user")

    # Establish the relationship: User to Orders (one-to-many)
    # A user (either owner or customer) can have many orders
    orders = relationship("Order", back_populates="user")
