from api.services.training_progression_integration_service import (
    build_training_progression_context,
    generate_training_progression_message,
    should_modify_training_progression,
)


def test_build_training_progression_context():

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

    context = build_training_progression_context(
        athlete_state=athlete_state,
        event="1500m",
        goal_time="4:45",
    )

    assert (
        context["event"]
        == "1500m"
    )

    assert (
        context["recommendation"]
        ["session_type"]
        == "interval"
    )


def test_training_progression_message():

    context = {
        "recommendation": {
            "workout": (
                "5 x 400m at race pace"
            ),
            "purpose": (
                "Improve race pace tolerance"
            ),
        }
    }

    message = (
        generate_training_progression_message(
            context,
        )
    )

    assert (
        "5 x 400m"
        in message
    )

    assert (
        "race pace"
        in message
    )


def test_low_readiness_modifies_training():

    athlete_state = {
        "readiness": {
            "score": 45,
        }
    }

    assert (
        should_modify_training_progression(
            athlete_state,
        )
        is True
    )


def test_good_readiness_keeps_training():

    athlete_state = {
        "readiness": {
            "score": 85,
        }
    }

    assert (
        should_modify_training_progression(
            athlete_state,
        )
        is False
    )
