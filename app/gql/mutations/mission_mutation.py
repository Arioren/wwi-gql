from graphene import Mutation, Int, Date, Float, Field
from sqlalchemy import desc

from app.db.database import session_maker
from app.db.model import Mission, Target
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
            mission_id = session.query(Mission).order_by(desc(Mission.mission_id)).first().mission_id + 1
            res_mission = Mission(mission_id=mission_id, mission_date=mission_date, airborne_aircraft=airborne_aircraft, attacking_aircraft=attacking_aircraft,
                        bombing_aircraft=bombing_aircraft, aircraft_returned=aircraft_returned,
                        aircraft_failed=aircraft_failed, aircraft_damaged=aircraft_damaged, aircraft_lost=aircraft_lost)
            session.add(res_mission)
            session.commit()
            session.refresh(res_mission)
            return AddMission(mission=res_mission)


class UpdateMission(Mutation):
    class Arguments:
        mission_id = Int()
        mission_date = Date()
        airborne_aircraft = Float()
        attacking_aircraft = Float()
        bombing_aircraft = Float()
        aircraft_returned = Float()
        aircraft_failed = Float()
        aircraft_damaged = Float()
        aircraft_lost = Float()

    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_id, mission_date, airborne_aircraft
               , attacking_aircraft, bombing_aircraft, aircraft_returned,
               aircraft_failed, aircraft_damaged, aircraft_lost):
        with session_maker() as session:
            res_mission:Mission = session.query(Mission).filter(Mission.mission_id == mission_id).first()
            if res_mission:
                res_mission.mission_date = mission_date
                res_mission.bombing_aircraft = bombing_aircraft
                res_mission.attacking_aircraft = attacking_aircraft
                res_mission.airborne_aircraft = airborne_aircraft
                res_mission.aircraft_damaged = aircraft_damaged
                res_mission.aircraft_returned = aircraft_returned
                res_mission.aircraft_lost = aircraft_lost
                res_mission.aircraft_failed = aircraft_failed
                session.commit()
                session.refresh(res_mission)
            else:
                raise Exception('mission not found')
            return UpdateMission(mission=res_mission)


class DeleteMission(Mutation):
    class Arguments:
        mission_id = Int()

    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_id):
        with session_maker() as session:
            res_mission:Mission = session.query(Mission).filter(Mission.mission_id == mission_id).first()
            x = res_mission.targets
            if res_mission:
                session.delete(res_mission)
                session.commit()
                return DeleteMission(mission=res_mission)
            else:
                session.rollback()
                raise Exception('mission not found')






