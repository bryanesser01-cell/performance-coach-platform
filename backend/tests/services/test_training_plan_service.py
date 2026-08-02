from api.services.training_plan_service import (
    generate_training_plan,
)


def test_generate_training_plan():
    result = generate_training_plan(
        goal="5k",
        fitness_status="progressing",
        training_load="stable",
    )

    assert result["goal"] == "5k"
    assert len(result["weekly_sessions"]) == 3


def test_generate_recovery_plan_when_needs_attention():
    result = generate_training_plan(
        goal="5k",
        fitness_status="needs_attention",
        training_load="stable",
    )

    assert result["weekly_sessions"][0]["workout"] == "Recovery Run"


def test_generate_plan_with_increasing_load():
    result = generate_training_plan(
        goal="10k",
        fitness_status="progressing",
        training_load="increasing",
    )

    assert result["weekly_sessions"][1]["workout"] == "Threshold Session"
