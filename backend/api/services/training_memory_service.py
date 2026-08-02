from sqlalchemy.orm import Session

from database.repositories.training_session_repository import (
    TrainingSessionRepository,
)


def build_training_memory(
    db: Session,
    athlete_id: int,
) -> dict:
    """
    Build training history context
    for AI Coach.

    Includes:
    - Training sessions
    - Workout intervals
    - Target times
    - Recovery details
    """

    repository = TrainingSessionRepository(
        db,
    )

    sessions = repository.get_recent_sessions(
        athlete_id,
    )

    if not isinstance(
        sessions,
        list,
    ):
        sessions = []

    history = []

    for session in sessions:

        workout = []

        intervals = getattr(
            session,
            "intervals",
            [],
        )

        if not isinstance(
            intervals,
            list,
        ):
            intervals = []

        for interval in intervals:

            workout.append(
                {
                    "distance_meters": (interval.distance_meters),
                    "repetitions": (interval.repetitions),
                    "target_time": (interval.target_time),
                    "recovery": (interval.recovery),
                }
            )

        history.append(
            {
                "date": str(
                    session.session_date,
                ),
                "type": (session.session_type),
                "focus": (session.focus),
                "status": (session.status),
                "workout": workout,
            }
        )

    return {
        "athlete_id": athlete_id,
        "training_history": history,
        "has_training_history": len(
            history,
        )
        > 0,
    }


def generate_training_memory_summary(
    context: dict,
) -> str:
    """
    Generate human readable training
    memory summary.
    """

    if not context.get(
        "has_training_history",
        False,
    ):
        return "No previous training sessions " "available."

    count = len(
        context.get(
            "training_history",
            [],
        )
    )

    return f"Athlete has {count} recent " "training session(s) recorded."
