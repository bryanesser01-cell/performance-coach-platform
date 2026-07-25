from abc import ABC, abstractmethod
from uuid import UUID

from .entities import Athlete


class AthleteRepository(ABC):
    """
    Repository interface for Athlete persistence.
    """

    @abstractmethod
    def get_by_id(self, athlete_id: UUID) -> Athlete | None:
        pass

    @abstractmethod
    def save(self, athlete: Athlete) -> Athlete:
        pass

    @abstractmethod
    def update(self, athlete: Athlete) -> Athlete:
        pass

    @abstractmethod
    def delete(self, athlete_id: UUID) -> None:
        pass
