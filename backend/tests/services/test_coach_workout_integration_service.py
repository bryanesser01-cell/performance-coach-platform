from api.services.coach_workout_integration_service import (
    build_coach_workout_response,
    generate_coach_workout_message,
    should_explain_workout,
)


def test_build_coach_workout_response():

    athlete_state = {
        "readiness": {
            "score": 85,
        },
        "performance": {
            "trend": "improving",
        },
        "training": {
            "load_status": "optimal",
        },
    }

    response = build_coach_workout_response(
        athlete_state=athlete_state,
        event="1500m",
        goal_time="4:45",
    )

    assert response["event"] == "1500m"

    assert response["workout"]["session_type"] == "interval"

    assert "coach_message" in response


def test_generate_coach_workout_message():

    workout_plan = {
        "workout": {
            "workout": ("5 x 400m at race pace"),
            "athlete_explanation": {
                "effort": "8-9/10",
                "feeling": ("Fast and controlled."),
                "purpose": ("Improve race pace ability."),
            },
            "coach_note": ("Current readiness supports " "planned training."),
        }
    }

    message = generate_coach_workout_message(
        workout_plan,
    )

    assert "5 x 400m" in message

    assert "8-9/10" in message


def test_should_explain_workout_question():

    assert should_explain_workout("What should I do tomorrow?") is True


def test_should_not_explain_random_question():

    assert should_explain_workout("What is my current weight?") is False
