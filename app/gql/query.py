from graphene import ObjectType, Field, Int, List, Date, String

from app.db.database import session_maker
from app.db.model import Mission, Target, City, Country, TargetStyle
from app.gql.types.mission_type import MissionType


class Query(ObjectType):
    # 1 מציאת משימה לפי מזהה משימה )ID Mission): מקבלים פרטי משימה מלאה
    missionById = Field(MissionType, mission_id=Int())
    @staticmethod
    def resolve_missionById(root, info, mission_id):
        with session_maker() as session:
            return (
                session.query(Mission)
                .filter(Mission.mission_id == mission_id)
                .first()
            )

    # .2 מציאת משימות לפי טווח תאריכים: מקבלים רשימה של פרטי כל המשימות
    # הרלוונטיות
    missionByDate = List(MissionType, start_date=Date(), end_date=Date())
    @staticmethod
    def resolve_missionByDate(root, info, start_date, end_date):
        with session_maker() as session:
            return(
                session.query(Mission)
                .filter(Mission.mission_date >= start_date,
                        Mission.mission_date <= end_date)
                .all()
            )

    # .3 מציאת משימה לפי מדינה שלקחו בו חלק: מקבלים רשימה של פרטי כל
    # המשימות המתאימות
    missionByCountry = List(MissionType, country_id=Int())
    @staticmethod
    def resolve_missionByCountry(root, info, country_id):
        with session_maker() as session:
            return (
                session.query(Mission)
                .join(Target, Target.mission_id == Mission.mission_id)
                .join(City, Target.city_id == City.city_id)
                .join(Country, City.country_id == Country.country_id)
                .filter(Country.country_id == country_id)
                .all()
            )

    # .4 מציאת משימה לפי תעשיית מטרה )Industry Target): מקבלים רשימה של
    # פרטי כל המשימות התואמות
    missionByIdustryType = List(MissionType, industry_type=String())
    @staticmethod
    def resolve_missionByIdustryType(root, info, industry_type):
        with session_maker() as session:
            return (
                session.query(Mission)
                .join(Target, Target.mission_id == Mission.mission_id)
                .filter(Target.target_industry == industry_type)
                .all()
            )

    # .5 מציאת כלי טיס לפי משימה: מקבלים רשימה של כלי טיס מתאימים
    aircraftByMission = Field(MissionType, mission_id=Int())
    @staticmethod
    def resolve_aircraftByMission(root, info, mission_id):
        # query = select(
        #     Mission.airborne_aircraft,
        #     Mission.bombing_aircraft,
        #     Mission.attacking_aircraft
        # )
        with session_maker() as session:
            return (
                session.query(Mission)
                .filter(Mission.mission_id == mission_id)
                .first()
            )

#     מציאת תוצאות של התקפה לפי סוג ההתקפה
    missionByTargetType = List(MissionType, target_type=Int())
    @staticmethod
    def resolve_missionByTargetType(root, info, target_type):
        with session_maker() as session:
            return(
                session.query(Mission)
                .join(Target, Target.mission_id == Mission.mission_id)
                .join(TargetStyle, TargetStyle.target_type_id == Target.target_type_id)
                .filter(TargetStyle.target_type_id == target_type)
                .all()
            )





