from api.services.recovery_intelligence_service import (
    analyse_recovery_status,
    calculate_readiness_score,
    generate_recovery_recommendation,
)


def test_calculate_high_readiness():

    result = calculate_readiness_score(
        sleep_score=90,
        soreness_score=10,
        energy_score=90,
        motivation_score=90,
        training_load=100,
    )

    assert result >= 80


def test_calculate_low_readiness():

    result = calculate_readiness_score(
        sleep_score=40,
        soreness_score=80,
        energy_score=40,
        motivation_score=40,
        training_load=600,
    )

    assert result < 50


def test_recovery_status():

    result = analyse_recovery_status(
        85,
    )

    assert (
        result["status"]
        == "excellent"
    )


def test_generate_recovery_recommendation():

    result = generate_recovery_recommendation(
        35,
    )

    assert (
        "recovery"
        in result["recommendation"].lower()
    )
