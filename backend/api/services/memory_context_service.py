from sqlalchemy.orm import Session

from database.models import (
    AthleteMemory,
    CoachDecision,
    CoachLearningEvent,
)


class MemoryContextService:
    """
    Builds historical context for the AI Coach.
    """

    def __init__(self, db: Session):
        self.db = db

    def build_context(
        self,
        athlete_id: int,
    ) -> dict:

        memories = (
            self.db.query(AthleteMemory)
            .filter(
                AthleteMemory.athlete_id == athlete_id
            )
            .order_by(
                AthleteMemory.created_at.desc()
            )
            .limit(20)
            .all()
        )

        decisions = (
            self.db.query(CoachDecision)
            .filter(
                CoachDecision.athlete_id == athlete_id
            )
            .order_by(
                CoachDecision.created_at.desc()
            )
            .limit(20)
            .all()
        )

        learning_events = (
            self.db.query(CoachLearningEvent)
            .filter(
                CoachLearningEvent.athlete_id == athlete_id
            )
            .order_by(
                CoachLearningEvent.timestamp.desc()
            )
            .limit(20)
            .all()
        )

        return {
            "memories": memories,
            "decisions": decisions,
            "learning_events": learning_events,
        }
