from api.services.adaptive_training_plan_service import (
    adapt_training_plan,
)


def test_reduce_plan_when_fatigue_is_high():
    result = adapt_training_plan(
        current_plan={
            "goal": "5k",
        },
        completed_sessions=3,
        missed_sessions=0,
        fatigue_level="high",
    )

    assert result["adjustment"] == "reduce_load"


def test_maintain_plan_when_sessions_are_missed():
    result = adapt_training_plan(
        current_plan={
            "goal": "5k",
        },
        completed_sessions=1,
        missed_sessions=2,
        fatigue_level="normal",
    )

    assert result["adjustment"] == "maintain"


def test_progress_plan_when_training_is_consistent():
    result = adapt_training_plan(
        current_plan={
            "goal": "5k",
        },
        completed_sessions=4,
        missed_sessions=0,
        fatigue_level="normal",
    )

    assert result["adjustment"] == "progress"
