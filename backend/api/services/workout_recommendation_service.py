from api.services.training_explanation_service import (
    explain_workout,
)
from api.services.training_progression_integration_service import (
    build_training_progression_context,
)


def build_workout_recommendation(
    athlete_state: dict,
    event: str,
    goal_time: str | None = None,
) -> dict:
    """
    Build complete athlete workout recommendation.

    Combines:
    - Training progression
    - Training explanation
    - Athlete readiness
    - Race goal
    """

    progression_context = (
        build_training_progression_context(
            athlete_state=athlete_state,
            event=event,
            goal_time=goal_time,
        )
    )

    recommendation = progression_context.get(
        "recommendation",
        {},
    )

    explained_workout = explain_workout(
        recommendation,
    )

    return {
        "event": event,
        "goal_time": goal_time,
        "readiness": progression_context.get(
            "readiness",
            {},
        ),
        "workout": explained_workout,
        "coach_reason": (
            recommendation.get(
                "purpose",
                "Improve performance.",
            )
        ),
    }


def generate_workout_coach_message(
    workout_recommendation: dict,
) -> str:
    """
    Convert workout recommendation
    into athlete-friendly message.
    """

    workout = workout_recommendation.get(
        "workout",
        {},
    )

    explanation = workout.get(
        "athlete_explanation",
        {},
    )

    return (
        f"Your next session is: "
        f"{workout.get('workout', 'planned training')}. "
        f"It should feel like "
        f"{explanation.get('effort', 'controlled effort')}. "
        f"{explanation.get('feeling', '')} "
        f"The purpose is "
        f"{explanation.get('purpose', '')}"
    )


def should_adjust_workout(
    athlete_state: dict,
) -> bool:
    """
    Check if workout should be reduced
    due to readiness.
    """

    readiness = athlete_state.get(
        "readiness",
        {},
    )

    score = readiness.get(
        "score",
        80,
    )

    return score < 60
