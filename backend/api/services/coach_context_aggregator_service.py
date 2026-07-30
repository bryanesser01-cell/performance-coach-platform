from api.services.activity_memory_integration_service import (
    build_activity_coach_prompt_context,
)
from api.services.recovery_memory_integration_service import (
    build_recovery_coach_prompt_context,
)


def merge_training_intelligence(
    training_memory: dict,
    activity_context: dict,
    recovery_context: dict,
    learning_memory: dict,
) -> dict:
    """
    Combine all AI Coach intelligence sources.

    Sources:
    - Training history
    - Activity intelligence
    - Recovery intelligence
    - Learning history
    """

    return {
        "training": training_memory,
        "activity": activity_context,
        "recovery": recovery_context,
        "learning": learning_memory,
    }


def build_coach_context(
    athlete_id: int,
    athlete_state: dict | None = None,
    training_memory: dict | None = None,
    learning_memory: dict | None = None,
    activities: list[dict] | None = None,
    recovery_data: dict | None = None,
) -> dict:
    """
    Build unified AI Coach context.

    This becomes the main brain input
    for future coaching decisions.
    """

    if athlete_state is None:
        athlete_state = {}

    if training_memory is None:
        training_memory = {}

    if learning_memory is None:
        learning_memory = {}

    if activities is None:
        activities = []

    if recovery_data is None:
        recovery_data = {
            "readiness_score": 0,
        }

    activity_context = (
        build_activity_coach_prompt_context(
            activities,
        )
        if activities
        else {}
    )

    recovery_context = (
        build_recovery_coach_prompt_context(
            recovery_data,
        )
    )

    intelligence = merge_training_intelligence(
        training_memory=training_memory,
        activity_context=activity_context,
        recovery_context=recovery_context,
        learning_memory=learning_memory,
    )

    return {
        "athlete_id": athlete_id,
        "athlete_state": athlete_state,
        "intelligence": intelligence,
    }


def generate_coach_context_summary(
    coach_context: dict,
) -> dict:
    """
    Generate a simplified summary
    for AI Coach decisions.
    """

    intelligence = coach_context.get(
        "intelligence",
        {},
    )

    activity = intelligence.get(
        "activity",
        {},
    )

    recovery = intelligence.get(
        "recovery",
        {},
    )

    learning = intelligence.get(
        "learning",
        {},
    )

    return {
        "training_stress": activity.get(
            "training_stress",
            0,
        ),
        "fitness_trend": activity.get(
            "fitness_trend",
            "unknown",
        ),
        "readiness_score": recovery.get(
            "readiness_score",
            0,
        ),
        "learning_confidence": learning.get(
            "confidence_adjustment",
            0,
        ),
    }
