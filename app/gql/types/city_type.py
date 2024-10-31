from graphene import ObjectType, Int, String, Float, List, Field

from app.db.database import session_maker
from app.db.model import Country, Target


class CityType(ObjectType):
    city_id = Int()
    city_name = String()
    country_id = Int()
    latitude = Float()
    longitude = Float()

    country = Field('app.gql.types.country_type.CountryType')
    targets = List('app.gql.types.target_type.TargetType')

    @staticmethod
    def resolve_country(root, info):
        with session_maker() as session:
            return (
                session.query(Country)
                .filter(Country.country_id == root.country_id)
                .first()
            )

    @staticmethod
    def resolve_targets(root, info):
        with session_maker() as session:
            return (
                session.query(Target)
                .filter(Target.city_id == root.city_id)
                .all()
            )


