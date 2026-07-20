from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db

from schemas.training import (
    TrainingSessionCreate,
    TrainingSessionResponse,
)

from api.services.training_database_service import (
    create_training_session,
    get_training_sessions,
    get_training_sessions_by_athlete,
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
    return create_training_session(db, training)


@router.get(
    "",
    response_model=list[TrainingSessionResponse],
)
def list_training_sessions(
    db: Session = Depends(get_db),
):
    return get_training_sessions(db)


@router.get(
    "/{athlete_id}",
    response_model=list[TrainingSessionResponse],
)
def list_training_sessions_by_athlete(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    return get_training_sessions_by_athlete(
        db,
        athlete_id,
    )