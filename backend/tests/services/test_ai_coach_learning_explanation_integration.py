from unittest.mock import Mock

from api.services.ai_coach_conversation_service import (
    generate_coach_conversation_response,
)


def test_ai_coach_adaptive_response_uses_learning_explanation():

    db = Mock()

    athlete_state = {
        "readiness": {
            "score": 50,
        },
        "training": {
            "load_status": "high",
        },
        "performance": {
            "trend": "stable",
        },
    }

    result = generate_coach_conversation_response(
        db=db,
        athlete_id=1,
        question="Why did you reduce my training?",
        athlete_state=athlete_state,
    )

    assert result["intent"] == "adaptive_coaching"

    assert result["answer"] is not None

    assert "training" in result["answer"].lower()


def test_ai_coach_adaptive_response_contains_decision_context():

    db = Mock()

    athlete_state = {
        "readiness": {
            "score": 45,
        },
        "training": {
            "load_status": "high",
        },
        "performance": {
            "trend": "stable",
        },
    }

    result = generate_coach_conversation_response(
        db=db,
        athlete_id=2,
        question="Why did you reduce my training?",
        athlete_state=athlete_state,
    )

    assert result["coach_decision_context"] is not None

    assert (
        result["coach_decision_context"]["coach_decision"]["decision"]
        == "REDUCE_TRAINING"
    )
