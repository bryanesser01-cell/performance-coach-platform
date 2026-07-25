from core.exceptions import (
    ForbiddenError,
    ResourceNotFoundError,
)
from database.athlete_models import Athlete
from repositories.athlete_repository import AthleteRepository
from schemas.athlete_schema import (
    AthleteCreate,
    AthleteUpdate,
)


class AthleteService:
    """
    Service responsible for Athlete business logic.
    """

    def __init__(
        self,
        repository: AthleteRepository,
    ):
        self.repository = repository

    def create(
        self,
        user_id: int,
        athlete: AthleteCreate,
    ) -> Athlete:
        """
        Create a new athlete.
        """
        db_athlete = Athlete(
            user_id=user_id,
            **athlete.model_dump(exclude_none=True),
        )

        return self.repository.create(
            db_athlete,
        )

    def get_all(
        self,
        user_id: int,
    ) -> list[Athlete]:
        """
        Retrieve all athletes belonging to the user.
        """
        return self.repository.get_by_user(
            user_id,
        )

    def get(
        self,
        athlete_id: int,
        user_id: int,
    ) -> Athlete:
        """
        Retrieve an athlete owned by the user.
        """
        athlete = self.repository.get_by_id(
            athlete_id,
        )

        if athlete is None:
            raise ResourceNotFoundError("Athlete not found.")

        if athlete.user_id != user_id:
            raise ForbiddenError("Not authorized.")

        return athlete

    def update(
        self,
        athlete_id: int,
        user_id: int,
        updates: AthleteUpdate,
    ) -> Athlete:
        """
        Update an athlete.
        """
        athlete = self.get(
            athlete_id,
            user_id,
        )

        return self.repository.update(
            athlete,
            updates.model_dump(
                exclude_unset=True,
                exclude_none=True,
            ),
        )

    def delete(
        self,
        athlete_id: int,
        user_id: int,
    ) -> None:
        """
        Delete an athlete.
        """
        athlete = self.get(
            athlete_id,
            user_id,
        )

        self.repository.delete(
            athlete,
        )
