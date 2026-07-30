from api.services.athlete_strategy_engine_service import (
    build_athlete_strategy_profile,
    generate_strategy_recommendation,
    run_athlete_strategy_engine,
    select_personalised_training_strategy,
)


def test_build_strategy_profile_recovery_first():

    result = build_athlete_strategy_profile(
        athlete_profile={
            "sport": "running",
        },
        training_history=[],
        recovery_history=[],
        decision_analysis={
            "REDUCE_TRAINING": {
                "success_rate": 90,
            },
            "PROGRESS_TRAINING": {
                "success_rate": 60,
            },
        },
    )

    assert (
        result["preferred_strategy"]
        == "RECOVERY_FIRST"
    )


def test_build_strategy_profile_progression():

    result = build_athlete_strategy_profile(
        athlete_profile={},
        training_history=[],
        recovery_history=[],
        decision_analysis={
            "REDUCE_TRAINING": {
                "success_rate": 50,
            },
            "PROGRESS_TRAINING": {
                "success_rate": 85,
            },
        },
    )

    assert (
        result["preferred_strategy"]
        == "PROGRESSION_FOCUSED"
    )


def test_low_readiness_prioritises_recovery():

    result = select_personalised_training_strategy(
        {
            "preferred_strategy": (
                "PROGRESSION_FOCUSED"
            ),
            "confidence": 80,
        },
        {
            "readiness_score": 30,
        },
    )

    assert (
        result["strategy"]
        == "RECOVERY_FIRST"
    )


def test_generate_strategy_recommendation():

    result = generate_strategy_recommendation(
        athlete_id=1,
        strategy_result={
            "strategy": "RECOVERY_FIRST",
            "confidence": 90,
        },
    )

    assert (
        result["recommended_strategy"]
        == "RECOVERY_FIRST"
    )

    assert (
        result["confidence"]
        == 90
    )


def test_full_athlete_strategy_engine():

    result = run_athlete_strategy_engine(
        athlete_id=1,
        athlete_profile={
            "sport": "running",
        },
        training_history=[
            {"type": "run"},
        ],
        recovery_history=[],
        decision_analysis={
            "REDUCE_TRAINING": {
                "success_rate": 85,
            },
        },
        current_state={
            "readiness_score": 70,
        },
    )

    assert (
        result["athlete_id"]
        == 1
    )

    assert (
        result["recommended_strategy"]
        == "RECOVERY_FIRST"
    )
