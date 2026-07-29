from api.services.training_progression_service import (
    recommend_next_workout,
)


def build_training_progression_context(
    athlete_state: dict,
    event: str,
    goal_time: str | None = None,
) -> dict:
    """
    Build training progression context
    for AI Coach.

    Uses:
    - Athlete state
    - Goal
    - Readiness
    - Event
    """

    readiness = athlete_state.get(
        "readiness",
        {},
    )

    performance = athlete_state.get(
        "performance",
        {},
    )

    training = athlete_state.get(
        "training",
        {},
    )

    readiness_score = readiness.get(
        "score",
        80,
    )

    recommendation = recommend_next_workout(
        event=event,
        goal_time=goal_time,
        readiness_score=readiness_score,
    )

    return {
        "event": event,
        "goal_time": goal_time,
        "readiness": {
            "score": readiness_score,
        },
        "performance": {
            "trend": performance.get(
                "trend",
                "unknown",
            ),
        },
        "training": {
            "load_status": training.get(
                "load_status",
                "unknown",
            ),
        },
        "recommendation": recommendation,
    }


def generate_training_progression_message(
    progression_context: dict,
) -> str:
    """
    Convert training progression
    into AI Coach response.
    """

    recommendation = progression_context.get(
        "recommendation",
        {},
    )

    workout = recommendation.get(
        "workout",
        "Complete your planned session.",
    )

    purpose = recommendation.get(
        "purpose",
        "",
    )

    return (
        f"Your next session is: "
        f"{workout}. "
        f"Purpose: {purpose}."
    )


def should_modify_training_progression(
    athlete_state: dict,
) -> bool:
    """
    Decide whether workout should
    be modified due to readiness.
    """

    readiness = athlete_state.get(
        "readiness",
        {},
    )

    score = readiness.get(
        "score",
        0,
    )

    return score < 60
