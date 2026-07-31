from api.models.coach_context import CoachContext
from api.services.decision_rules_engine import (
    DecisionRulesEngine,
)


def test_low_readiness():

    context = CoachContext(
        athlete_id=1,
    )

    context.athlete_state = {
        "readiness": {
            "score": 30,
        }
    }

    result = DecisionRulesEngine().evaluate(
        context,
    )

    assert result["decision"] == "RECOVERY_DAY"


def test_progress_training():

    context = CoachContext(
        athlete_id=1,
    )

    context.athlete_state = {
        "readiness": {
            "score": 90,
        }
    }

    context.memory_reasoning = {
        "fatigue_trend": "stable",
        "injury_risk": "low",
    }

    context.performance_intelligence = {
        "performance_trend": {
            "trend": "improving",
        }
    }

    result = DecisionRulesEngine().evaluate(
        context,
    )

    assert result["decision"] == "PROGRESS_TRAINING"


def test_reduce_volume():

    context = CoachContext(
        athlete_id=1,
    )

    context.athlete_state = {
        "readiness": {
            "score": 55,
        }
    }

    context.memory_reasoning = {
        "fatigue_trend": "increasing",
        "injury_risk": "low",
    }

    result = DecisionRulesEngine().evaluate(
        context,
    )

    assert result["decision"] == "REDUCE_VOLUME"
