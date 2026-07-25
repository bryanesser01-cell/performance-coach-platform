from sqlalchemy.orm import Session

from database.performance_cycle_models import PerformanceCycle
from repositories.base_repository import BaseRepository


class PerformanceCycleRepository(BaseRepository[PerformanceCycle]):
    """Repository for PerformanceCycle persistence."""

    def __init__(self, db: Session):
        super().__init__(
            PerformanceCycle,
            db,
        )
