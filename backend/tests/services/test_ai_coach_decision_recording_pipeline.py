from unittest.mock import Mock, patch

from api.services.ai_coach_conversation_service import (
    generate_coach_conversation_response,
)


def test_ai_coach_records_adaptive_decision():

    db = Mock()

    with patch(
        "api.services.ai_coach_conversation_service.generate_coach_decision_context",
        return_value={
            "coach_decision": {
                "decision": "REDUCE_TRAINING",
                "reason": (
                    "Recovery status requires adjustment."
                ),
            },
            "learning_confidence": 80,
        },
    ), patch(
        "api.services.ai_coach_conversation_service.generate_ai_coach_response",
        return_value={
            "coach_message": (
                "Take a recovery day."
            ),
        },
    ), patch(
        "api.services.ai_coach_conversation_service.record_coach_decision",
        return_value={
            "id": 1,
            "decision": "REDUCE_TRAINING",
        },
    ) as record_mock:

        result = (
            generate_coach_conversation_response(
                db=db,
                athlete_id=1,
                question=(
                    "Should I train today?"
                ),
                athlete_state={
                    "readiness": {
                        "score": 40,
                    }
                },
            )
        )

    assert (
        result["response"]
        is not None
    )

    assert (
        record_mock.called
        is True
    )


def test_ai_coach_decision_record_contains_confidence():

    db = Mock()

    with patch(
        "api.services.ai_coach_conversation_service.record_coach_decision",
        return_value={
            "id": 5,
            "confidence": 85,
        },
    ) as record_mock:

        record_mock(
            db=db,
            athlete_id=1,
            decision="PROGRESS_TRAINING",
            reason="Fitness improving",
            confidence=85,
        )

    args = record_mock.call_args.kwargs

    assert (
        args["decision"]
        == "PROGRESS_TRAINING"
    )

    assert (
        args["confidence"]
        == 85
    )
