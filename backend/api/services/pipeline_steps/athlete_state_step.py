from sqlalchemy.orm import Session

from api.models.coach_context import CoachContext
from api.services.athlete_state_service import (
    get_athlete_state,
)


class AthleteStateStep:
    """
    Loads the athlete state.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def __call__(
        self,
        context: CoachContext,
    ) -> None:

        context.athlete_state = get_athlete_state(
            self.db,
            context.athlete_id,
        )
