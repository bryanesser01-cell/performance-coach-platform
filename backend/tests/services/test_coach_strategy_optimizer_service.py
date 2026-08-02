from api.services.coach_strategy_optimizer_service import (
    calculate_strategy_confidence,
    generate_strategy_optimisation_report,
    optimise_future_decision,
    select_best_coaching_strategy,
)


def test_calculate_strategy_confidence():

    result = calculate_strategy_confidence(
        success_rate=80,
        learning_confidence=70,
    )

    assert result == 75


def test_select_best_strategy():

    analysis = {
        "REDUCE_TRAINING": {
            "success_rate": 85,
        },
        "PROGRESS_TRAINING": {
            "success_rate": 60,
        },
    }

    result = select_best_coaching_strategy(
        analysis,
    )

    assert result["decision"] == "REDUCE_TRAINING"

    assert result["success_rate"] == 85


def test_optimise_future_decision():

    analysis = {
        "REDUCE_TRAINING": {
            "success_rate": 90,
        },
        "PROGRESS_TRAINING": {
            "success_rate": 50,
        },
    }

    result = optimise_future_decision(
        proposed_decision="PROGRESS_TRAINING",
        decision_analysis=analysis,
        learning_confidence=70,
    )

    assert result["recommended_decision"] == "REDUCE_TRAINING"

    assert result["confidence"] == 80


def test_generate_strategy_report():

    analysis = {
        "REDUCE_TRAINING": {
            "success_rate": 90,
        },
    }

    result = generate_strategy_optimisation_report(
        analysis,
    )

    assert result["best_strategy"] == "REDUCE_TRAINING"

    assert result["success_rate"] == 90
