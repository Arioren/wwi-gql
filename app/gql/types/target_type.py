import graphene
from graphene import ObjectType, Int, String, Field

from app.db.database import session_maker
from app.db.model import Mission, City, TargetStyle


class TargetType(ObjectType):
    target_id = Int()
    mission_id = Int()
    target_industry = String()
    city_id = Int()
    target_type_id = Int()
    target_priority = Int()

    mission = Field('app.gql.types.mission_type.MissionType')
    city = Field('app.gql.types.city_type.CityType')
    target_style = Field('app.gql.types.target_style_type.TargetStyleType')

    @staticmethod
    def resolve_mission(root, info):
        with session_maker() as session:
            return (
                session.query(Mission)
                .filter(Mission.mission_id == root.mission_id)
                .first()
            )

    @staticmethod
    def resolve_city(root, info):
        with session_maker() as session:
            return (
                session.query(City)
                .filter(City.city_id == root.city_id)
                .all()
            )

    @staticmethod
    def resolve_target_style(root, info):
        with session_maker() as session:
            return (
                session.query(TargetStyle)
                .filter(TargetStyle.target_type_id == root.target_type_id)
                .first()
            )



