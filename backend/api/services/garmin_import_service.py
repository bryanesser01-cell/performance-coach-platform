from database.repositories.activity_repository import ActivityRepository
from domain.activity.entities import Activity
from integrations.garmin import GarminActivityImporter


class GarminImportService:
    """
    Imports Garmin activities into the platform.
    """

    def __init__(
        self,
        repository: ActivityRepository,
        importer: GarminActivityImporter,
    ):
        self.repository = repository
        self.importer = importer

    def import_activities(
        self,
        athlete_id,
    ) -> list[Activity]:
        """
        Import all Garmin activities for an athlete.
        """

        imported: list[Activity] = []

        activities = self.importer.get_activities(
            athlete_id,
        )

        for activity in activities:

            if self.repository.exists(
                activity.external_id,
            ):
                continue

            self.repository.create(
                activity,
            )

            imported.append(
                activity,
            )

        return imported
