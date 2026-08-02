from sqlalchemy.orm import Session

from database.models import AthleteMemory


class AthleteMemoryRepository:
    """
    Repository for athlete memory storage.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create(
        self,
        athlete_id: int,
        memory_type: str,
        memory_value: str,
    ) -> AthleteMemory:
        """
        Create a new athlete memory item.
        """

        memory = AthleteMemory(
            athlete_id=athlete_id,
            memory_type=memory_type,
            memory_value=memory_value,
        )

        self.db.add(
            memory,
        )

        self.db.commit()

        self.db.refresh(
            memory,
        )

        return memory

    def get_by_athlete_id(
        self,
        athlete_id: int,
    ) -> list[AthleteMemory]:
        """
        Retrieve all memories for athlete.
        """

        return (
            self.db.query(
                AthleteMemory,
            )
            .filter(
                AthleteMemory.athlete_id == athlete_id,
            )
            .order_by(
                AthleteMemory.created_at.desc(),
            )
            .all()
        )

    def get_by_type(
        self,
        athlete_id: int,
        memory_type: str,
    ) -> list[AthleteMemory]:
        """
        Retrieve memories by type.
        """

        return (
            self.db.query(
                AthleteMemory,
            )
            .filter(
                AthleteMemory.athlete_id == athlete_id,
            )
            .filter(
                AthleteMemory.memory_type == memory_type,
            )
            .order_by(
                AthleteMemory.created_at.desc(),
            )
            .all()
        )
