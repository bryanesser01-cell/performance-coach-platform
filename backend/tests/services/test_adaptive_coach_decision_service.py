from api.services.adaptive_coach_decision_service import (
    generate_coach_decision,
)


def test_reduce_training_when_fatigue_is_high():

    result = generate_coach_decision(
        readiness_score=45,
        training_load_status="high_fatigue",
        performance_trend="declining",
    )

    assert (
        result["decision"]
        == "REDUCE_TRAINING"
    )


def test_progress_training_when_improving():

    result = generate_coach_decision(
        readiness_score=85,
        training_load_status="stable",
        performance_trend="improving",
    )

    assert (
        result["decision"]
        == "PROGRESS_TRAINING"
    )


def test_maintain_training_when_balanced():

    result = generate_coach_decision(
        readiness_score=75,
        training_load_status="stable",
        performance_trend="stable",
    )

    assert (
        result["decision"]
        == "MAINTAIN_TRAINING"
    )


def test_race_taper_before_event():

    result = generate_coach_decision(
        readiness_score=90,
        training_load_status="stable",
        performance_trend="improving",
        days_to_race=7,
    )

    assert (
        result["decision"]
        == "RACE_TAPER"
    )


def test_recovery_session_when_needs_attention():

    result = generate_coach_decision(
        readiness_score=65,
        training_load_status="increasing",
        performance_trend="declining",
    )

    assert (
        result["decision"]
        == "RECOVERY_SESSION"
    )
