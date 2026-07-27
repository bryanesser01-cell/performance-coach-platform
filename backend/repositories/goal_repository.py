from sqlalchemy.orm import Session

from database.models import Goal
from schemas.goal import GoalCreate


class GoalRepository:
    """
    Repository responsible for Goal database operations.
    """

    def __init__(self, db: Session):
        self.db = db

    def create(self, goal: GoalCreate) -> Goal:
        db_goal = Goal(**goal.model_dump())

        self.db.add(db_goal)
        self.db.commit()
        self.db.refresh(db_goal)

        return db_goal

    def get_all(self) -> list[Goal]:
        return self.db.query(Goal).order_by(Goal.id).all()
