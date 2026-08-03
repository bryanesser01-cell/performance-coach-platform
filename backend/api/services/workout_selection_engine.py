"""
Workout Selection Engine

Selects the optimal workout based on:

- Athlete Digital Twin
- Coaching decision
- Goal
- Race phase
"""

from api.services.workout_library_service import (
    WorkoutLibraryService,
)


class WorkoutSelectionEngine:
    """
    Selects the optimal workout
    based on athlete context.
    """

    def select_workout(
        self,
        twin,
        decision: str,
    ) -> dict:

        library = WorkoutLibraryService()

        #
        # Athlete Digital Twin overrides
        #
        if twin is not None:

            if twin.needs_recovery():
                return library.recovery_run()

            if twin.is_tapering():
                return library.taper_run()

        #
        # Decision overrides
        #
        if decision == "RECOVERY_DAY":
            return library.recovery_run()

        if decision == "REDUCE_VOLUME":
            return library.easy_run()

        if decision == "RACE_TAPER":
            return library.taper_run()

        #
        # Progress training
        #
        if decision == "PROGRESS_TRAINING":

            if twin is None:
                return library.threshold_run()

            goal = twin.goal().lower()
            phase = twin.race_phase().lower()

            #
            # 5K athlete
            #
            if goal == "5k":

                if phase == "base":
                    return library.threshold_run()

                if phase == "build":
                    return library.vo2_max()

                if phase == "peak":
                    return library.threshold_run()

                if phase == "taper":
                    return library.taper_run()

            #
            # Marathon athlete
            #
            if goal == "marathon":

                if phase == "base":
                    return library.long_run()

                if phase == "build":
                    return library.tempo_run()

                if phase == "peak":
                    return library.tempo_run()

                if phase == "taper":
                    return library.taper_run()

            #
            # Default progression workout
            #
            return library.threshold_run()

        #
        # Default
        #
        return library.easy_run()
