from api.services.race_readiness_service import (
    analyse_race_readiness,
    calculate_race_readiness_score,
    generate_race_readiness_summary,
)


def test_race_readiness_score():

    result = calculate_race_readiness_score(
        training_consistency=90,
        performance_trend="improving",
        recovery_status="good",
        recent_training_load="appropriate",
    )

    assert result["status"] == "ready"

    assert result["readiness_score"] == 100


def test_analyse_race_readiness():

    result = analyse_race_readiness(
        {
            "training_consistency": 70,
            "performance_trend": "improving",
            "recovery_status": "good",
            "recent_training_load": "appropriate",
        }
    )

    assert "race_readiness" in result


def test_generate_race_readiness_summary():

    result = generate_race_readiness_summary(
        {
            "race_readiness": {
                "status": "ready",
            }
        }
    )

    assert result["status"] == "ready"
