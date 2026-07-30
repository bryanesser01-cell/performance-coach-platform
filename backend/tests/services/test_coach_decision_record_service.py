from api.services.coach_decision_record_service import (
    calculate_average_decision_confidence,
)


def test_average_decision_confidence():

    history = [
        {
            "decision": "REDUCE_TRAINING",
            "confidence": 80,
        },
        {
            "decision": "PROGRESS_TRAINING",
            "confidence": 60,
        },
    ]

    result = (
        calculate_average_decision_confidence(
            history,
        )
    )

    assert result == 70


def test_empty_history_confidence():

    result = (
        calculate_average_decision_confidence(
            []
        )
    )

    assert result == 0
