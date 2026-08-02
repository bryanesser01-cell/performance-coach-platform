from sqlalchemy.orm import Session

from database.repositories.athlete_checkin_repository import (
    AthleteCheckinRepository,
)
from database.repositories.athlete_state_repository import (
    AthleteStateRepository,
)
from database.repositories.performance_trend_repository import (
    PerformanceTrendRepository,
)
from database.repositories.training_load_repository import (
    TrainingLoadRepository,
)


def calculate_readiness_score(
    sleep_score: int,
    soreness_score: int,
    energy_score: int,
    motivation_score: int,
) -> int:
    """
    Calculate athlete readiness score.

    Sleep        25%
    Soreness     25%
    Energy       25%
    Motivation   25%
    """

    soreness_adjusted = 10 - soreness_score

    score = (
        (sleep_score * 10)
        + (soreness_adjusted * 10)
        + (energy_score * 10)
        + (motivation_score * 10)
    ) / 4

    return int(score)


def get_readiness_status(
    readiness_score: int,
) -> str:
    """
    Convert readiness score into status.
    """

    if readiness_score >= 80:
        return "ready"

    if readiness_score >= 60:
        return "moderate"

    return "recovery"


def build_athlete_state(
    athlete: dict,
    goal: dict | None = None,
    readiness: dict | None = None,
    training: dict | None = None,
    performance: dict | None = None,
    training_sessions: list | None = None,
    next_race: dict | None = None,
    metadata: dict | None = None,
) -> dict:
    """
    Build complete athlete state.
    """

    return {
        "athlete": {
            "id": athlete.get(
                "id",
            ),
            "name": athlete.get(
                "name",
                "Athlete",
            ),
            "sport": athlete.get(
                "sport",
                "running",
            ),
            "primary_event": athlete.get(
                "primary_event",
                "5K",
            ),
        },
        "goal": {
            "target": (goal.get("target") if goal else None),
            "status": (goal.get("status") if goal else None),
        },
        "readiness": {
            "score": (readiness.get("score") if readiness else 0),
            "status": (readiness.get("status") if readiness else "unknown"),
        },
        "training": {
            "load_status": (training.get("load_status") if training else "unknown"),
            "weekly_distance": (training.get("weekly_distance") if training else 0),
        },
        "performance": {
            "trend": (performance.get("trend") if performance else "unknown"),
            "current_metric": (
                performance.get("current_metric") if performance else None
            ),
        },
        "training_sessions": (training_sessions if training_sessions else []),
        "next_race": (next_race if next_race else None),
        "metadata": (metadata if metadata else {}),
    }


def get_athlete_state(
    db: Session,
    athlete_id: int,
) -> dict:
    """
    Retrieve complete athlete state.

    Sources:
    - Athlete profile
    - Goals
    - Daily check-ins
    - Training load
    - Performance trend
    """

    athlete_repository = AthleteStateRepository(
        db,
    )

    checkin_repository = AthleteCheckinRepository(
        db,
    )

    training_repository = TrainingLoadRepository(
        db,
    )

    performance_repository = PerformanceTrendRepository(
        db,
    )

    athlete = athlete_repository.get_athlete(
        athlete_id,
    )

    goal = athlete_repository.get_active_goal(
        athlete_id,
    )

    checkin = checkin_repository.get_latest_by_athlete_id(
        athlete_id,
    )

    if (
        checkin
        and isinstance(checkin.sleep_score, int)
        and isinstance(checkin.soreness_score, int)
        and isinstance(checkin.energy_score, int)
        and isinstance(checkin.motivation_score, int)
    ):

        readiness_score = calculate_readiness_score(
            sleep_score=checkin.sleep_score,
            soreness_score=checkin.soreness_score,
            energy_score=checkin.energy_score,
            motivation_score=checkin.motivation_score,
        )

        readiness_status = get_readiness_status(
            readiness_score,
        )

    else:

        readiness_score = 0
        readiness_status = "unknown"

    training_load_status = training_repository.calculate_training_load_status(
        athlete_id,
    )

    weekly_distance = training_repository.get_weekly_distance(
        athlete_id,
    )

    performance_trend = performance_repository.calculate_performance_trend(
        athlete_id,
    )

    current_metric = performance_repository.get_current_performance_metric(
        athlete_id,
    )

    #
    # Future AI Coach datasets
    #
    training_sessions = []

    next_race = None

    metadata = {
        "state_version": 2,
    }

    return build_athlete_state(
        athlete=(
            {
                "id": athlete.id,
                "name": athlete.name,
                "sport": athlete.sport,
                "primary_event": athlete.primary_event,
            }
            if athlete
            else {}
        ),
        goal=(
            {
                "target": goal.goal_type,
                "status": goal.status,
            }
            if goal
            else None
        ),
        readiness={
            "score": readiness_score,
            "status": readiness_status,
        },
        training={
            "load_status": training_load_status,
            "weekly_distance": weekly_distance,
        },
        performance={
            "trend": performance_trend,
            "current_metric": current_metric,
        },
        training_sessions=training_sessions,
        next_race=next_race,
        metadata=metadata,
    )


def generate_athlete_state_summary(
    athlete_state: dict,
) -> str:
    """
    Generate human readable athlete summary.
    """

    athlete = athlete_state["athlete"]
    readiness = athlete_state["readiness"]
    training = athlete_state["training"]
    performance = athlete_state["performance"]

    return (
        f"{athlete['name']} is training for "
        f"{athlete['primary_event']}. "
        f"Readiness score is "
        f"{readiness['score']} "
        f"({readiness['status']}). "
        f"Training load is "
        f"{training['load_status']}. "
        f"Performance trend is "
        f"{performance['trend']}."
    )
