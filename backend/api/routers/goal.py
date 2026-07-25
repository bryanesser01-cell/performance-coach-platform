from fastapi import APIRouter, Depends, Response, status

from api.dependencies.auth import get_current_user
from api.dependencies.services import get_goal_service
from api.services.goal_service import GoalService
from database.user_models import User
from schemas.goal import (
    GoalAnalysisResponse,
    GoalCreate,
    GoalResponse,
)

router = APIRouter(
    prefix="/goals",
    tags=["Goals"],
)


@router.post(
    "",
    response_model=GoalAnalysisResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new goal",
)
def create_goal(
    goal: GoalCreate,
    service: GoalService = Depends(get_goal_service),
    current_user: User = Depends(get_current_user),
):
    """
    Create a new goal for one of the authenticated user's athletes
    and return an analysis of its achievability.
    """
    return service.create(
        goal=goal,
        user_id=current_user.id,
    )


@router.get(
    "/athlete/{athlete_id}",
    response_model=list[GoalResponse],
    summary="List athlete goals",
)
def get_goals(
    athlete_id: int,
    service: GoalService = Depends(get_goal_service),
    current_user: User = Depends(get_current_user),
):
    """
    Retrieve all goals for a specific athlete.
    """
    return service.get_all(
        athlete_id=athlete_id,
        user_id=current_user.id,
    )


@router.get(
    "/{goal_id}",
    response_model=GoalResponse,
    summary="Get goal",
)
def get_goal(
    goal_id: int,
    service: GoalService = Depends(get_goal_service),
    current_user: User = Depends(get_current_user),
):
    """
    Retrieve a goal by its ID.
    """
    return service.get(
        goal_id=goal_id,
        user_id=current_user.id,
    )


@router.delete(
    "/{goal_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete goal",
)
def delete_goal(
    goal_id: int,
    service: GoalService = Depends(get_goal_service),
    current_user: User = Depends(get_current_user),
):
    """
    Delete a goal.
    """
    service.delete(
        goal_id=goal_id,
        user_id=current_user.id,
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )
