from api.services.coach_decision_analytics_service import (
    analyse_decision_history,
    calculate_decision_success_rate,
    generate_coach_performance_report,
)


def test_calculate_decision_success_rate():

    result = calculate_decision_success_rate(
        [
            "positive",
            "positive",
            "negative",
            "positive",
        ]
    )

    assert result == 75


def test_analyse_decision_history():

    history = [
        {
            "decision": "REDUCE_TRAINING",
            "outcome": "positive",
        },
        {
            "decision": "REDUCE_TRAINING",
            "outcome": "positive",
        },
        {
            "decision": "REDUCE_TRAINING",
            "outcome": "negative",
        },
        {
            "decision": "PROGRESS_TRAINING",
            "outcome": "positive",
        },
    ]

    result = analyse_decision_history(
        history,
    )

    assert (
        result[
            "REDUCE_TRAINING"
        ]["times_used"]
        == 3
    )

    assert (
        result[
            "REDUCE_TRAINING"
        ]["success_rate"]
        == 66
    )


def test_generate_coach_performance_report():

    history = [
        {
            "decision": "REDUCE_TRAINING",
            "outcome": "positive",
        },
        {
            "decision": "PROGRESS_TRAINING",
            "outcome": "positive",
        },
    ]

    result = generate_coach_performance_report(
        history,
    )

    assert (
        result["total_decisions"]
        == 2
    )

    assert (
        result["overall_success_rate"]
        == 100
    )
