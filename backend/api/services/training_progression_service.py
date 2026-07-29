from sqlalchemy.orm import Session

from database.repositories.training_progression_repository import (
    TrainingProgressionRepository,
)


def determine_training_focus(
    event: str,
) -> str:
    """
    Determine training focus by event.
    """

    event = event.lower()

    if event in [
        "800m",
        "1500m",
    ]:
        return "speed endurance"

    if event in [
        "3000m",
        "5k",
    ]:
        return "threshold endurance"

    if event in [
        "10k",
        "half marathon",
        "marathon",
    ]:
        return "aerobic endurance"

    return "general fitness"


def recommend_next_workout(
    event: str,
    goal_time: str | None = None,
    readiness_score: int = 80,
) -> dict:
    """
    Recommend next training session.

    Uses:
    - Event
    - Goal
    - Readiness
    """

    focus = determine_training_focus(
        event,
    )

    if readiness_score < 60:

        return {
            "session_type": "recovery",
            "workout": (
                "Easy recovery run"
            ),
            "purpose": (
                "Restore freshness before "
                "quality training"
            ),
        }

    if event.lower() == "1500m":

        return {
            "session_type": "interval",
            "workout": (
                "5 x 400m at race pace"
            ),
            "target_pace": (
                goal_time
                if goal_time
                else "controlled"
            ),
            "recovery": (
                "90 seconds jog"
            ),
            "purpose": (
                "Improve race pace tolerance"
            ),
            "focus": focus,
        }

    if event.lower() == "800m":

        return {
            "session_type": "speed endurance",
            "workout": (
                "6 x 200m fast relaxed"
            ),
            "recovery": (
                "200m jog"
            ),
            "purpose": (
                "Develop speed endurance"
            ),
            "focus": focus,
        }

    if event.lower() == "5k":

        return {
            "session_type": "threshold",
            "workout": (
                "3 x 2km threshold effort"
            ),
            "recovery": (
                "2 minutes recovery"
            ),
            "purpose": (
                "Improve aerobic capacity"
            ),
            "focus": focus,
        }

    return {
        "session_type": "easy",
        "workout": (
            "Easy aerobic run"
        ),
        "purpose": (
            "Build consistency"
        ),
        "focus": focus,
    }


def create_training_progression(
    db: Session,
    athlete_id: int,
    event: str,
    goal_time: str | None = None,
    readiness_score: int = 80,
):

    recommendation = recommend_next_workout(
        event=event,
        goal_time=goal_time,
        readiness_score=readiness_score,
    )

    repository = TrainingProgressionRepository(
        db,
    )

    return repository.create_progression(
        athlete_id=athlete_id,
        event=event,
        goal_time=goal_time,
        session_type=(
            recommendation["session_type"]
        ),
        workout_description=(
            recommendation["workout"]
        ),
        target_pace=(
            recommendation.get(
                "target_pace",
            )
        ),
        recovery=(
            recommendation.get(
                "recovery",
            )
        ),
        purpose=(
            recommendation.get(
                "purpose",
            )
        ),
    )
