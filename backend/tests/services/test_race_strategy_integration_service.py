from api.services.race_strategy_integration_service import (
    build_race_strategy_context,
    generate_race_coach_message,
    should_adjust_race_strategy,
)


def test_build_race_strategy_context():

    athlete_state = {
        "athlete": {
            "name": "Athlete",
        },
        "readiness": {
            "score": 85,
        },
        "performance": {
            "trend": "improving",
        },
    }

    context = build_race_strategy_context(
        athlete_state=athlete_state,
        event="1500m",
        target_time="4:45",
    )

    assert (
        context["race_goal"]["target_time"]
        == "4:45"
    )

    assert (
        context["race_strategy"]["event"]
        == "1500m"
    )

    assert (
        len(
            context["race_strategy"]["checkpoints"]
        )
        == 4
    )


def test_generate_race_coach_message():

    context = build_race_strategy_context(
        athlete_state={},
        event="1500m",
        target_time="4:45",
    )

    message = generate_race_coach_message(
        context,
    )

    assert "1500m" in message

    assert "4:45" in message


def test_should_adjust_strategy_when_low_readiness():

    athlete_state = {
        "readiness": {
            "score": 45,
        }
    }

    assert (
        should_adjust_race_strategy(
            athlete_state,
        )
        is True
    )


def test_should_not_adjust_strategy_when_ready():

    athlete_state = {
        "readiness": {
            "score": 85,
        }
    }

    assert (
        should_adjust_race_strategy(
            athlete_state,
        )
        is False
    )
