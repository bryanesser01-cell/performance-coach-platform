from unittest.mock import Mock, patch

from api.services.coach_feedback_service import (
    analyse_feedback_sentiment,
    record_coach_feedback,
)


def test_positive_feedback_increases_confidence():

    db = Mock()

    with patch(
        "api.services.coach_feedback_service.record_learning_event",
        return_value={
            "confidence_change": 10,
        },
    ):

        result = record_coach_feedback(
            db=db,
            athlete_id=1,
            decision="REDUCE_TRAINING",
            feedback=(
                "The session worked "
                "and I feel better."
            ),
        )

    assert (
        result["outcome"]
        == "positive"
    )

    assert (
        result["confidence_change"]
        == 10
    )


def test_negative_feedback_reduces_confidence():

    db = Mock()

    with patch(
        "api.services.coach_feedback_service.record_learning_event",
        return_value={
            "confidence_change": -10,
        },
    ):

        result = record_coach_feedback(
            db=db,
            athlete_id=1,
            decision="PROGRESS_TRAINING",
            feedback=(
                "The workout was too hard "
                "and I struggled."
            ),
        )

    assert (
        result["outcome"]
        == "negative"
    )

    assert (
        result["confidence_change"]
        == -10
    )


def test_neutral_feedback():

    result = analyse_feedback_sentiment(
        "It was okay",
    )

    assert (
        result["sentiment"]
        == "neutral"
    )


def test_positive_sentiment():

    result = analyse_feedback_sentiment(
        "That was good",
    )

    assert (
        result["sentiment"]
        == "positive"
    )


def test_negative_sentiment():

    result = analyse_feedback_sentiment(
        "That was bad",
    )

    assert (
        result["sentiment"]
        == "negative"
    )
