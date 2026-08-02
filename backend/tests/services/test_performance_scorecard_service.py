from api.services.performance_scorecard_service import (
    calculate_overall_score,
    generate_performance_scorecard,
    generate_scorecard_summary,
)


def test_calculate_overall_score():

    result = calculate_overall_score(
        fitness_score=90,
        consistency_score=80,
        readiness_score=85,
        improvement_score=85,
    )

    assert result == 85


def test_generate_performance_scorecard():

    result = generate_performance_scorecard(
        fitness_score=90,
        consistency_score=80,
        readiness_score=85,
        improvement_score=85,
        trend="improving",
    )

    assert result["overall_score"] == 85

    assert result["status"] == "excellent"


def test_generate_scorecard_summary():

    result = generate_scorecard_summary(
        {
            "overall_score": 85,
            "status": "excellent",
            "trend": "improving",
        }
    )

    assert "excellent" in result["headline"]
