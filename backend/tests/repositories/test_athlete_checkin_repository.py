from datetime import UTC, datetime

from database.repositories.athlete_checkin_repository import (
    AthleteCheckinRepository,
)


class FakeCheckin:
    def __init__(
        self,
        athlete_id,
        sleep_score,
        soreness_score,
        energy_score,
        motivation_score,
    ):
        self.athlete_id = athlete_id
        self.sleep_score = sleep_score
        self.soreness_score = soreness_score
        self.energy_score = energy_score
        self.motivation_score = motivation_score
        self.created_at = datetime.now(UTC)


def test_create_checkin():

    class FakeDB:

        def add(self, item):
            self.item = item

        def commit(self):
            pass

        def refresh(self, item):
            pass

    db = FakeDB()

    repository = AthleteCheckinRepository(
        db,
    )

    checkin = repository.create(
        athlete_id=1,
        sleep_score=8,
        soreness_score=2,
        energy_score=9,
        motivation_score=8,
    )

    assert checkin.athlete_id == 1


def test_repository_has_latest_method():

    assert hasattr(
        AthleteCheckinRepository,
        "get_latest_by_athlete_id",
    )
