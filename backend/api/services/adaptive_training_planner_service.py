"""
Adaptive Training Planner

Generates training session recommendations
using athlete intelligence and coaching decisions.
"""

from api.services.workout_library_service import (
    WorkoutLibraryService,
)


class AdaptiveTrainingPlannerService:
    """
    Generates adaptive training sessions
    for an athlete.
    """

    def generate_session(
        self,
        twin,
        decision: str,
    ) -> dict:
        """
        Generate a training session based
        on the current coaching decision.
        """

        library = WorkoutLibraryService()

        #
        # Use the Athlete Digital Twin when available
        #
        if twin is not None:

            if twin.needs_recovery():
                return library.recovery_run()

            if twin.is_tapering():
                return library.taper_run()

        #
        # Fall back to coach decision
        #
        if decision == "RECOVERY_DAY":
            return library.recovery_run()

        if decision == "REDUCE_VOLUME":
            return library.easy_run()

        if decision == "RACE_TAPER":
            return library.taper_run()

        if decision == "PROGRESS_TRAINING":

            #
            # No Digital Twin available
            #
            if twin is None:
                return library.threshold_run()

            #
            # 5K Athlete
            #
            if twin.goal().lower() == "5k":

                if twin.race_phase() == "base":
                    return library.threshold_run()

                if twin.race_phase() == "build":
                    return library.vo2_max()

                if twin.race_phase() == "peak":
                    return library.threshold_run()

                if twin.race_phase() == "taper":
                    return library.taper_run()

            #
            # Marathon Athlete
            #
            if twin.goal().lower() == "marathon":

                if twin.race_phase() == "base":
                    return library.long_run()

                if twin.race_phase() == "build":
                    return library.tempo_run()

                if twin.race_phase() == "peak":
                    return library.tempo_run()

                if twin.race_phase() == "taper":
                    return library.taper_run()

            #
            # Default progress workout
            #
            return library.threshold_run()

        #
        # Default decision
        #
        return library.easy_run()
