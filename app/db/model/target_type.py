from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.model import Base


class TargetType(Base):
    target_type_id = Column(Integer, primary_key=True, autoincrement=True)
    target_type_name = Column(String)

    targets = relationship('Target', back_populates='target_type')