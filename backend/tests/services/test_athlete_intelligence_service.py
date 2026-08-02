from api.services.athlete_intelligence_service import (
    build_athlete_intelligence_profile,
    calculate_performance_trend,
    calculate_readiness_score,
    calculate_training_fatigue,
)


def test_calculate_readiness_score():

    result = calculate_readiness_score(
        sleep_score=90,
        recovery_score=85,
        recent_training_load=300,
    )

    assert "readiness_score" in result

    assert 0 <= result["readiness_score"] <= 100


def test_calculate_training_fatigue():

    result = calculate_training_fatigue(
        training_load=900,
        recovery_score=40,
    )

    assert "fatigue_score" in result

    assert 0 <= result["fatigue_score"] <= 100


def test_calculate_performance_trend():

    result = calculate_performance_trend(
        [
            300,
            320,
            340,
        ],
    )

    assert result["trend"] == "IMPROVING"


def test_build_athlete_intelligence_profile():

    result = build_athlete_intelligence_profile(
        readiness_score=90,
        fatigue_score=20,
        performance_trend="IMPROVING",
    )

    assert result["status"] == "READY_TO_PERFORM"
