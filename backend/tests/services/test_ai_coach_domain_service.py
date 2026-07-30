from api.services.ai_coach_domain_service import (
    build_coach_strategy,
    evaluate_coaching_decision,
    generate_coach_recommendation,
)


def test_evaluate_coaching_decision_recovery():

    result = evaluate_coaching_decision(
        readiness_score=50,
        fatigue_score=80,
        training_load=700,
    )

    assert (
        result["decision"]
        == "RECOVERY"
    )


def test_evaluate_coaching_decision_train():

    result = evaluate_coaching_decision(
        readiness_score=90,
        fatigue_score=20,
        training_load=500,
    )

    assert (
        result["decision"]
        == "TRAIN"
    )


def test_generate_coach_recommendation():

    result = generate_coach_recommendation(
        decision="RECOVERY",
    )

    assert (
        result["decision"]
        == "RECOVERY"
    )

    assert (
        result["recommendation"]
        is not None
    )


def test_build_coach_strategy():

    result = build_coach_strategy(
        decision="RECOVERY",
        recommendation=(
            "Take a recovery day."
        ),
        confidence=90,
    )

    assert (
        result["strategy"]
        == "RECOVERY_FIRST"
    )

    assert (
        result["confidence"]
        == 90
    )
