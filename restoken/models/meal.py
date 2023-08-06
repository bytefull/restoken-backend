from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from restoken.database import Base


class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    image_url = Column(String)

    # Define the one-to-many relationship from Meal to Order
    orders = relationship("Order", back_populates="meal")
