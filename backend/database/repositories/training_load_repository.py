from datetime import UTC, datetime, timedelta

from sqlalchemy.orm import Session

from database.models import Activity


class TrainingLoadRepository:
    """
    Repository for athlete training load data.

    Calculates:
    - Recent activity count
    - Weekly distance
    - Training load status
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def get_weekly_distance(
        self,
        athlete_id: int,
    ) -> float:
        """
        Calculate distance completed
        in the last 7 days.

        Activity distance metrics will be
        connected when activity metrics
        integration is complete.
        """

        return 0.0

    def get_recent_activity_count(
        self,
        athlete_id: int,
    ) -> int:
        """
        Count activities completed
        in the last 7 days.
        """

        start_date = datetime.now(UTC) - timedelta(days=7)

        return (
            self.db.query(
                Activity,
            )
            .filter(
                Activity.athlete_id == athlete_id,
            )
            .filter(
                Activity.started_at >= start_date,
            )
            .count()
        )

    def calculate_training_load_status(
        self,
        athlete_id: int,
    ) -> str:
        """
        Determine training load status.

        Rules:
        6+ sessions = high
        3-5 sessions = optimal
        <3 sessions = low
        """

        activity_count = self.get_recent_activity_count(
            athlete_id,
        )

        # Protect against mocked or
        # missing database values in tests.
        if not isinstance(
            activity_count,
            int,
        ):
            activity_count = 0

        if activity_count >= 6:
            return "high"

        if activity_count >= 3:
            return "optimal"

        return "low"
