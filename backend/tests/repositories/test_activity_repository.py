from datetime import UTC, datetime, timedelta

from database.models import Activity
from database.repositories.activity_repository import ActivityRepository


def build_activity(
    athlete_id: int = 1,
    external_id: str = "garmin-1",
    started_at: datetime | None = None,
) -> Activity:
    """
    Build a test activity.
    """

    if started_at is None:
        started_at = datetime.now(
            UTC,
        )

    return Activity(
        athlete_id=athlete_id,
        source="garmin",
        external_id=external_id,
        category="Run",
        name="Morning Run",
        started_at=started_at,
        ended_at=started_at + timedelta(minutes=45),
        created_at=datetime.now(
            UTC,
        ),
    )


def test_create_activity(
    db_session,
):
    repository = ActivityRepository(
        db_session,
    )

    activity = build_activity()

    created = repository.create(
        activity,
    )

    assert created.id is not None


def test_bulk_create(
    db_session,
):
    repository = ActivityRepository(
        db_session,
    )

    activities = [
        build_activity(
            external_id="garmin-1",
        ),
        build_activity(
            external_id="garmin-2",
        ),
    ]

    created = repository.bulk_create(
        activities,
    )

    assert len(created) == 2


def test_get_by_athlete_id(
    db_session,
):
    repository = ActivityRepository(
        db_session,
    )

    repository.create(
        build_activity(
            athlete_id=1,
            external_id="a1",
        )
    )

    repository.create(
        build_activity(
            athlete_id=2,
            external_id="a2",
        )
    )

    activities = repository.get_by_athlete_id(
        1,
    )

    assert len(activities) == 1
    assert activities[0].athlete_id == 1


def test_get_by_external_id(
    db_session,
):
    repository = ActivityRepository(
        db_session,
    )

    repository.create(
        build_activity(
            external_id="garmin-123",
        )
    )

    activity = repository.get_by_external_id(
        "garmin-123",
    )

    assert activity is not None
    assert activity.external_id == "garmin-123"


def test_exists(
    db_session,
):
    repository = ActivityRepository(
        db_session,
    )

    repository.create(
        build_activity(
            external_id="exists-test",
        )
    )

    assert repository.exists(
        "exists-test",
    )

    assert not repository.exists(
        "does-not-exist",
    )


def test_get_recent_activities(
    db_session,
):
    repository = ActivityRepository(
        db_session,
    )

    base = datetime.now(
        UTC,
    )

    for i in range(5):
        repository.create(
            build_activity(
                external_id=f"recent-{i}",
                started_at=base + timedelta(days=i),
            )
        )

    activities = repository.get_recent_activities(
        athlete_id=1,
        limit=3,
    )

    assert len(activities) == 3


def test_get_last_n(
    db_session,
):
    repository = ActivityRepository(
        db_session,
    )

    base = datetime.now(
        UTC,
    )

    for i in range(10):
        repository.create(
            build_activity(
                external_id=f"last-{i}",
                started_at=base + timedelta(days=i),
            )
        )

    activities = repository.get_last_n(
        athlete_id=1,
        limit=5,
    )

    assert len(activities) == 5


def test_get_between_dates(
    db_session,
):
    repository = ActivityRepository(
        db_session,
    )

    now = datetime.now(
        UTC,
    )

    repository.create(
        build_activity(
            external_id="before",
            started_at=now - timedelta(days=10),
        )
    )

    repository.create(
        build_activity(
            external_id="inside",
            started_at=now,
        )
    )

    repository.create(
        build_activity(
            external_id="after",
            started_at=now + timedelta(days=10),
        )
    )

    activities = repository.get_between_dates(
        athlete_id=1,
        start_date=now - timedelta(days=1),
        end_date=now + timedelta(days=1),
    )

    assert len(activities) == 1
    assert activities[0].external_id == "inside"
