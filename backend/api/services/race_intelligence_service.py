"""
Race Intelligence Service

Responsible for:
- analysing upcoming races
- determining training phase
- recommending training focus
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
                "phase": "General Training",
                "days_until_race": None,
                "recommended_focus": "Base Fitness",
                "taper_required": False,
            }

        today = date.today()

        race_date = race["date"]

        days = (
            race_date - today
        ).days

        if days <= 7:
            phase = "Taper"
            focus = "Recovery and Race Pace"

        elif days <= 28:
            phase = "Peak"
            focus = "Race Specific"

        elif days <= 84:
            phase = "Build"
            focus = "Threshold and VO₂ Max"

        else:
            phase = "Base"
            focus = "Aerobic Development"

        return {
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
            "taper_required": days <= 7,
        }
