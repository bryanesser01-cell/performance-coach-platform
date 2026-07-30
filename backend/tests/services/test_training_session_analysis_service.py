from unittest.mock import Mock, patch

from api.services.training_session_analysis_service import (
    analyse_training_outcome,
    generate_session_learning_event,
    recommend_next_adjustment,
)
from database.training_models import TrainingSession


def create_session(
    notes: str,
):
    return TrainingSession(
        id=1,
        athlete_id=1,
        session_type="tempo",
        focus="threshold",
        status="completed",
        notes=notes,
    )


def test_positive_training_outcome():

    session = create_session(
        "Felt strong and comfortable",
    )

    result = analyse_training_outcome(
        session,
    )

    assert (
        result["outcome"]
        == "positive"
    )


def test_negative_training_outcome():

    session = create_session(
        "Struggled and felt tired",
    )

    result = analyse_training_outcome(
        session,
    )

    assert (
        result["outcome"]
        == "negative"
    )


def test_learning_event_created():

    db = Mock()

    session = create_session(
        "Great session",
    )

    with patch(
        "api.services.training_session_analysis_service.record_learning_event",
        return_value={
            "confidence_change": 10,
        },
    ):

        result = generate_session_learning_event(
            db=db,
            athlete_id=1,
            session=session,
            decision="PROGRESS_TRAINING",
        )

    assert (
        result["analysis"]["outcome"]
        == "positive"
    )


def test_recommendation_positive():

    session = create_session(
        "Easy and strong",
    )

    result = recommend_next_adjustment(
        session,
    )

    assert (
        "progression"
        in result["recommendation"]
    )
