"""
Workout Library Service

Provides structured workout templates
for the Adaptive Training Planner.
"""


class WorkoutLibraryService:
    """
    Library of coaching workouts.
    """

    def recovery_run(self) -> dict:
        return {
            "session_type": "Recovery Run",
            "duration_minutes": 30,
            "warmup": "5 min walk",
            "main_set": "20 min easy running",
            "cooldown": "5 min walk",
            "intensity": "very_easy",
        }

    def easy_run(self) -> dict:
        return {
            "session_type": "Easy Run",
            "duration_minutes": 45,
            "warmup": "10 min easy",
            "main_set": "30 min aerobic running",
            "cooldown": "5 min easy",
            "intensity": "easy",
        }

    def threshold_run(self) -> dict:
        return {
            "session_type": "Threshold Run",
            "duration_minutes": 55,
            "warmup": "15 min easy",
            "main_set": "5 x 6 min threshold pace",
            "recovery": "90 sec jog",
            "cooldown": "10 min easy",
            "intensity": "moderate_hard",
        }

    def vo2_max(self) -> dict:
        return {
            "session_type": "VO₂ Max Intervals",
            "duration_minutes": 60,
            "warmup": "15 min easy",
            "main_set": "6 x 3 min VO₂ pace",
            "recovery": "2 min jog",
            "cooldown": "10 min easy",
            "intensity": "very_hard",
        }

    def long_run(self) -> dict:
        return {
            "session_type": "Long Run",
            "duration_minutes": 90,
            "warmup": "10 min easy",
            "main_set": "75 min aerobic",
            "cooldown": "5 min walk",
            "intensity": "easy",
        }

    def tempo_run(self) -> dict:
        return {
            "session_type": "Tempo Run",
            "duration_minutes": 50,
            "warmup": "15 min easy",
            "main_set": "25 min tempo",
            "cooldown": "10 min easy",
            "intensity": "moderate_hard",
        }

    def taper_run(self) -> dict:
        return {
            "session_type": "Taper Session",
            "duration_minutes": 30,
            "warmup": "10 min easy",
            "main_set": "6 x 20 sec strides",
            "cooldown": "10 min easy",
            "intensity": "easy",
        }
