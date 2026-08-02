from api.services.recovery_intelligence_service import (
    analyse_recovery_intelligence,
)


def test_builds_recovery():

    athlete_state = {
        "readiness": {
            "sleep_score": 90,
            "soreness_score": 20,
            "energy_score": 85,
            "motivation_score": 90,
        },
        "training": {
            "training_load": 150,
        },
    }

    result = analyse_recovery_intelligence(
        athlete_state,
    )

    assert isinstance(result, dict)
    assert "status" in result
    assert "score" in result
    assert "recommendation" in result
