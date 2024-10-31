from graphene import Mutation, Int, String, Field

from app.db.database import session_maker
from app.db.model import Target
from app.gql.types.target_type import TargetType


class AddTarget(Mutation):
    class Arguments:
        target_id = Int()
        mission_id = Int()
        target_industry = String()
        city_id = Int()
        target_type_id =  Int()
        target_priority =  Int()

    target = Field(TargetType)

    @staticmethod
    def mutate(root, info, target_id, mission_id, target_industry
               , city_id, target_type_id, target_priority,
               aircraft_failed, aircraft_damaged, aircraft_lost):
        with session_maker() as session:
            res_target = Target(target_id=target_id, mission_id=mission_id, target_industry=target_industry, city_id=city_id,
                        target_type_id=target_type_id, target_priority=target_priority)
            session.add(res_target)
            session.commit()
            session.refresh(res_target)
            return AddTarget(target=res_target)



