from api.services.coach_decision_engine_service import (
    evaluate_training_state,
    generate_coach_decision,
    generate_decision_explanation,
    select_coach_action,
)


def test_low_readiness_reduces_training():

    result = evaluate_training_state(
        readiness_score=30,
        training_stress=200,
        fitness_trend="stable",
    )

    assert (
        result["decision"]
        == "REDUCE_TRAINING"
    )


def test_improving_fitness_progresses_training():

    result = evaluate_training_state(
        readiness_score=85,
        training_stress=100,
        fitness_trend="improving",
    )

    assert (
        result["decision"]
        == "PROGRESS_TRAINING"
    )


def test_select_coach_action():

    result = select_coach_action(
        {
            "decision": "REDUCE_TRAINING",
        }
    )

    assert (
        "recovery"
        in result["action"].lower()
    )


def test_generate_explanation():

    result = generate_decision_explanation(
        {
            "decision": "MAINTAIN_TRAINING",
            "reason": "training is balanced",
        }
    )

    assert (
        "MAINTAIN_TRAINING"
        in result["explanation"]
    )


def test_full_coach_decision():

    result = generate_coach_decision(
        readiness_score=80,
        training_stress=100,
        fitness_trend="improving",
        learning_confidence=75,
    )

    assert (
        result["decision"]
        == "PROGRESS_TRAINING"
    )

    assert (
        result["learning_confidence"]
        == 75
    )
