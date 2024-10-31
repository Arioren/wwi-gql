from graphene import Mutation, Int, String, Field

from app.db.model import Target
from app.db.repository.target_repo import create_target
from app.gql.types.target_type import TargetType


class AddTarget(Mutation):
    class Arguments:
        mission_id = Int()
        target_industry = String()
        city_id = Int()
        target_type_id =  Int()
        target_priority =  Int()

    target = Field(TargetType)

    @staticmethod
    def mutate(root, info, mission_id, target_industry
               , city_id, target_type_id, target_priority):
        return AddTarget(target=create_target(Target(mission_id=mission_id, target_industry=target_industry, city_id=city_id,
                         target_type_id=target_type_id, target_priority=target_priority)))




