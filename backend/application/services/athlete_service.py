from uuid import UUID

from domain.athlete.entities import Athlete
from domain.athlete.exceptions import AthleteNotFound
from domain.athlete.repository import AthleteRepository


class AthleteService:
    """
    Application service containing Athlete use cases.
    """

    def __init__(self, repository: AthleteRepository):
        self._repository = repository

    def get_athlete(self, athlete_id: UUID) -> Athlete:
        athlete = self._repository.get_by_id(athlete_id)

        if athlete is None:
            raise AthleteNotFound(f"Athlete with ID '{athlete_id}' was not found.")

        return athlete

    def create_athlete(self, athlete: Athlete) -> Athlete:
        return self._repository.save(athlete)

    def update_athlete(self, athlete: Athlete) -> Athlete:
        return self._repository.update(athlete)

    def delete_athlete(self, athlete_id: UUID) -> None:
        self._repository.delete(athlete_id)
