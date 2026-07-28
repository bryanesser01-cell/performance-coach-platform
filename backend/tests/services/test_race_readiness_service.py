from api.services.race_readiness_service import (
    calculate_race_readiness_score,
    generate_race_readiness_report,
)


def test_calculate_high_readiness_score():

    score = calculate_race_readiness_score(
        training_load=90,
        performance_score=95,
        fatigue_score=85,
        consistency_score=90,
    )

    assert score >= 90


def test_generate_ready_report():

    result = generate_race_readiness_report(
        training_load=80,
        performance_score=85,
        fatigue_score=80,
        consistency_score=90,
    )

    assert (
        result["status"]
        == "ready"
    )

    assert (
        "race_readiness_score"
        in result
    )


def test_low_readiness_requires_recovery():

    result = generate_race_readiness_report(
        training_load=30,
        performance_score=40,
        fatigue_score=20,
        consistency_score=30,
    )

    assert (
        result["status"]
        == "needs_recovery"
    )
