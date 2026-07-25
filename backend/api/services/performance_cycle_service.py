from core.exceptions import ResourceNotFoundError
from database.performance_cycle_models import (
    PerformanceCycle,
)
from repositories.performance_cycle_repository import (
    PerformanceCycleRepository,
)
from schemas.performance_cycle import (
    PerformanceCycleCreate,
    PerformanceCycleResponse,
    PerformanceCycleUpdate,
)


class PerformanceCycleService:
    """
    Service responsible for managing performance cycles.
    """

    def __init__(
        self,
        repository: PerformanceCycleRepository,
    ):
        self.repository = repository

    def create(
        self,
        performance_cycle: PerformanceCycleCreate,
    ) -> PerformanceCycleResponse:
        """
        Create a new performance cycle.
        """

        new_cycle = PerformanceCycle(
            **performance_cycle.model_dump(),
        )

        created_cycle = self.repository.create(
            new_cycle,
        )

        return PerformanceCycleResponse.model_validate(
            created_cycle,
        )

    def get_by_id(
        self,
        cycle_id: int,
    ) -> PerformanceCycleResponse:
        """
        Return a performance cycle by ID.
        """

        cycle = self.repository.get_by_id(
            cycle_id,
        )

        if cycle is None:
            raise ResourceNotFoundError("Performance cycle not found.")

        return PerformanceCycleResponse.model_validate(
            cycle,
        )

    def get_all(
        self,
    ) -> list[PerformanceCycleResponse]:
        """
        Return all performance cycles.
        """

        cycles = self.repository.get_all()

        return [
            PerformanceCycleResponse.model_validate(
                cycle,
            )
            for cycle in cycles
        ]

    def update(
        self,
        cycle_id: int,
        performance_cycle: PerformanceCycleUpdate,
    ) -> PerformanceCycleResponse:
        """
        Update a performance cycle.
        """

        cycle = self.repository.get_by_id(
            cycle_id,
        )

        if cycle is None:
            raise ResourceNotFoundError("Performance cycle not found.")

        updated_cycle = self.repository.update(
            cycle,
            performance_cycle.model_dump(
                exclude_unset=True,
            ),
        )

        return PerformanceCycleResponse.model_validate(
            updated_cycle,
        )

    def delete(
        self,
        cycle_id: int,
    ) -> None:
        """
        Delete a performance cycle.
        """

        cycle = self.repository.get_by_id(
            cycle_id,
        )

        if cycle is None:
            raise ResourceNotFoundError("Performance cycle not found.")

        self.repository.delete(
            cycle,
        )
