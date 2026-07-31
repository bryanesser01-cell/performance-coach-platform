"""
Race Intelligence Service

Responsible for:
- analysing upcoming races
- determining training phase
- recommending training focus
- providing race intelligence for the AI Coach
"""

from datetime import date


class RaceIntelligenceService:
    """
    Analyse the athlete's next race.
    """

    def analyse(
        self,
        race: dict | None,
    ) -> dict:

        if not race:
            return {
                "has_race": False,
                "goal_event": None,
                "priority": None,
                "phase": "General Training",
                "days_until_race": None,
                "recommended_focus": "Base Fitness",
                "taper_required": False,

                # Intelligence
                "race_readiness": "training",
                "recommendation": "continue_base_training",
                "confidence": 1.0,
            }

        today = date.today()

        race_date = race["date"]

        days = (
            race_date - today
        ).days

        if days <= 7:

            phase = "Taper"

            focus = (
                "Recovery and Race Pace"
            )

            recommendation = (
                "taper_training"
            )

            readiness = "race_ready"

        elif days <= 28:

            phase = "Peak"

            focus = (
                "Race Specific"
            )

            recommendation = (
                "maintain_peak"
            )

            readiness = "peaking"

        elif days <= 84:

            phase = "Build"

            focus = (
                "Threshold and VO₂ Max"
            )

            recommendation = (
                "progress_training"
            )

            readiness = "building"

        else:

            phase = "Base"

            focus = (
                "Aerobic Development"
            )

            recommendation = (
                "build_aerobic_base"
            )

            readiness = "base"

        return {
            #
            # Existing fields
            #
            "has_race": True,
            "goal_event": race.get(
                "event",
                "Unknown",
            ),
            "priority": race.get(
                "priority",
                "B",
            ),
            "days_until_race": days,
            "phase": phase,
            "recommended_focus": focus,
            "taper_required": (
                days <= 7
            ),

            #
            # Intelligence
            #
            "race_readiness": readiness,
            "recommendation": recommendation,
            "confidence": 1.0,
        }
