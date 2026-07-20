from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db

from api.services.training_database_service import (
    get_training_sessions_by_athlete,
)

from api.services.performance_engine import analyse_training
from api.services.coach_reasoning import generate_coach_reasoning

from schemas.analysis import PerformanceAnalysis

router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"],
)


@router.get(
    "/{athlete_id}",
    response_model=PerformanceAnalysis,
)
def analyse_athlete(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    sessions = get_training_sessions_by_athlete(
        db,
        athlete_id,
    )

    if not sessions:
        raise HTTPException(
            status_code=404,
            detail="No training sessions found.",
        )

    analysis = analyse_training(sessions)

    reasoning = generate_coach_reasoning(analysis)

    analysis.coach_comment = reasoning["coach_comment"]
    analysis.strengths = reasoning["strengths"]
    analysis.risks = reasoning["risks"]
    analysis.recommendations = reasoning["recommendations"]

    return analysis