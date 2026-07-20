from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas.goal import GoalCreate

from api.services.goal_database_service import (
    create_goal,
    get_all_goals,
)

from api.services.goal_analysis import analyse_goal
from api.services.database_service import get_athlete_by_id
from api.services.training_database_service import (
    get_training_sessions_by_athlete,
)

from database.database import get_db

router = APIRouter()


@router.get("/goals")
def list_goals(
    db: Session = Depends(get_db)
):
    return get_all_goals(db)


@router.post("/goals")
def add_goal(
    goal: GoalCreate,
    db: Session = Depends(get_db)
):
    # Save the goal
    saved_goal = create_goal(db, goal)

    # Retrieve the athlete
    athlete = get_athlete_by_id(db, goal.athlete_id)

    if athlete is None:
        raise HTTPException(
            status_code=404,
            detail="Athlete not found."
        )

    # Get the athlete's training sessions
    sessions = get_training_sessions_by_athlete(
        db,
        athlete.id,
    )

    # Analyse the goal
    analysis = analyse_goal(
        saved_goal,
        athlete,
        sessions,
    )

    return {
        "goal": saved_goal,
        "analysis": analysis,
    }