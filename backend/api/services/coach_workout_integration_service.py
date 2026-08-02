from api.services.coach_workout_planning_service import (
    build_coach_workout_plan,
)


def build_coach_workout_response(
    athlete_state: dict,
    event: str,
    goal_time: str | None = None,
) -> dict:
    """
    Build complete athlete-facing workout response.

    Combines:
    - Coach workout planning
    - Workout details
    - Coaching explanation
    """

    workout_plan = build_coach_workout_plan(
        athlete_state=athlete_state,
        event=event,
        goal_time=goal_time,
    )

    workout = workout_plan.get(
        "workout",
        {},
    )

    return {
        "event": event,
        "goal_time": goal_time,
        "adjusted": workout_plan.get(
            "adjusted",
            False,
        ),
        "workout": workout,
        "coach_message": generate_coach_workout_message(
            workout_plan,
        ),
    }


def generate_coach_workout_message(
    workout_plan: dict,
) -> str:
    """
    Convert workout plan into
    natural coach language.
    """

    workout = workout_plan.get(
        "workout",
        {},
    )

    workout_name = workout.get(
        "workout",
        "planned session",
    )

    explanation = workout.get(
        "athlete_explanation",
        {},
    )

    effort = explanation.get(
        "effort",
        "",
    )

    feeling = explanation.get(
        "feeling",
        "",
    )

    purpose = explanation.get(
        "purpose",
        "",
    )

    coach_note = workout.get(
        "coach_note",
        "",
    )

    message = f"Your next session is: " f"{workout_name}. "

    if effort:

        message += f"Effort: {effort}. "

    if feeling:

        message += f"How it should feel: " f"{feeling} "

    if purpose:

        message += f"Purpose: {purpose}. "

    if coach_note:

        message += coach_note

    return message.strip()


def should_explain_workout(
    question: str,
) -> bool:
    """
    Determine if athlete is asking
    for workout guidance.
    """

    question_lower = question.lower()

    keywords = [
        "workout",
        "train",
        "training",
        "session",
        "tomorrow",
        "next",
        "what should i do",
    ]

    return any(word in question_lower for word in keywords)
