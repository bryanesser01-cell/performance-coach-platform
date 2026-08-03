from datetime import datetime

from domain.activity.entities import Activity
from domain.activity.enums import (
    ActivityCategory,
    ActivitySource,
)


class GarminActivityImporter:
    """
    Imports Garmin activities into the platform's
    domain Activity entity.
    """

    def import_activity(
        self,
        payload: dict,
    ) -> Activity:
        """
        Convert a Garmin payload into a domain Activity.
        """

        return Activity(
            athlete_id=payload["athlete_id"],
            external_id=payload["activity_id"],
            source=ActivitySource.GARMIN,
            category=ActivityCategory.RUNNING,
            name=payload["activity_name"],
            started_at=datetime.fromisoformat(
                payload["start_time"],
            ),
            ended_at=datetime.fromisoformat(
                payload["end_time"],
            ),
        )

    def get_activities(
        self,
        athlete_id,
    ) -> list[Activity]:
        """
        Placeholder until Garmin Connect integration
        is implemented.
        """

        return []
