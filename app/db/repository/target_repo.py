from sqlalchemy import desc

from app.db.database import session_maker
from app.db.model import Target


def create_target(target:Target):
    with session_maker() as session:
        target_id = session.query(Target).order_by(desc(Target.target_id)).first().target_id + 1
        target.target_id = target_id
        session.add(target)
        session.commit()
        session.refresh(target)
        return target