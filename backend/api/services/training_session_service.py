from datetime import datetime

from sqlalchemy.orm import Session

from database.training_models import TrainingSession


def create_training_session(
    db: Session,
    athlete_id: int,
    session_date: datetime,
    session_type: str,
    focus: str,
    notes: str | None = None,
) -> dict:
    """
    Create a planned training session.

    Examples:
    - Interval session
    - Tempo run
    - Long run
    - Recovery run
    """

    session = TrainingSession(
        athlete_id=athlete_id,
        session_date=session_date,
        session_type=session_type,
        focus=focus,
        status="planned",
        notes=notes,
    )

    db.add(
        session,
    )

    db.commit()

    db.refresh(
        session,
    )

    return {
        "id": session.id,
        "athlete_id": session.athlete_id,
        "session_type": session.session_type,
        "focus": session.focus,
        "status": session.status,
        "notes": session.notes,
    }


def complete_training_session(
    db: Session,
    session_id: int,
    notes: str | None = None,
) -> dict:
    """
    Mark a training session as completed.
    """

    session = (
        db.query(TrainingSession)
        .filter(
            TrainingSession.id == session_id,
        )
        .first()
    )

    if session is None:
        return {
            "error": "Training session not found",
        }

    session.status = "completed"

    if notes is not None:
        session.notes = notes

    db.commit()

    db.refresh(
        session,
    )

    return {
        "id": session.id,
        "athlete_id": session.athlete_id,
        "status": session.status,
        "notes": session.notes,
    }


def get_upcoming_sessions(
    db: Session,
    athlete_id: int,
) -> list[TrainingSession]:
    """
    Retrieve planned upcoming sessions
    for an athlete.
    """

    return (
        db.query(TrainingSession)
        .filter(
            TrainingSession.athlete_id == athlete_id,
            TrainingSession.status == "planned",
        )
        .order_by(
            TrainingSession.session_date,
        )
        .all()
    )


def get_completed_sessions(
    db: Session,
    athlete_id: int,
) -> list[TrainingSession]:
    """
    Retrieve completed sessions
    for an athlete.
    """

    return (
        db.query(TrainingSession)
        .filter(
            TrainingSession.athlete_id == athlete_id,
            TrainingSession.status == "completed",
        )
        .order_by(
            TrainingSession.session_date.desc(),
        )
        .all()
    )


def analyse_completed_session(
    session: TrainingSession,
) -> dict:
    """
    Analyse a completed training session.

    Future enhancements:
    - Garmin metrics
    - Training load
    - Recovery score
    - Performance trend
    - AI learning feedback
    """

    return {
        "session_id": session.id,
        "session_type": session.session_type,
        "focus": session.focus,
        "status": session.status,
        "recommendation": ("Review recovery before the next session."),
    }
