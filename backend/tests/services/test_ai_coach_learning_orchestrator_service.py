from api.services.ai_coach_learning_orchestrator_service import (
    attach_learning_context,
    complete_coach_interaction,
    orchestrate_learning_after_response,
)


def test_orchestrate_learning_after_response():

    result = orchestrate_learning_after_response(
        athlete_id=1,
        question="Should I train today?",
        response={
            "decision": "REDUCE_TRAINING",
            "confidence": 90,
            "outcome": "positive",
        },
    )

    assert result["learning_updated"] is True


def test_attach_learning_context():

    result = attach_learning_context(
        response={
            "coach_message": ("Recover today."),
        },
        learning_response={
            "learning_updated": True,
            "learning_result": {
                "signal": "REINFORCE",
            },
        },
    )

    assert result["learning_context"]["learning_updated"] is True

    assert result["learning_context"]["learning_result"]["signal"] == "REINFORCE"


def test_complete_coach_interaction():

    result = complete_coach_interaction(
        athlete_id=1,
        question="Should I reduce training?",
        response={
            "decision": "REDUCE_TRAINING",
            "confidence": 85,
            "outcome": "positive",
        },
    )

    assert result["learning_context"]["learning_updated"] is True
