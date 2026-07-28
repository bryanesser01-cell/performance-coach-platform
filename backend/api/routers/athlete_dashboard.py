from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.services.athlete_dashboard_service import (
    generate_fitness_summary,
    generate_prediction,
    generate_race_readiness,
    generate_training_status,
)
from database.session import get_db

router = APIRouter(
    prefix="/athletes",
    tags=["Athlete Dashboard"],
)


@router.get("/{athlete_id}/fitness-summary")
def get_fitness_summary(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    return generate_fitness_summary(
        db,
        athlete_id,
    )


@router.get("/{athlete_id}/training-status")
def get_training_status(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    return generate_training_status(
        db,
        athlete_id,
    )


@router.get("/{athlete_id}/race-readiness")
def get_race_readiness(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    return generate_race_readiness(
        db,
        athlete_id,
    )


@router.get("/{athlete_id}/prediction")
def get_prediction(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    return generate_prediction(
        db,
        athlete_id,
    )
