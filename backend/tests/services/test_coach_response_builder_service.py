from api.services.coach_response_builder_service import (
    build_coach_response,
    response_to_text,
)


def test_build_workout_response():

    context = {
        "workout": {
            "workout": (
                "5 x 400m at race pace"
            ),
            "athlete_explanation": {
                "effort": "8-9/10",
                "feeling": (
                    "Fast but controlled."
                ),
                "purpose": (
                    "Improve race pace."
                ),
            },
            "coach_note": (
                "Stay consistent."
            ),
        }
    }

    response = build_coach_response(
        intent="workout",
        context=context,
    )

    assert (
        response["title"]
        == "Next Training Session"
    )

    assert (
        "400m"
        in response["session"]
    )

    assert (
        response["effort"]
        == "8-9/10"
    )


def test_build_race_response():

    context = {
        "event": "1500m",
        "strategy": (
            "Controlled first lap"
        ),
        "splits": [
            "300m - 57 seconds",
        ],
    }

    response = build_coach_response(
        intent="race_strategy",
        context=context,
    )

    assert (
        response["title"]
        == "Race Strategy"
    )

    assert (
        response["event"]
        == "1500m"
    )


def test_build_explanation_response():

    context = {
        "term": "threshold",
        "explanation": (
            "Controlled hard running"
        ),
        "effort": "7/10",
        "purpose": (
            "Improve endurance"
        ),
    }

    response = build_coach_response(
        intent="explanation",
        context=context,
    )

    assert (
        response["title"]
        == "Training Explanation"
    )

    assert (
        response["effort"]
        == "7/10"
    )


def test_response_to_text():

    response = {
        "title": "Coach Advice",
        "message": (
            "Keep progressing."
        ),
    }

    text = response_to_text(
        response,
    )

    assert (
        "Coach Advice"
        in text
    )

    assert (
        "Keep progressing"
        in text
    )
