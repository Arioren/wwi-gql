from graphene import Mutation, Int, Date, Float, Field

from app.db.database import session_maker
from app.db.model import Mission
from app.gql.types.mission_type import MissionType


class AddMission(Mutation):
    class Arguments:
        mission_date = Date()
        airborne_aircraft = Float()
        attacking_aircraft = Float()
        bombing_aircraft =  Float()
        aircraft_returned =  Float()
        aircraft_failed =  Float()
        aircraft_damaged =  Float()
        aircraft_lost =  Float()


    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_date, airborne_aircraft
               , attacking_aircraft, bombing_aircraft, aircraft_returned,
               aircraft_failed, aircraft_damaged, aircraft_lost):
        with session_maker() as session:
            res_mission = Mission(mission_date=mission_date, airborne_aircraft=airborne_aircraft, attacking_aircraft=attacking_aircraft,
                        bombing_aircraft=bombing_aircraft, aircraft_returned=aircraft_returned,
                        aircraft_failed=aircraft_failed, aircraft_damaged=aircraft_damaged, aircraft_lost=aircraft_lost)
            session.add(res_mission)
            session.commit()
            session.refresh(res_mission)
            return AddMission(mission=res_mission)




