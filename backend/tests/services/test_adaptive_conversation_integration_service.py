from api.services.adaptive_conversation_integration_service import (
    build_adaptive_conversation_context,
    generate_adaptive_coach_message,
    generate_adaptive_conversation_response,
    integrate_learning_into_response,
)


def test_build_adaptive_conversation_context():

    result = build_adaptive_conversation_context(
        {
            "summary": {
                "readiness_score": 80,
                "training_stress": 100,
                "fitness_trend": "improving",
                "learning_confidence": 70,
            }
        },
        {
            "confidence_adjustment": 10,
        },
    )

    assert "adaptive_decision" in result


def test_generate_adaptive_coach_message():

    result = generate_adaptive_coach_message(
        {
            "adaptive_decision": {
                "message": ("Continue progressive training."),
            }
        }
    )

    assert "Continue" in result


def test_integrate_learning_into_response():

    result = integrate_learning_into_response(
        {
            "message": "Train easy today.",
        },
        {
            "confidence_adjustment": 25,
        },
    )

    assert result["learning_confidence"] == 25


def test_full_adaptive_conversation():

    result = generate_adaptive_conversation_response(
        {
            "summary": {
                "readiness_score": 30,
                "training_stress": 600,
                "fitness_trend": "stable",
                "learning_confidence": 60,
            }
        },
        {
            "confidence_adjustment": 10,
        },
    )

    assert "message" in result

    assert result["learning_confidence"] == 10
