from domain.training.entities import TrainingSession
from domain.training.repository import TrainingRepository


class TrainingService:
    def __init__(self, repository: TrainingRepository):
        self._repository = repository

    def create_training_session(self, session: TrainingSession) -> None:
        self._repository.save(session)

    def get_training_session(self, session_id):
        return self._repository.get_by_id(session_id)

    def list_training_sessions(self, athlete_id):
        return self._repository.list_by_athlete(athlete_id)
