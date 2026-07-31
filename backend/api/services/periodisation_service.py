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
                "recommendation": "maintain_training",
            },
            "Base": {
                "weekly_focus": "Aerobic Development",
                "volume": "High",
                "intensity": "Low",
                "recommendation": "build_aerobic_base",
            },
            "Build": {
                "weekly_focus": "Threshold Development",
                "volume": "Moderate-High",
                "intensity": "Moderate",
                "recommendation": "progress_training",
            },
            "Peak": {
                "weekly_focus": "Race Specific Speed",
                "volume": "Moderate",
                "intensity": "High",
                "recommendation": "maintain_peak",
            },
            "Taper": {
                "weekly_focus": "Freshen Up",
                "volume": "Low",
                "intensity": "Race Pace",
                "recommendation": "taper_training",
            },
            "Recovery": {
                "weekly_focus": "Recovery",
                "volume": "Very Low",
                "intensity": "Easy",
                "recommendation": "recover",
            },
        }

        plan = plans.get(
            phase,
            plans["General Training"],
        )

        return {
            #
            # Existing fields
            #
            "phase": phase,
            **plan,

            #
            # Intelligence
            #
            "confidence": 1.0,
            "periodisation_complete": True,
        }
