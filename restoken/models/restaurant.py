from sqlalchemy import Column, ForeignKey, Integer, String, UUID
from sqlalchemy.orm import relationship

from restoken.database import Base


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    # Establish the relationship: Restaurant to User (many-to-one)
    # Many restaurants can be associated with one user (owner)
    user = relationship("User", back_populates="restaurants")

    # Establish the relationship: Restaurant to Orders (one-to-many)
    # A restaurant can have many orders
    orders = relationship("Order", back_populates="restaurant")
