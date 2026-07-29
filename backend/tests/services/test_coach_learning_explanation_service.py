from api.services.coach_learning_explanation_service import (
    build_athlete_friendly_message,
    build_learning_explanation,
)


def test_build_explanation_for_reduced_training():

    result = build_learning_explanation(
        decision="REDUCE_TRAINING",
        confidence=80,
        reason=(
            "Your readiness is low and "
            "previous recovery adjustments "
            "have worked well."
        ),
    )

    assert (
        result["decision"]
        == "REDUCE_TRAINING"
    )

    assert (
        result["confidence"]
        == 80
    )

    assert (
        "recovery"
        in result["explanation"]
    )


def test_build_explanation_for_progression():

    result = build_learning_explanation(
        decision="PROGRESS_TRAINING",
        confidence=75,
    )

    assert (
        "increased your training"
        in result["explanation"]
    )


def test_learning_history_is_included():

    result = build_learning_explanation(
        decision="REDUCE_TRAINING",
        confidence=85,
        learning_history={
            "previous_success": True,
        },
    )

    assert (
        "Previous athlete outcomes"
        in result["explanation"]
    )


def test_athlete_message_contains_confidence():

    explanation = {
        "decision": "REDUCE_TRAINING",
        "confidence": 85,
        "explanation": (
            "Recovery has been prioritised."
        ),
    }

    result = build_athlete_friendly_message(
        explanation,
    )

    assert (
        "85%"
        in result
    )
