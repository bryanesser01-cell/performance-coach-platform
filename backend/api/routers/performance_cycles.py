from fastapi import (
    APIRouter,
    Depends,
    Response,
    status,
)

from api.dependencies.performance_cycle import (
    get_performance_cycle_service,
)
from api.services.performance_cycle_service import (
    PerformanceCycleService,
)
from schemas.performance_cycle import (
    PerformanceCycleCreate,
    PerformanceCycleResponse,
    PerformanceCycleUpdate,
)

router = APIRouter(
    prefix="/performance-cycles",
    tags=["Performance Cycles"],
)


@router.post(
    "",
    response_model=PerformanceCycleResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_performance_cycle(
    performance_cycle: PerformanceCycleCreate,
    service: PerformanceCycleService = Depends(
        get_performance_cycle_service,
    ),
) -> PerformanceCycleResponse:
    """
    Create a new performance cycle.
    """

    return service.create(
        performance_cycle,
    )


@router.get(
    "",
    response_model=list[PerformanceCycleResponse],
)
def get_performance_cycles(
    service: PerformanceCycleService = Depends(
        get_performance_cycle_service,
    ),
) -> list[PerformanceCycleResponse]:
    """
    Return all performance cycles.
    """

    return service.get_all()


@router.get(
    "/{cycle_id}",
    response_model=PerformanceCycleResponse,
)
def get_performance_cycle(
    cycle_id: int,
    service: PerformanceCycleService = Depends(
        get_performance_cycle_service,
    ),
) -> PerformanceCycleResponse:
    """
    Return a performance cycle by ID.
    """

    return service.get_by_id(
        cycle_id,
    )


@router.put(
    "/{cycle_id}",
    response_model=PerformanceCycleResponse,
)
def update_performance_cycle(
    cycle_id: int,
    performance_cycle: PerformanceCycleUpdate,
    service: PerformanceCycleService = Depends(
        get_performance_cycle_service,
    ),
) -> PerformanceCycleResponse:
    """
    Update a performance cycle.
    """

    return service.update(
        cycle_id,
        performance_cycle,
    )


@router.delete(
    "/{cycle_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_performance_cycle(
    cycle_id: int,
    service: PerformanceCycleService = Depends(
        get_performance_cycle_service,
    ),
) -> Response:
    """
    Delete a performance cycle.
    """

    service.delete(
        cycle_id,
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )
