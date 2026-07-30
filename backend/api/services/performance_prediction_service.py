"""
Performance Prediction Service

Responsible for:
- estimating future performance
- calculating prediction confidence
- generating athlete-facing predictions

Important:
Predictions are estimates, not guarantees.
"""


def predict_race_performance(
    current_time_seconds: float,
    improvement_percentage: float,
) -> dict:
    """
    Estimate future race performance.

    Lower time is better.
    """

    predicted_time = (
        current_time_seconds
        *
        (
            1
            -
            improvement_percentage / 100
        )
    )


    return {
        "current_time_seconds": (
            current_time_seconds
        ),

        "predicted_time_seconds": round(
            predicted_time,
            2,
        ),

        "improvement_percentage": (
            improvement_percentage
        ),

        "prediction_type": "estimate",
    }



def calculate_prediction_confidence(
    training_consistency: int,
    performance_trend: str,
) -> str:
    """
    Calculate confidence level.

    Based on:
    - consistency
    - performance direction
    """

    if (
        training_consistency >= 75
        and performance_trend == "improving"
    ):

        return "high"


    if (
        training_consistency >= 50
        or performance_trend == "improving"
    ):

        return "medium"


    return "low"



def generate_prediction_range(
    predicted_time_seconds: float,
) -> dict:
    """
    Create performance range.

    Allows natural variation.
    """

    margin = (
        predicted_time_seconds
        *
        0.02
    )


    return {
        "lower_bound_seconds": round(
            predicted_time_seconds - margin,
            2,
        ),

        "upper_bound_seconds": round(
            predicted_time_seconds + margin,
            2,
        ),
    }



def generate_prediction_summary(
    event: str,
    prediction: dict,
    confidence: str,
) -> dict:
    """
    Generate athlete-facing message.
    """

    predicted_time = (
        prediction[
            "predicted_time_seconds"
        ]
    )


    return {
        "event": event,

        "estimated_time_seconds": (
            predicted_time
        ),

        "confidence": confidence,

        "message": (
            f"Based on recent training, "
            f"your estimated {event} "
            "capability is improving. "
            "This is a prediction, not "
            "a guaranteed result."
        ),
    }
