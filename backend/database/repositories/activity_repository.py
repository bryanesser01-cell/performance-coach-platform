from datetime import datetime

from sqlalchemy.orm import Session

from database.models import Activity
from database.repositories.base_repository import BaseRepository


class ActivityRepository(BaseRepository[Activity]):
    """
    Repository for athlete activity database operations.
    """

    def __init__(
        self,
        db: Session,
    ):
        super().__init__(
            db,
            Activity,
        )

    def bulk_create(
        self,
        activities: list[Activity],
    ) -> list[Activity]:
        """
        Create multiple activities in a single transaction.
        """

        if not activities:
            return []

        self.db.add_all(
            activities,
        )

        self.db.commit()

        for activity in activities:
            self.db.refresh(
                activity,
            )

        return activities

    def get_by_athlete_id(
        self,
        athlete_id: int,
    ) -> list[Activity]:
        """
        Retrieve all activities for an athlete.
        """

        return (
            self.db.query(
                Activity,
            )
            .filter(
                Activity.athlete_id == athlete_id,
            )
            .order_by(
                Activity.started_at.desc(),
            )
            .all()
        )

    def get_by_external_id(
        self,
        external_id: str,
    ) -> Activity | None:
        """
        Retrieve an activity by its external provider ID.

        Used to prevent duplicate imports from
        Garmin, Strava, Apple Health and COROS.
        """

        return (
            self.db.query(
                Activity,
            )
            .filter(
                Activity.external_id == external_id,
            )
            .first()
        )

    def exists(
        self,
        external_id: str,
    ) -> bool:
        """
        Check whether an activity already exists.
        """

        return (
            self.get_by_external_id(
                external_id,
            )
            is not None
        )

    def get_recent_activities(
        self,
        athlete_id: int,
        limit: int = 10,
    ) -> list[Activity]:
        """
        Retrieve the most recent activities for an athlete.
        """

        return (
            self.db.query(
                Activity,
            )
            .filter(
                Activity.athlete_id == athlete_id,
            )
            .order_by(
                Activity.started_at.desc(),
            )
            .limit(
                limit,
            )
            .all()
        )

    def get_last_n(
        self,
        athlete_id: int,
        limit: int,
    ) -> list[Activity]:
        """
        Retrieve the last N activities for an athlete.
        """

        return (
            self.db.query(
                Activity,
            )
            .filter(
                Activity.athlete_id == athlete_id,
            )
            .order_by(
                Activity.started_at.desc(),
            )
            .limit(
                limit,
            )
            .all()
        )

    def get_between_dates(
        self,
        athlete_id: int,
        start_date: datetime,
        end_date: datetime,
    ) -> list[Activity]:
        """
        Retrieve activities between two dates.
        """

        return (
            self.db.query(
                Activity,
            )
            .filter(
                Activity.athlete_id == athlete_id,
                Activity.started_at >= start_date,
                Activity.started_at <= end_date,
            )
            .order_by(
                Activity.started_at.desc(),
            )
            .all()
        )
