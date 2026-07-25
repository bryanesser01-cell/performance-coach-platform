from fastapi import APIRouter, Depends, status

from api.dependencies.auth import get_current_user
from api.dependencies.services import get_training_service
from api.services.training_service import TrainingService
from database.user_models import User
from schemas.training import (
    TrainingSessionCreate,
    TrainingSessionResponse,
    TrainingSessionUpdate,
)

router = APIRouter(
    prefix="/training",
    tags=["Training Sessions"],
)


@router.post(
    "",
    response_model=TrainingSessionResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_training(
    training: TrainingSessionCreate,
    service: TrainingService = Depends(get_training_service),
    current_user: User = Depends(get_current_user),
):
    return service.create(training)


@router.get(
    "/{training_id}",
    response_model=TrainingSessionResponse,
)
def get_training(
    training_id: int,
    service: TrainingService = Depends(get_training_service),
    current_user: User = Depends(get_current_user),
):
    return service.get(training_id)


@router.get(
    "/athlete/{athlete_id}",
    response_model=list[TrainingSessionResponse],
)
def get_training_by_athlete(
    athlete_id: int,
    service: TrainingService = Depends(get_training_service),
    current_user: User = Depends(get_current_user),
):
    return service.get_all(athlete_id)


@router.put(
    "/{training_id}",
    response_model=TrainingSessionResponse,
)
def update_training(
    training_id: int,
    updates: TrainingSessionUpdate,
    service: TrainingService = Depends(get_training_service),
    current_user: User = Depends(get_current_user),
):
    return service.update(
        training_id,
        updates,
    )


@router.delete(
    "/{training_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_training(
    training_id: int,
    service: TrainingService = Depends(get_training_service),
    current_user: User = Depends(get_current_user),
):
    service.delete(training_id)
