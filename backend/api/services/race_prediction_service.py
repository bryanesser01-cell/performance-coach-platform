def predict_race_time(
    recent_time_seconds: int,
    readiness_score: int,
    performance_trend: str,
) -> dict:
    """
    Predict race performance based on current fitness.

    Uses:
    - Recent race performance
    - Race readiness score
    - Performance trend
    """

    predicted_time = recent_time_seconds

    if performance_trend == "improving":
        predicted_time *= 0.98

    elif performance_trend == "declining":
        predicted_time *= 1.03

    if readiness_score >= 90:
        predicted_time *= 0.99

    elif readiness_score < 60:
        predicted_time *= 1.02

    predicted_time = round(
        predicted_time,
    )

    return {
        "predicted_time_seconds": predicted_time,
        "confidence": calculate_prediction_confidence(
            readiness_score,
            performance_trend,
        ),
        "outlook": get_prediction_outlook(
            predicted_time,
            recent_time_seconds,
        ),
    }


def calculate_prediction_confidence(
    readiness_score: int,
    performance_trend: str,
) -> int:
    """
    Calculate confidence in prediction.
    """

    confidence = readiness_score

    if performance_trend == "stable":
        confidence += 5

    elif performance_trend == "declining":
        confidence -= 10

    return min(
        max(confidence, 0),
        100,
    )


def get_prediction_outlook(
    predicted_time: int,
    recent_time: int,
) -> str:
    """
    Determine race outlook.
    """

    if predicted_time < recent_time:
        return "positive"

    if predicted_time == recent_time:
        return "stable"

    return "needs_improvement"
