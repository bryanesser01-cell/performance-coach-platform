def build_coach_response(
    intent: str,
    context: dict,
) -> dict:
    """
    Build consistent AI Coach response.

    Formats:
    - Workout plans
    - Race strategy
    - Training explanations
    - Recovery advice
    """

    if intent == "workout":

        return build_workout_response(
            context,
        )

    if intent == "race_strategy":

        return build_race_response(
            context,
        )

    if intent == "explanation":

        return build_explanation_response(
            context,
        )

    if intent == "recovery":

        return build_recovery_response(
            context,
        )

    return {
        "title": "Coach Advice",
        "message": (
            context.get(
                "message",
                "Keep progressing with your training.",
            )
        ),
    }


def build_workout_response(
    context: dict,
) -> dict:
    """
    Format workout recommendation.
    """

    workout = context.get(
        "workout",
        {},
    )

    explanation = workout.get(
        "athlete_explanation",
        {},
    )

    return {
        "title": "Next Training Session",
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
        "coach_note": workout.get(
            "coach_note",
            "",
        ),
    }


def build_race_response(
    context: dict,
) -> dict:
    """
    Format race strategy response.
    """

    return {
        "title": "Race Strategy",
        "event": context.get(
            "event",
            "",
        ),
        "strategy": context.get(
            "strategy",
            "",
        ),
        "splits": context.get(
            "splits",
            [],
        ),
    }


def build_explanation_response(
    context: dict,
) -> dict:
    """
    Format training explanation.
    """

    return {
        "title": "Training Explanation",
        "term": context.get(
            "term",
            "",
        ),
        "explanation": context.get(
            "explanation",
            "",
        ),
        "effort": context.get(
            "effort",
            "",
        ),
        "purpose": context.get(
            "purpose",
            "",
        ),
    }


def build_recovery_response(
    context: dict,
) -> dict:
    """
    Format recovery advice.
    """

    return {
        "title": "Recovery Advice",
        "message": context.get(
            "message",
            "Focus on recovery today.",
        ),
        "recommendation": context.get(
            "recommendation",
            "",
        ),
    }


def response_to_text(
    response: dict,
) -> str:
    """
    Convert response dictionary
    into athlete friendly text.
    """

    title = response.get(
        "title",
        "Coach",
    )

    parts = [
        title,
    ]

    for value in response.values():

        if (
            isinstance(
                value,
                str,
            )
            and value != title
            and value
        ):
            parts.append(
                value,
            )

    return ". ".join(
        parts,
    )
