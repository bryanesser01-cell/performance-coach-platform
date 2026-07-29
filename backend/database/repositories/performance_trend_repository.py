from datetime import UTC, datetime, timedelta

from sqlalchemy.orm import Session

from database.models import Activity


class PerformanceTrendRepository:
    """
    Repository for athlete performance trends.

    Analyses recent activity history to determine:
    - Improving
    - Stable
    - Declining
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def get_recent_activities(
        self,
        athlete_id: int,
        days: int = 30,
    ) -> list[Activity]:
        """
        Retrieve recent athlete activities.
        """

        start_date = (
            datetime.now(UTC)
            - timedelta(days=days)
        )

        activities = (
            self.db.query(
                Activity,
            )
            .filter(
                Activity.athlete_id
                == athlete_id,
            )
            .filter(
                Activity.started_at >= start_date,
            )
            .order_by(
                Activity.started_at.asc(),
            )
            .all()
        )

        if not isinstance(
            activities,
            list,
        ):
            return []

        return activities

    def calculate_performance_trend(
        self,
        athlete_id: int,
    ) -> str:
        """
        Determine athlete performance trend.

        Placeholder logic until activity
        metrics are connected.

        Future:
        - pace changes
        - race times
        - training consistency
        """

        activities = self.get_recent_activities(
            athlete_id,
        )

        activity_count = len(
            activities,
        )

        if activity_count >= 8:
            return "improving"

        if activity_count >= 3:
            return "stable"

        return "unknown"

    def get_current_performance_metric(
        self,
        athlete_id: int,
    ):
        """
        Retrieve latest performance metric.

        Future:
        Connect to:
        - activity metrics
        - race prediction
        - pace analysis
        """

        return None
