from api.services.adaptive_training_plan_service import (
    adapt_training_plan,
)
from api.services.training_plan_service import (
    generate_training_plan,
)


def test_training_plan_adapts_after_athlete_feedback():

    initial_plan = generate_training_plan(
        goal="5k",
        fitness_status="progressing",
        training_load="stable",
    )

    adjusted_plan = adapt_training_plan(
        current_plan=initial_plan,
        completed_sessions=3,
        missed_sessions=0,
        fatigue_level="normal",
    )

    assert adjusted_plan["adjustment"] == "progress"


def test_training_plan_reduces_when_fatigue_detected():

    initial_plan = generate_training_plan(
        goal="5k",
        fitness_status="progressing",
        training_load="stable",
    )

    adjusted_plan = adapt_training_plan(
        current_plan=initial_plan,
        completed_sessions=4,
        missed_sessions=0,
        fatigue_level="high",
    )

    assert adjusted_plan["adjustment"] == "reduce_load"


def test_training_plan_maintains_after_missed_sessions():

    initial_plan = generate_training_plan(
        goal="10k",
        fitness_status="progressing",
        training_load="stable",
    )

    adjusted_plan = adapt_training_plan(
        current_plan=initial_plan,
        completed_sessions=1,
        missed_sessions=2,
        fatigue_level="normal",
    )

    assert adjusted_plan["adjustment"] == "maintain"
