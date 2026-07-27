from sqlalchemy.orm import Session

from database.repositories.training_repository import TrainingRepository


def calculate_performance_score(
    db: Session,
    athlete_id: int,
):
    """
    Calculate athlete performance intelligence summary.
    """

    repository = TrainingRepository(db)

    weekly_distance = repository.get_weekly_distance(
        athlete_id,
    )

    training_load = repository.get_training_load(
        athlete_id,
    )

    recent_sessions = repository.get_recent_sessions(
        athlete_id,
    )

    sessions_completed = len(
        recent_sessions,
    )

    fitness_score = min(
        100,
        weekly_distance * 2,
    )

    fatigue_score = min(
        100,
        training_load / 5,
    )

    consistency_score = min(
        100,
        sessions_completed * 10,
    )

    readiness_score = max(
        0,
        fitness_score - fatigue_score + consistency_score / 2,
    )

    return {
        "athlete_id": athlete_id,
        "fitness_score": round(
            fitness_score,
            2,
        ),
        "fatigue_score": round(
            fatigue_score,
            2,
        ),
        "consistency_score": round(
            consistency_score,
            2,
        ),
        "readiness_score": round(
            readiness_score,
            2,
        ),
    }
