from api.services.race_prediction_service import (
    predict_race_time,
)


def test_predict_improved_race_time():

    result = predict_race_time(
        recent_time_seconds=1200,
        readiness_score=90,
        performance_trend="improving",
    )

    assert (
        result["predicted_time_seconds"]
        < 1200
    )

    assert (
        result["outlook"]
        == "positive"
    )


def test_prediction_confidence():

    result = predict_race_time(
        recent_time_seconds=1500,
        readiness_score=85,
        performance_trend="stable",
    )

    assert (
        result["confidence"]
        == 90
    )


def test_declining_performance():

    result = predict_race_time(
        recent_time_seconds=1200,
        readiness_score=50,
        performance_trend="declining",
    )

    assert (
        result["outlook"]
        == "needs_improvement"
    )
