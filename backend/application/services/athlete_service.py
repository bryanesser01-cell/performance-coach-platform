from uuid import UUID

from domain.athlete.entities import Athlete
from domain.athlete.repository import AthleteRepository
from domain.athlete.exceptions import AthleteNotFound


class AthleteService:
    """
    Application service containing Athlete use cases.
    """

    def __init__(self, repository: AthleteRepository):
        self.repository = repository

    def get_athlete(self, athlete_id: UUID) -> Athlete:
        athlete = self.repository.get_by_id(athlete_id)

        if athlete is None:
            raise AthleteNotFound(f"Athlete with ID '{athlete_id}' was not found.")

        return athlete

    def create_athlete(self, athlete: Athlete) -> Athlete:
        return self.repository.save(athlete)

    def update_athlete(self, athlete: Athlete) -> Athlete:
        return self.repository.update(athlete)

    def delete_athlete(self, athlete_id: UUID) -> None:
        self.repository.delete(athlete_id)
