"""
Periodisation Engine

Responsible for converting race phase into
weekly coaching recommendations.
"""


class PeriodisationEngine:
    """
    Build weekly training recommendations.
    """

    def build_plan(
        self,
        race_intelligence: dict,
    ) -> dict:

        phase = race_intelligence.get(
            "phase",
            "General Training",
        )

        plans = {
            "General Training": {
                "weekly_focus": "General Fitness",
                "volume": "Normal",
                "intensity": "Moderate",
            },
            "Base": {
                "weekly_focus": "Aerobic Development",
                "volume": "High",
                "intensity": "Low",
            },
            "Build": {
                "weekly_focus": "Threshold Development",
                "volume": "Moderate-High",
                "intensity": "Moderate",
            },
            "Peak": {
                "weekly_focus": "Race Specific Speed",
                "volume": "Moderate",
                "intensity": "High",
            },
            "Taper": {
                "weekly_focus": "Freshen Up",
                "volume": "Low",
                "intensity": "Race Pace",
            },
            "Recovery": {
                "weekly_focus": "Recovery",
                "volume": "Very Low",
                "intensity": "Easy",
            },
        }

        plan = plans.get(
            phase,
            plans["General Training"],
        )

        return {
            "phase": phase,
            **plan,
        }
