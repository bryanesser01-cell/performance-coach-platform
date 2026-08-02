from sqlalchemy.orm import Session

from database.models import VoiceSession


class VoiceSessionRepository:
    """
    Repository for voice coach sessions.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create_session_message(
        self,
        athlete_id: int,
        session_id: str,
        user_message: str,
        coach_response: str,
    ) -> VoiceSession:
        """
        Store conversation message.
        """

        session = VoiceSession(
            athlete_id=athlete_id,
            session_id=session_id,
            user_message=user_message,
            coach_response=coach_response,
        )

        self.db.add(
            session,
        )

        self.db.commit()

        self.db.refresh(
            session,
        )

        return session

    def get_session_history(
        self,
        athlete_id: int,
        session_id: str,
    ) -> list[VoiceSession]:
        """
        Retrieve previous conversation.
        """

        return (
            self.db.query(
                VoiceSession,
            )
            .filter(
                VoiceSession.athlete_id == athlete_id,
            )
            .filter(
                VoiceSession.session_id == session_id,
            )
            .order_by(
                VoiceSession.created_at.asc(),
            )
            .all()
        )
