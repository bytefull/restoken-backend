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
    meal_id = Column(Integer, ForeignKey("meals.id"))

    customer = relationship("User", back_populates="orders")
    # Define the many-to-one relationship from Order to Meal
    meal = relationship("Meal", back_populates="orders")
