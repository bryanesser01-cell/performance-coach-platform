from sqlalchemy.orm import Session

from repositories.goal_repository import GoalRepository
from repositories.athlete_repository import AthleteRepository
from repositories.training_repository import TrainingRepository

from api.services.goal_analysis import analyse_goal

from schemas.goal import GoalCreate


def list_goals(
    db: Session,
):
    repository = GoalRepository(db)
    return repository.get_all()


def create_goal_service(
    db: Session,
    goal: GoalCreate,
):
    goal_repository = GoalRepository(db)
    athlete_repository = AthleteRepository(db)
    training_repository = TrainingRepository(db)

    # Save the goal
    saved_goal = goal_repository.create(goal)

    # Retrieve athlete
    athlete = athlete_repository.get_by_id(
        goal.athlete_id
    )

    if athlete is None:
        raise ValueError(
            f"Athlete {goal.athlete_id} not found."
        )

    # Retrieve training sessions
    sessions = training_repository.get_by_athlete(
        athlete.id
    )

    # Analyse the goal
    analysis = analyse_goal(
        saved_goal,
        athlete,
        sessions,
    )

    return {
        "goal": saved_goal,
        "analysis": analysis,
    }