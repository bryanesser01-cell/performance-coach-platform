from api.services.goal_analysis import analyse_goal
from core.exceptions import ResourceNotFoundError
from database.goal_models import Goal
from repositories.athlete_repository import AthleteRepository
from repositories.goal_repository import GoalRepository
from repositories.training_repository import TrainingRepository
from schemas.goal import (
    GoalAnalysis,
    GoalAnalysisResponse,
    GoalCreate,
    GoalResponse,
)


class GoalService:
    """
    Service responsible for Goal business logic.
    """

    def __init__(
        self,
        goal_repository: GoalRepository,
        athlete_repository: AthleteRepository,
        training_repository: TrainingRepository,
    ):
        self.goal_repository = goal_repository
        self.athlete_repository = athlete_repository
        self.training_repository = training_repository

    def get_all(
        self,
        athlete_id: int,
        user_id: int,
    ) -> list[Goal]:
        """
        Retrieve all goals for an athlete belonging to the current user.
        """
        athlete = self.athlete_repository.get_by_id_and_user(
            athlete_id,
            user_id,
        )

        if athlete is None:
            raise ResourceNotFoundError("Athlete not found.")

        return self.goal_repository.get_by_athlete(
            athlete.id,
        )

    def create(
        self,
        goal: GoalCreate,
        user_id: int,
    ) -> GoalAnalysisResponse:
        """
        Create a goal and return its analysis.
        """
        athlete = self.athlete_repository.get_by_id_and_user(
            goal.athlete_id,
            user_id,
        )

        if athlete is None:
            raise ResourceNotFoundError("Athlete not found.")

        db_goal = Goal(**goal.model_dump(exclude_none=True))

        saved_goal = self.goal_repository.create(
            db_goal,
        )

        sessions = self.training_repository.get_by_athlete(
            athlete.id,
        )

        analysis = analyse_goal(
            saved_goal,
            athlete,
            sessions,
        )

        return GoalAnalysisResponse(
            goal=GoalResponse.model_validate(
                saved_goal,
            ),
            analysis=GoalAnalysis.model_validate(
                analysis,
            ),
        )

    def get(
        self,
        goal_id: int,
        user_id: int,
    ) -> Goal:
        """
        Retrieve a goal belonging to the current user.
        """
        goal = self.goal_repository.get_by_id(
            goal_id,
        )

        if goal is None:
            raise ResourceNotFoundError("Goal not found.")

        athlete = self.athlete_repository.get_by_id_and_user(
            goal.athlete_id,
            user_id,
        )

        if athlete is None:
            raise ResourceNotFoundError("Goal not found.")

        return goal

    def delete(
        self,
        goal_id: int,
        user_id: int,
    ) -> None:
        """
        Delete a goal belonging to the current user.
        """
        goal = self.get(
            goal_id,
            user_id,
        )

        self.goal_repository.delete(
            goal,
        )
