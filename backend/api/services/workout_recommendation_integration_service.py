from api.services.workout_recommendation_service import (
    build_workout_recommendation,
    generate_workout_coach_message,
)


def build_complete_workout_coach_context(
    athlete_state: dict,
    event: str,
    goal_time: str | None = None,
) -> dict:
    """
    Build complete AI Coach workout context.

    Combines:
    - Training progression
    - Workout recommendation
    - Training explanation
    """

    recommendation = build_workout_recommendation(
        athlete_state=athlete_state,
        event=event,
        goal_time=goal_time,
    )

    message = generate_workout_coach_message(
        recommendation,
    )

    return {
        "event": event,
        "goal_time": goal_time,
        "recommendation": recommendation,
        "coach_message": message,
    }


def get_workout_summary(
    workout_context: dict,
) -> dict:
    """
    Return simple workout summary
    for athlete display.
    """

    workout = workout_context.get(
        "recommendation",
        {},
    ).get(
        "workout",
        {},
    )

    explanation = workout.get(
        "athlete_explanation",
        {},
    )

    return {
        "session": workout.get(
            "workout",
            "",
        ),
        "effort": explanation.get(
            "effort",
            "",
        ),
        "feeling": explanation.get(
            "feeling",
            "",
        ),
        "purpose": explanation.get(
            "purpose",
            "",
        ),
    }


def needs_coach_adjustment(
    athlete_state: dict,
) -> bool:
    """
    Check if coach should modify
    planned workout.
    """

    readiness = athlete_state.get(
        "readiness",
        {},
    )

    score = readiness.get(
        "score",
        80,
    )

    training = athlete_state.get(
        "training",
        {},
    )

    load_status = training.get(
        "load_status",
        "",
    )

    if score < 60:
        return True

    if load_status == "high":
        return True

    return False
