from api.services.athlete_insights_narrative_service import (
    generate_insight_narrative,
)


def test_generates_improving_performance_narrative():

    result = generate_insight_narrative(
        fitness_trend="improving",
        pace_improvement_seconds_per_km=30,
        consistency_score=90,
    )

    assert "improving" in result["summary"]

    assert "30" in result["summary"]


def test_detects_recovery_requirement():

    result = generate_insight_narrative(
        fitness_trend="improving",
        pace_improvement_seconds_per_km=10,
        consistency_score=85,
        training_load_status="high",
    )

    assert "recovery" in result["recommendation"]


def test_handles_declining_performance():

    result = generate_insight_narrative(
        fitness_trend="declining",
        pace_improvement_seconds_per_km=0,
        consistency_score=40,
    )

    assert "recovery" in result["summary"] or "need" in result["summary"]
