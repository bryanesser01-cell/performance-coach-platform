from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.services.goal_service import (
    create_goal_service,
    get_goal_progress_service,
    list_goals,
)
from database.session import get_db
from schemas.goal import GoalCreate

router = APIRouter(
    prefix="/goals",
    tags=["Goals"],
)


@router.get("")
def get_goals(
    db: Session = Depends(get_db),
):
    return list_goals(db)


@router.post("")
def add_goal(
    goal: GoalCreate,
    db: Session = Depends(get_db),
):
    return create_goal_service(
        db,
        goal,
    )


@router.get("/{athlete_id}/progress")
def get_goal_progress(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    return get_goal_progress_service(
        db,
        athlete_id,
    )
