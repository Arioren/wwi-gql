from graphene import ObjectType, Field, Int, List

from app.db.database import session_maker
from app.db.model import Mission
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
# .3 מציאת משימה לפי מדינה שלקחו בו חלק: מקבלים רשימה של פרטי כל
# המשימות המתאימות
# .4 מציאת משימה לפי תעשיית מטרה )Industry Target): מקבלים רשימה של
# פרטי כל המשימות התואמות
# .5 מציאת כלי טיס לפי משימה: מקבלים רשימה של כלי טיס מתאימים