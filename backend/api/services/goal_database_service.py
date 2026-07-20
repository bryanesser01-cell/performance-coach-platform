from sqlalchemy.orm import Session

from database.models import Goal


def create_goal(db: Session, goal_data):

    goal = Goal(
        athlete_id=goal_data.athlete_id,
        goal_type=goal_data.goal_type,
        target_value=goal_data.target_value,
        target_unit=goal_data.target_unit,
        current_value=goal_data.current_value,
        status=goal_data.status,
    )

    db.add(goal)
    db.commit()
    db.refresh(goal)

    return goal


def get_all_goals(db: Session):
    return db.query(Goal).all()