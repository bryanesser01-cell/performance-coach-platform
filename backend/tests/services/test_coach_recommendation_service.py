from api.services.coach_recommendation_service import (
    generate_recommendation,
)


def test_recommend_progression():
    result = generate_recommendation(
        status="progressing",
        pace_trend="improving",
        training_load_trend="stable",
    )

    assert result["recommendation"] == (
        "continue_progression"
    )


def test_recommend_recovery_when_load_increases():
    result = generate_recommendation(
        status="progressing",
        pace_trend="improving",
        training_load_trend="increasing",
    )

    assert result["recommendation"] == (
        "monitor_recovery"
    )


def test_recommend_reduce_load_when_performance_declines():
    result = generate_recommendation(
        status="needs_attention",
        pace_trend="declining",
        training_load_trend="stable",
    )

    assert result["recommendation"] == (
        "reduce_load"
    )
