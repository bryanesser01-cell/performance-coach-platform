from api.models.coach_context import CoachContext
from api.services.confidence_engine import (
    ConfidenceEngine,
)


def test_calculates_confidence():

    context = CoachContext(
        athlete_id=1,
    )

    context.athlete_state = {
        "readiness": {
            "score": 85,
        },
    }

    context.performance_prediction = {
        "confidence": "high",
    }

    context.recovery_intelligence = {
        "status": "good",
    }

    context.training_load_intelligence = {
        "risk": "low",
    }

    result = ConfidenceEngine().calculate(
        context,
    )

    assert result["score"] == 75
    assert result["confidence"] == "medium"
