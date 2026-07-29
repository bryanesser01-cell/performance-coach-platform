from api.services.workout_recommendation_integration_service import (
    build_complete_workout_coach_context,
    needs_coach_adjustment,
)


def build_coach_workout_plan(
    athlete_state: dict,
    event: str,
    goal_time: str | None = None,
) -> dict:
    """
    Create final coach workout decision.

    Combines:
    - Athlete readiness
    - Training progression
    - Workout recommendation
    - Training explanation
    """

    adjustment_required = (
        needs_coach_adjustment(
            athlete_state,
        )
    )

    workout_context = (
        build_complete_workout_coach_context(
            athlete_state=athlete_state,
            event=event,
            goal_time=goal_time,
        )
    )

    recommendation = workout_context.get(
        "recommendation",
        {},
    )

    workout = recommendation.get(
        "workout",
        {},
    )

    if adjustment_required:

        workout = {
            **workout,
            "adjusted": True,
            "coach_note": (
                "Workout adjusted due to "
                "current recovery status."
            ),
        }

    else:

        workout = {
            **workout,
            "adjusted": False,
            "coach_note": (
                "Current readiness supports "
                "planned training."
            ),
        }

    return {
        "event": event,
        "goal_time": goal_time,
        "adjusted": adjustment_required,
        "workout": workout,
        "coach_message": workout_context.get(
            "coach_message",
            "",
        ),
    }


def get_coach_workout_decision(
    workout_plan: dict,
) -> str:
    """
    Return the coach decision message.
    """

    if workout_plan.get(
        "adjusted",
        False,
    ):

        return (
            "The workout has been modified "
            "to protect recovery."
        )

    return (
        "The planned workout is suitable "
        "for your current fitness."
    )


def should_skip_quality_session(
    athlete_state: dict,
) -> bool:
    """
    Decide if hard training should be avoided.
    """

    readiness = athlete_state.get(
        "readiness",
        {},
    )

    score = readiness.get(
        "score",
        80,
    )

    return score < 50
