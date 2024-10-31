from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.db.model import Base


class City(Base):
   __tablename__ = "cities"
   city_id = Column(Integer, primary_key=True, autoincrement=True)
   city_name = Column(String)
   country_id = Column(Integer, ForeignKey('countries.id'))
   latitude = Column(Float)
   longitude = Column(Float)

   country = relationship("Country", back_populates="cities")
   targets = relationship('Target', back_populates='city')

