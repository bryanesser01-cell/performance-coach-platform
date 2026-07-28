from sqlalchemy.orm import Session

from database.models import Activity
from database.repositories.activity_repository import (
    ActivityRepository,
)
from integrations.base import ActivityImporter


def ingest_activity(
    db: Session,
    importer: ActivityImporter,
    payload: dict,
) -> Activity:
    """
    Import an external activity and persist it.

    Supports:
    - Garmin
    - Strava
    - COROS
    - Apple Health
    - FIT / GPX / TCX
    """

    repository = ActivityRepository(db)

    external_id = payload.get(
        "activity_id",
    )

    if external_id:
        existing_activity = repository.get_by_external_id(
            external_id,
        )

        if existing_activity:
            return existing_activity

    activity = importer.import_activity(
        payload,
    )

    db_activity = Activity(
        athlete_id=activity.athlete_id,
        source=activity.source.value,
        external_id=activity.external_id,
        category=activity.category.value,
        name=activity.name,
        started_at=activity.started_at,
        ended_at=activity.ended_at,
    )

    return repository.create(
        db_activity,
    )
