from fastapi import APIRouter, Depends, Response, status

from api.dependencies.auth import get_current_user
from api.dependencies.services import get_athlete_service
from api.services.athlete_service import AthleteService
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
    summary="Create a new athlete",
)
def create_athlete(
    athlete: AthleteCreate,
    service: AthleteService = Depends(get_athlete_service),
    current_user: User = Depends(get_current_user),
):
    """
    Create a new athlete for the authenticated user.
    """
    return service.create(
        user_id=current_user.id,
        athlete=athlete,
    )


@router.get(
    "",
    response_model=list[AthleteResponse],
    summary="List athletes",
)
def get_athletes(
    service: AthleteService = Depends(get_athlete_service),
    current_user: User = Depends(get_current_user),
):
    """
    Retrieve all athletes belonging to the authenticated user.
    """
    return service.get_all(
        user_id=current_user.id,
    )


@router.get(
    "/{athlete_id}",
    response_model=AthleteResponse,
    summary="Get athlete",
)
def get_athlete(
    athlete_id: int,
    service: AthleteService = Depends(get_athlete_service),
    current_user: User = Depends(get_current_user),
):
    """
    Retrieve a single athlete by ID.
    """
    return service.get(
        athlete_id=athlete_id,
        user_id=current_user.id,
    )


@router.put(
    "/{athlete_id}",
    response_model=AthleteResponse,
    summary="Update athlete",
)
def update_athlete(
    athlete_id: int,
    athlete: AthleteUpdate,
    service: AthleteService = Depends(get_athlete_service),
    current_user: User = Depends(get_current_user),
):
    """
    Update an existing athlete.
    """
    return service.update(
        athlete_id=athlete_id,
        user_id=current_user.id,
        updates=athlete,
    )


@router.delete(
    "/{athlete_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete athlete",
)
def delete_athlete(
    athlete_id: int,
    service: AthleteService = Depends(get_athlete_service),
    current_user: User = Depends(get_current_user),
):
    """
    Delete an athlete.
    """
    service.delete(
        athlete_id=athlete_id,
        user_id=current_user.id,
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )
