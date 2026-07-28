from sqlalchemy.orm import Session

from api.services.athlete_performance_report_service import (
    generate_athlete_performance_report,
)


def generate_fitness_summary(
    db: Session,
    athlete_id: int,
) -> dict:
    """
    Generate athlete fitness summary.
    """

    report = generate_athlete_performance_report(
        db,
        athlete_id,
    )

    return {
        "athlete_id": athlete_id,
        "fitness_status": report.get(
            "fitness_status",
            "unknown",
        ),
        "race_readiness": report.get(
            "race_readiness",
            {},
        ),
    }


def generate_training_status(
    db: Session,
    athlete_id: int,
) -> dict:
    """
    Generate current training status.
    """

    report = generate_athlete_performance_report(
        db,
        athlete_id,
    )

    coach_insights = report.get(
        "coach_insights",
        {},
    )

    return {
        "athlete_id": athlete_id,
        "status": coach_insights.get(
            "status",
            "unknown",
        ),
        "recommendations": coach_insights.get(
            "recommendations",
            [],
        ),
    }


def generate_race_readiness(
    db: Session,
    athlete_id: int,
) -> dict:
    """
    Generate race readiness dashboard data.
    """

    report = generate_athlete_performance_report(
        db,
        athlete_id,
    )

    return {
        "athlete_id": athlete_id,
        "race_readiness": report.get(
            "race_readiness",
            {},
        ),
    }


def generate_prediction(
    db: Session,
    athlete_id: int,
) -> dict:
    """
    Generate race prediction dashboard data.
    """

    report = generate_athlete_performance_report(
        db,
        athlete_id,
    )

    return {
        "athlete_id": athlete_id,
        "race_prediction": report.get(
            "race_prediction",
            {},
        ),
    }
