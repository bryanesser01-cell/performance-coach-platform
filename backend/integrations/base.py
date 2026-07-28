from abc import ABC, abstractmethod

from domain.activity.entities import Activity


class ActivityImporter(ABC):
    """
    Base interface for activity data importers.

    All external activity providers must convert
    their data into the internal Activity domain model.

    Examples:
    - Garmin
    - Strava
    - COROS
    - Apple Health
    - FIT files
    - GPX files
    - TCX files
    """

    @abstractmethod
    def import_activity(
        self,
        payload: dict,
    ) -> Activity:
        """
        Convert external activity payload
        into the internal Activity entity.

        Args:
            payload:
                Raw activity data from an external source.

        Returns:
            Activity domain entity.
        """

        raise NotImplementedError
