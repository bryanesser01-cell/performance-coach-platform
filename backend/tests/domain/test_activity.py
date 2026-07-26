from datetime import UTC, datetime
from uuid import uuid4

from domain.activity.entities import Activity
from domain.activity.enums import (
    ActivityCategory,
    ActivitySource,
    ActivityStatus,
)


def test_create_activity():
    activity = Activity(
        athlete_id=uuid4(),
        category=ActivityCategory.RUNNING,
        name="Easy Run",
        started_at=datetime.now(UTC),
    )

    assert activity.name == "Easy Run"
    assert activity.category == ActivityCategory.RUNNING
    assert activity.status == ActivityStatus.PLANNED
    assert activity.source == ActivitySource.MANUAL
    assert activity.ended_at is None
