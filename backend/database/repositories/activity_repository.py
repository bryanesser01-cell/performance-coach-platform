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

    def create(
        self,
        activity: Activity,
    ) -> Activity:
        """
        Create a new activity.
        """

        self.db.add(activity)
        self.db.commit()
        self.db.refresh(activity)

        return activity

    def get_by_athlete_id(
        self,
        athlete_id: int,
    ) -> list[Activity]:
        """
        Retrieve all activities for an athlete.
        """

        return (
            self.db.query(Activity)
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
        Retrieve activity from an external provider ID.

        Used to prevent duplicate imports from:
        Garmin, Strava, COROS, etc.
        """

        return (
            self.db.query(Activity)
            .filter(
                Activity.external_id == external_id,
            )
            .first()
        )

    def get_recent_activities(
        self,
        athlete_id: int,
        limit: int = 10,
    ) -> list[Activity]:
        """
        Retrieve recent activities for an athlete.
        """

        return (
            self.db.query(Activity)
            .filter(
                Activity.athlete_id == athlete_id,
            )
            .order_by(
                Activity.started_at.desc(),
            )
            .limit(limit)
            .all()
        )
