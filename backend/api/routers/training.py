from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.services.training_service import (
    create_training,
    list_training,
    list_training_by_athlete,
)
from database.database import get_db
from schemas.training import (
    TrainingSessionCreate,
    TrainingSessionResponse,
)

router = APIRouter(
    prefix="/training",
    tags=["Training"],
)


@router.post(
    "",
    response_model=TrainingSessionResponse,
)
def add_training_session(
    training: TrainingSessionCreate,
    db: Session = Depends(get_db),
):
    return create_training(
        db,
        training,
    )


@router.get(
    "",
    response_model=list[TrainingSessionResponse],
)
def get_training_sessions(
    db: Session = Depends(get_db),
):
    return list_training(db)


@router.get(
    "/{athlete_id}",
    response_model=list[TrainingSessionResponse],
)
def get_training_sessions_by_athlete(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    return list_training_by_athlete(
        db,
        athlete_id,
    )
