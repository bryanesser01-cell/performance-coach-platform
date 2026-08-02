from api.services.coach_prompt_builder_service import (
    build_coach_prompt,
    has_race_strategy,
)
from api.services.race_strategy_integration_service import (
    build_race_strategy_context,
)


def test_race_strategy_added_to_prompt():

    athlete_state = {
        "athlete": {
            "name": "Athlete",
            "primary_event": "1500m",
        },
        "readiness": {
            "score": 85,
        },
    }

    race_context = build_race_strategy_context(
        athlete_state=athlete_state,
        event="1500m",
        target_time="4:45",
    )

    prompt = build_coach_prompt(
        question=("How should I run my 1500m race?"),
        athlete_state=athlete_state,
        race_strategy_context=race_context,
    )

    assert prompt["race_strategy"]["race_goal"]["target_time"] == "4:45"


def test_race_strategy_detected():

    context = {
        "race_strategy": {
            "event": "1500m",
        }
    }

    assert (
        has_race_strategy(
            context,
        )
        is True
    )


def test_1500m_checkpoint_generation():

    athlete_state = {
        "athlete": {
            "name": "Athlete",
            "primary_event": "1500m",
        },
    }

    race_context = build_race_strategy_context(
        athlete_state=athlete_state,
        event="1500m",
        target_time="4:45",
    )

    checkpoints = race_context["race_strategy"]["checkpoints"]

    assert checkpoints[0]["distance"] == 300

    assert checkpoints[-1]["distance"] == 1500
