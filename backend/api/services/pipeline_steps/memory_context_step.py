from sqlalchemy.orm import Session

from api.models.coach_context import CoachContext
from api.services.memory_context_service import (
    MemoryContextService,
)


class MemoryContextStep:
    """
    Loads memory context into the coach context.
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
        context.memory_context = (
            MemoryContextService(self.db)
            .build_context(
                context.athlete_id,
            )
        )
