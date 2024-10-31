from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.model import Base


class Country(Base):
    __tablename__ = 'countries'
    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String)

    cities = relationship("City", back_populates="country")

