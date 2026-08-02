from api.models.coach_context import CoachContext
from api.services.decision_scoring_engine import (
    DecisionScoringEngine,
)


def test_scores_progress_training():

    context = CoachContext(
        athlete_id=1,
    )

    context.athlete_state = {
        "readiness": {
            "score": 85,
        },
    }

    context.goal_intelligence = {
        "on_track": True,
    }

    context.performance_intelligence = {
        "trend": "improving",
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

    context.race_intelligence = {
        "phase": "Base",
    }

    result = DecisionScoringEngine().score(
        context,
    )

    assert result["decision"] == "PROGRESS_TRAINING"
    assert result["score"] == 80
    assert result["confidence"] == "high"
    assert "scores" in result
    assert "ranking" in result
    assert "reasons" in result
