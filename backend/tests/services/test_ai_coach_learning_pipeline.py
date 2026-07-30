from unittest.mock import Mock, patch

from api.services.ai_coach_conversation_service import (
    generate_coach_conversation_response,
)


def test_ai_coach_creates_learning_context():

    db = Mock()

    with patch(
        "api.services.ai_coach_conversation_service.build_training_memory",
        return_value={
            "sessions": 10,
        },
    ), patch(
        "api.services.ai_coach_conversation_service.get_learning_context",
        return_value={
            "confidence_adjustment": 20,
            "learning_events": [],
        },
    ), patch(
        "api.services.ai_coach_conversation_service.generate_ai_coach_response",
        return_value={
            "coach_message": (
                "Take an easy recovery run."
            ),
        },
    ):

        result = (
            generate_coach_conversation_response(
                db=db,
                athlete_id=1,
                question=(
                    "Should I train today?"
                ),
            )
        )

    assert (
        "learning_memory"
        in result
    )

    assert (
        result["learning_memory"]
        ["confidence_adjustment"]
        == 20
    )


def test_ai_coach_context_contains_decision_context():

    db = Mock()

    with patch(
        "api.services.ai_coach_conversation_service.generate_coach_decision_context",
        return_value={
            "coach_decision": {
                "decision": (
                    "REDUCE_TRAINING"
                ),
            }
        },
    ), patch(
        "api.services.ai_coach_conversation_service.generate_ai_coach_response",
        return_value={
            "coach_message": "Recover today.",
        },
    ):

        result = (
            generate_coach_conversation_response(
                db=db,
                athlete_id=1,
                question=(
                    "Should I train today?"
                ),
            )
        )

    assert (
        result["coach_decision_context"]
        ["coach_decision"]
        ["decision"]
        == "REDUCE_TRAINING"
    )


def test_learning_pipeline_returns_response():

    db = Mock()

    with patch(
        "api.services.ai_coach_conversation_service.generate_ai_coach_response",
        return_value={
            "coach_message": (
                "Keep progressing."
            ),
        },
    ):

        result = (
            generate_coach_conversation_response(
                db=db,
                athlete_id=5,
                question=(
                    "How should I train?"
                ),
            )
        )

    assert (
        result["response"]
        is not None
    )

    assert (
        result["answer"]
        is not None
    )
