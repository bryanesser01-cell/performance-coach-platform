from api.models.coach_context import CoachContext
from api.services.coach_brain_service import (
    CoachBrainService,
)


def test_build_decision_basic():

    context = CoachContext(
        athlete_id=1,
    )

    context.athlete_state = {
        "readiness": {
            "score": 85,
        },
        "training": {
            "load_status": "low",
        },
        "performance": {
            "trend": "improving",
        },
    }

    context.memory_reasoning = {
        "fatigue_trend": "stable",
        "injury_risk": "low",
    }

    context.decision = {
        "decision": "PROGRESS_TRAINING",
        "recommendation": (
            "Progress training."
        ),
        "learning_confidence": 90,
    }

    result = (
        CoachBrainService()
        .build_decision(
            context=context,
        )
    )

    assert (
        result["decision"]
        == "PROGRESS_TRAINING"
    )

    assert (
        result["recommendation"]
        == "Progress training"
    )

    assert result["confidence"] == 90


def test_reasoning_contains_new_fields():

    context = CoachContext(
        athlete_id=1,
    )

    context.athlete_state = {
        "readiness": {
            "score": 90,
        },
        "training": {
            "load_status": "low",
        },
        "performance": {
            "trend": "improving",
        },
    }

    context.memory_reasoning = {
        "fatigue_trend": "stable",
        "injury_risk": "low",
    }

    context.decision = {}

    result = (
        CoachBrainService()
        .build_decision(
            context=context,
        )
    )

    reasoning = result["reasoning"]

    assert "strengths" in reasoning
    assert "watch_items" in reasoning
    assert "evidence" in reasoning

    assert (
        "High readiness"
        in reasoning["strengths"]
    )

    assert (
        "Performance improving"
        in reasoning["strengths"]
    )


def test_risk_detection():

    context = CoachContext(
        athlete_id=1,
    )

    context.training_load_intelligence = {
        "risk": "high",
    }

    context.recovery_intelligence = {
        "status": "poor",
    }

    context.memory_reasoning = {
        "injury_risk": "high",
    }

    context.race_intelligence = {
        "phase": "taper",
    }

    result = (
        CoachBrainService()
        .build_decision(
            context=context,
        )
    )

    risks = result["risks"]

    assert "High training load." in risks
    assert "Poor recovery." in risks
    assert "Elevated injury risk." in risks
    assert "Approaching race taper." in risks


def test_today_focus_defaults():

    context = CoachContext(
        athlete_id=1,
    )

    result = (
        CoachBrainService()
        .build_decision(
            context=context,
        )
    )

    assert (
        result["today_focus"]
        == "General Training"
    )
