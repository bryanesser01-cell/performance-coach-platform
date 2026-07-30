from api.services.adaptive_coaching_engine_service import (
    apply_learning_adjustment,
    build_adaptive_training_decision,
    generate_adaptive_coaching_response,
    run_adaptive_coaching_engine,
)


def test_build_adaptive_training_decision():

    result = build_adaptive_training_decision(
        {
            "summary": {
                "readiness_score": 85,
                "training_stress": 100,
                "fitness_trend": "improving",
                "learning_confidence": 70,
            }
        }
    )

    assert (
        result["decision"]
        == "PROGRESS_TRAINING"
    )


def test_learning_adjustment():

    result = apply_learning_adjustment(
        {
            "learning_confidence": 50,
        },
        {
            "confidence_adjustment": 20,
        },
    )

    assert (
        result["learning_confidence"]
        == 70
    )


def test_generate_adaptive_response():

    result = generate_adaptive_coaching_response(
        {
            "decision": "REDUCE_TRAINING",
            "action": "Take a recovery day.",
            "learning_confidence": 80,
            "explanation": "Recovery is needed.",
        }
    )

    assert (
        result["decision"]
        == "REDUCE_TRAINING"
    )

    assert (
        result["confidence"]
        == 80
    )


def test_full_adaptive_engine():

    result = run_adaptive_coaching_engine(
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

    assert (
        result["decision"]
        == "REDUCE_TRAINING"
    )

    assert (
        result["confidence"]
        == 70
    )
