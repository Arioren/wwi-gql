from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .country import Country
from .target import Target
from .target_style import TargetStyle
from .cities import City
from .mission import Mission
