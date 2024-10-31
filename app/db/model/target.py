from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.db.model import Base


class Target(Base):
   __tablename__ = "targets"
   target_id = Column(Integer, primary_key=True, autoincrement=True)
   mission_id = Column(Integer, ForeignKey('missions.id'))
   target_industry = Column(String)
   city_id = Column(Integer, ForeignKey('cities.id'))
   target_type_id = Column(Integer, ForeignKey('targettypes.id'))
   target_priority = Column(Integer)

   mission = relationship('Mission', back_populates="targets")
   city = relationship('City', back_populates="targets")
   target_type = relationship('TargetType',  back_populates="targets")


