from sqlalchemy.orm import Session

from api.services.goal_analysis import analyse_goal
from database.repositories.athlete_repository import AthleteRepository
from database.repositories.goal_repository import GoalRepository
from database.repositories.training_repository import TrainingRepository
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
    athlete = athlete_repository.get_by_id(goal.athlete_id)

    if athlete is None:
        raise ValueError(f"Athlete {goal.athlete_id} not found.")

    # Retrieve training sessions
    sessions = training_repository.get_by_athlete(athlete.id)

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


def get_goal_progress_service(
    db: Session,
    athlete_id: int,
):
    goal_repository = GoalRepository(db)
    athlete_repository = AthleteRepository(db)
    training_repository = TrainingRepository(db)

    athlete = athlete_repository.get_by_id(
        athlete_id,
    )

    if athlete is None:
        raise ValueError(f"Athlete {athlete_id} not found.")

    goals = goal_repository.get_active_goals(
        athlete_id,
    )

    sessions = training_repository.get_by_athlete(
        athlete_id,
    )

    results = []

    for goal in goals:
        analysis = analyse_goal(
            goal,
            athlete,
            sessions,
        )

        results.append(
            {
                "goal": goal,
                "analysis": analysis,
            }
        )

    return results
