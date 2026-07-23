from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from api.dependencies.auth import get_current_user
from api.services.athlete_service import AthleteService
from database.database import get_db
from database.user_models import User
from schemas.athlete_schema import (
    AthleteCreate,
    AthleteResponse,
    AthleteUpdate,
)

router = APIRouter(
    prefix="/athletes",
    tags=["Athletes"],
)


@router.post(
    "",
    response_model=AthleteResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_athlete(
    athlete: AthleteCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    service = AthleteService(db)
    return service.create(current_user, athlete)


@router.get(
    "",
    response_model=list[AthleteResponse],
)
def get_athletes(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    service = AthleteService(db)
    return service.get_all(current_user)


@router.get(
    "/{athlete_id}",
    response_model=AthleteResponse,
)
def get_athlete(
    athlete_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    service = AthleteService(db)
    return service.get(current_user, athlete_id)


@router.put(
    "/{athlete_id}",
    response_model=AthleteResponse,
)
def update_athlete(
    athlete_id: int,
    athlete: AthleteUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    service = AthleteService(db)
    return service.update(current_user, athlete_id, athlete)


@router.delete(
    "/{athlete_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_athlete(
    athlete_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    service = AthleteService(db)
    service.delete(current_user, athlete_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)