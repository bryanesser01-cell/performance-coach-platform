from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.services.athlete_intelligence_memory_service import (
    build_athlete_intelligence_memory,
)
from api.services.athlete_memory_service import (
    build_memory_context,
    recall,
    remember,
)
from database.session import get_db

router = APIRouter(
    prefix="/athletes",
    tags=["Athlete Memory"],
)


@router.post("/{athlete_id}/memory")
def create_athlete_memory(
    athlete_id: int,
    memory_type: str,
    memory_value: str,
    db: Session = Depends(get_db),
):
    """
    Store athlete memory.
    """

    return remember(
        db=db,
        athlete_id=athlete_id,
        memory_type=memory_type,
        memory_value=memory_value,
    )


@router.get("/{athlete_id}/memory")
def get_athlete_memory(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    """
    Retrieve athlete memories.
    """

    return recall(
        db=db,
        athlete_id=athlete_id,
    )


@router.get("/{athlete_id}/memory/context")
def get_athlete_memory_context(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    """
    Build AI Coach memory context.
    """

    memories = recall(
        db=db,
        athlete_id=athlete_id,
    )

    return build_memory_context(
        memories,
    )


@router.get("/{athlete_id}/memory/intelligence")
def get_athlete_memory_intelligence(
    athlete_id: int,
    db: Session = Depends(get_db),
):
    """
    Build athlete intelligence memory.
    """

    memories = recall(
        db=db,
        athlete_id=athlete_id,
    )

    return build_athlete_intelligence_memory(
        athlete_profile={
            "athlete_id": athlete_id,
        },
        stored_memories=memories,
        race_results=[],
        training_history=[],
    )
