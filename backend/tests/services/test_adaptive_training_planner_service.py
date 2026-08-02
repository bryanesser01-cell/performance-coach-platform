from api.services.adaptive_training_planner_service import (
    adapt_plan_from_results,
    adjust_weekly_load,
    create_training_plan,
    generate_race_preparation_plan,
)


def test_create_training_plan():

    result = create_training_plan(
        goal="Improve 1500m PB",
        event="1500m",
        weeks=12,
        current_time="5:00",
        target_time="4:45",
    )

    assert result["timeline_weeks"] == 12

    assert len(result["phases"]) == 4


def test_adjust_weekly_load_improving():

    result = adjust_weekly_load(
        previous_load=500,
        performance_response="improving",
    )

    assert result["new_load"] == 550


def test_adjust_weekly_load_fatigued():

    result = adjust_weekly_load(
        previous_load=500,
        performance_response="fatigued",
    )

    assert result["new_load"] == 400


def test_adapt_plan_from_results():

    result = adapt_plan_from_results(
        race_result="4:50",
        target_result="4:55",
        fatigue_score=30,
    )

    assert result["action"] == "CONTINUE_PROGRESS"


def test_generate_race_preparation_plan():

    result = generate_race_preparation_plan(
        event="1500m",
        race_date="2026-10-01",
        goal="Personal Best",
    )

    assert result["event"] == "1500m"

    assert len(result["strategy"]) > 0
