from database.models import Activity
from integrations.garmin.garmin_models import GarminActivity


class GarminMapper:
    """
    Maps Garmin activities into the platform's
    internal Activity database model.
    """

    @staticmethod
    def to_activity(
        activity: GarminActivity,
    ) -> Activity:
        """
        Convert a GarminActivity into an Activity.
        """

        return Activity(
            athlete_id=activity.athlete_id,
            source=activity.source,
            external_id=activity.external_id,
            category=activity.activity_type,
            name=activity.name,
            started_at=activity.started_at,
            ended_at=activity.ended_at,
            created_at=activity.started_at,
        )
