from sqlalchemy import Column, ForeignKey, Integer, TIMESTAMP, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from restoken.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    customer_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))

    # Establish the relationship: Order to User (many-to-one)
    # Many orders can be made by one user (either owner or customer)
    user = relationship("User", back_populates="orders")

    # Establish the relationship: Order to Restaurant (many-to-one)
    # Many orders can be made in one restaurant
    restaurant = relationship("Restaurant", back_populates="orders")
