from datetime import datetime

from domain.activity.entities import Activity
from domain.activity.enums import ActivityCategory
from integrations.base import ActivityImporter
from integrations.models import ExternalActivityPayload


class GarminActivityImporter(ActivityImporter):
    """
    Converts Garmin activity data into the
    Performance Coach activity model.
    """

    def import_activity(
        self,
        payload: dict,
    ) -> Activity:
        external_activity = ExternalActivityPayload(
            source="garmin",
            external_id=payload.get("activity_id"),
            name=payload["activity_name"],
            category=ActivityCategory.RUNNING,
            started_at=datetime.fromisoformat(
                payload["start_time"],
            ),
            ended_at=(
                datetime.fromisoformat(
                    payload["end_time"],
                )
                if payload.get("end_time")
                else None
            ),
            distance=payload.get("distance"),
            duration=payload.get("duration"),
            average_hr=payload.get("average_hr"),
            max_hr=payload.get("max_hr"),
            cadence=payload.get("cadence"),
            elevation_gain=payload.get("elevation_gain"),
        )

        return Activity(
            athlete_id=payload["athlete_id"],
            category=external_activity.category,
            name=external_activity.name,
            started_at=external_activity.started_at,
            source=external_activity.source,
            external_id=external_activity.external_id,
            ended_at=external_activity.ended_at,
        )
