from api.models.athlete_digital_twin import AthleteDigitalTwin
from api.models.coach_context import CoachContext
from api.services.decision_rules_engine import (
    DecisionRulesEngine,
)


def test_returns_decision():

    context = CoachContext(
        athlete_id=1,
    )

    context.athlete_state = {
        "readiness": {
            "score": 85,
        },
    }

    context.memory_reasoning = {
        "fatigue_trend": "stable",
        "injury_risk": "low",
    }

    context.goal_intelligence = {
        "on_track": True,
    }

    context.performance_intelligence = {
        "trend": "improving",
        "recommendation": "progress",
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

    context.performance_prediction = {
        "confidence": "medium",
    }

    #
    # Build Athlete Digital Twin
    #
    context.athlete_digital_twin = AthleteDigitalTwin(
        athlete=context.athlete_state,
        goal_intelligence=context.goal_intelligence,
        performance_intelligence=context.performance_intelligence,
        recovery_intelligence=context.recovery_intelligence,
        training_load_intelligence=context.training_load_intelligence,
        race_intelligence=context.race_intelligence,
        memory_reasoning=context.memory_reasoning,
    )

    result = DecisionRulesEngine().evaluate(
        context,
    )

    assert result["decision"] == "PROGRESS_TRAINING"
    assert result["confidence"] == 95
    assert "High readiness" in result["reason"]


def test_high_acwr_reduces_volume(): ...
