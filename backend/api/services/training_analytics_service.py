from sqlalchemy.orm import Session

from database.repositories.training_repository import TrainingRepository


def get_training_summary(
    db: Session,
    athlete_id: int,
):
    """
    Generate training summary for athlete.
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

    return {
        "athlete_id": athlete_id,
        "weekly_distance": weekly_distance,
        "training_load": training_load,
        "recent_sessions": recent_sessions,
    }
