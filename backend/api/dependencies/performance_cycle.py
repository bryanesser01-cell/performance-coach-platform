from fastapi import Depends
from sqlalchemy.orm import Session

from database.database import get_db
from repositories.performance_cycle_repository import (
    PerformanceCycleRepository,
)
from api.services.performance_cycle_service import (
    PerformanceCycleService,
)


def get_performance_cycle_repository(
    db: Session = Depends(get_db),
) -> PerformanceCycleRepository:
    """
    Return a PerformanceCycleRepository instance.
    """
    return PerformanceCycleRepository(db)


def get_performance_cycle_service(
    repository: PerformanceCycleRepository = Depends(
        get_performance_cycle_repository,
    ),
) -> PerformanceCycleService:
    """
    Return a PerformanceCycleService instance.
    """
    return PerformanceCycleService(repository)
