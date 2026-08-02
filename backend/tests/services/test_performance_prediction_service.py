from api.services.performance_prediction_service import (
    calculate_prediction_confidence,
    generate_prediction_range,
    generate_prediction_summary,
    predict_race_performance,
)


def test_predict_race_performance():

    result = predict_race_performance(
        current_time_seconds=1380,
        improvement_percentage=5,
    )

    assert result["predicted_time_seconds"] == 1311


def test_prediction_confidence():

    result = calculate_prediction_confidence(
        training_consistency=90,
        performance_trend="improving",
    )

    assert result == "high"


def test_prediction_range():

    result = generate_prediction_range(
        predicted_time_seconds=1300,
    )

    assert result["lower_bound_seconds"] < 1300

    assert result["upper_bound_seconds"] > 1300


def test_prediction_summary():

    result = generate_prediction_summary(
        event="5K",
        prediction={
            "predicted_time_seconds": 1300,
        },
        confidence="medium",
    )

    assert result["event"] == "5K"

    assert result["confidence"] == "medium"
