from api.schemas.ai_coach_response_schema import (
    AICoachResponseSchema,
)


def test_ai_coach_response_defaults():

    response = AICoachResponseSchema(
        coach_message=(
            "Recover today."
        ),
    )

    assert (
        response.success
        is True
    )

    assert (
        response.memory_used
        is False
    )

    assert (
        response.learning_updated
        is False
    )


def test_ai_coach_response_full_payload():

    response = AICoachResponseSchema(
        athlete_id=1,
        question=(
            "Should I train today?"
        ),
        coach_message=(
            "Reduce training load."
        ),
        decision=(
            "REDUCE_TRAINING"
        ),
        recommendation=(
            "Easy recovery run."
        ),
        confidence=90,
        memory_used=True,
        learning_updated=True,
        strategy=(
            "RECOVERY_FIRST"
        ),
    )

    assert (
        response.athlete_id
        == 1
    )

    assert (
        response.decision
        == "REDUCE_TRAINING"
    )

    assert (
        response.confidence
        == 90
    )

    assert (
        response.memory_used
        is True
    )


def test_confidence_validation():

    response = AICoachResponseSchema(
        coach_message="Test",
        confidence=100,
    )

    assert (
        response.confidence
        == 100
    )
