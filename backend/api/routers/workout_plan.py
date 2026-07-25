from fastapi import APIRouter, Depends, HTTPException, status

from api.dependencies.auth import get_current_user
from api.dependencies.services import get_workout_plan_service
from api.services.workout_plan_service import WorkoutPlanService
from schemas.workout_plan import (
    WorkoutPlanCreate,
    WorkoutPlanResponse,
    WorkoutPlanUpdate,
)

router = APIRouter(
    prefix="/workout-plans",
    tags=["Workout Plans"],
)


@router.post(
    "",
    response_model=WorkoutPlanResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_workout_plan(
    workout_plan_data: WorkoutPlanCreate,
    service: WorkoutPlanService = Depends(get_workout_plan_service),
    current_user=Depends(get_current_user),
):
    return service.create_workout_plan(workout_plan_data)


@router.get(
    "/{workout_plan_id}",
    response_model=WorkoutPlanResponse,
)
def get_workout_plan(
    workout_plan_id: int,
    service: WorkoutPlanService = Depends(get_workout_plan_service),
    current_user=Depends(get_current_user),
):
    workout_plan = service.get_workout_plan(workout_plan_id)

    if workout_plan is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Workout plan not found",
        )

    return workout_plan


@router.get(
    "/athlete/{athlete_id}",
    response_model=list[WorkoutPlanResponse],
)
def get_workout_plans_by_athlete(
    athlete_id: int,
    service: WorkoutPlanService = Depends(get_workout_plan_service),
    current_user=Depends(get_current_user),
):
    return service.get_workout_plans_by_athlete(athlete_id)


@router.put(
    "/{workout_plan_id}",
    response_model=WorkoutPlanResponse,
)
def update_workout_plan(
    workout_plan_id: int,
    workout_plan_data: WorkoutPlanUpdate,
    service: WorkoutPlanService = Depends(get_workout_plan_service),
    current_user=Depends(get_current_user),
):
    workout_plan = service.update_workout_plan(
        workout_plan_id,
        workout_plan_data,
    )

    if workout_plan is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Workout plan not found",
        )

    return workout_plan


@router.delete(
    "/{workout_plan_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_workout_plan(
    workout_plan_id: int,
    service: WorkoutPlanService = Depends(get_workout_plan_service),
    current_user=Depends(get_current_user),
):
    deleted = service.delete_workout_plan(workout_plan_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Workout plan not found",
        )
