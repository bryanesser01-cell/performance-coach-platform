from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from .entities import Activity


class ActivityRepository(ABC):
    """
    Repository interface for Activity entities.
    """

    @abstractmethod
    def save(self, activity: Activity) -> Activity:
        """
        Persist an activity and return the saved entity.
        """
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, activity_id: UUID) -> Activity | None:
        """
        Retrieve an activity by its unique identifier.
        """
        raise NotImplementedError

    @abstractmethod
    def list_by_athlete(self, athlete_id: UUID) -> list[Activity]:
        """
        Return all activities belonging to an athlete.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, activity_id: UUID) -> None:
        """
        Delete an activity.
        """
        raise NotImplementedError