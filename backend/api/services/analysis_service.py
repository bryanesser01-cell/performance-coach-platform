from fastapi import HTTPException
from sqlalchemy.orm import Session

from api.services.coach_reasoning import generate_coach_reasoning
from api.services.performance_engine import analyse_training
from repositories.training_repository import TrainingRepository
from schemas.analysis import PerformanceAnalysis


def analyse_athlete_service(
    db: Session,
    athlete_id: int,
) -> PerformanceAnalysis:

    training_repository = TrainingRepository(db)

    sessions = training_repository.get_by_athlete(athlete_id)

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
