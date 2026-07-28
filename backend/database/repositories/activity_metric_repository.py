from sqlalchemy.orm import Session

from database.activity_models import ActivityMetric
from database.models import Activity
from database.repositories.base_repository import BaseRepository


class ActivityMetricRepository(BaseRepository[ActivityMetric]):
    """
    Repository for activity metric database operations.
    """

    def __init__(
        self,
        db: Session,
    ):
        super().__init__(
            db,
            ActivityMetric,
        )

    def create_metric(
        self,
        metric: ActivityMetric,
    ) -> ActivityMetric:
        """
        Create activity metric.
        """

        self.db.add(metric)
        self.db.commit()
        self.db.refresh(metric)

        return metric

    def get_by_activity_id(
        self,
        activity_id: int,
    ) -> ActivityMetric | None:
        """
        Retrieve metrics by activity.
        """

        return (
            self.db.query(ActivityMetric)
            .filter(
                ActivityMetric.activity_id == activity_id,
            )
            .first()
        )

    def get_by_athlete_id(
        self,
        athlete_id: int,
    ) -> list[ActivityMetric]:
        """
        Retrieve activity metrics for an athlete.
        """

        return (
            self.db.query(ActivityMetric)
            .join(
                Activity,
                ActivityMetric.activity_id == Activity.id,
            )
            .filter(
                Activity.athlete_id == athlete_id,
            )
            .all()
        )

    def get_recent_metrics(
        self,
        limit: int = 10,
    ) -> list[ActivityMetric]:
        """
        Retrieve recent activity metrics.
        """

        return (
            self.db.query(ActivityMetric)
            .order_by(
                ActivityMetric.id.desc(),
            )
            .limit(limit)
            .all()
        )
