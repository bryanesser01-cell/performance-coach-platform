from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.services.performance_engine import analyse_training
from database.repositories.training_repository import (
    TrainingRepository,
)
from database.session import get_db

router = APIRouter(
    prefix="/performance",
    tags=["Performance"],
)


@router.get("/{athlete_id}")
def get_performance(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    repository = TrainingRepository(db)

    sessions = repository.get_by_athlete(
        athlete_id,
    )

    analysis = analyse_training(
        sessions,
    )

    return {
        "athlete_id": athlete_id,
        "analysis": analysis,
    }
