from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.services.goal_service import (
    create_goal_service,
    list_goals,
)
from database.database import get_db
from schemas.goal import GoalCreate

router = APIRouter()


@router.get("/goals")
def get_goals(
    db: Session = Depends(get_db),
):
    return list_goals(db)


@router.post("/goals")
def add_goal(
    goal: GoalCreate,
    db: Session = Depends(get_db),
):
    return create_goal_service(
        db,
        goal,
    )
