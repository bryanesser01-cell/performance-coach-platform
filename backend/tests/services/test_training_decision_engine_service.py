from api.services.training_decision_engine_service import (
    evaluate_training_readiness,
    generate_daily_training_decision,
    select_training_intensity,
)


def test_evaluate_training_readiness_ready():

    result = evaluate_training_readiness(
        readiness_score=90,
        fatigue_score=20,
        performance_trend="IMPROVING",
    )

    assert (
        result["readiness_status"]
        == "READY"
    )


def test_evaluate_training_readiness_recovery():

    result = evaluate_training_readiness(
        readiness_score=50,
        fatigue_score=80,
        performance_trend="DECLINING",
    )

    assert (
        result["readiness_status"]
        == "RECOVERY_REQUIRED"
    )


def test_select_training_intensity():

    result = select_training_intensity(
        readiness_status="READY",
        performance_trend="IMPROVING",
    )

    assert (
        result["intensity"]
        == "HIGH"
    )


def test_generate_daily_training_decision():

    result = generate_daily_training_decision(
        readiness_score=90,
        fatigue_score=20,
        performance_trend="IMPROVING",
    )

    assert (
        result["decision"]
        == "TRAIN_HARD"
    )

    assert (
        result["training_intensity"]
        == "HIGH"
    )
