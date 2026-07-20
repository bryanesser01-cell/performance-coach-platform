from pydantic import BaseModel


class WorkoutRecommendation(BaseModel):
    workout_type: str
    distance_km: float
    duration_minutes: int
    target_pace: str
    target_heart_rate: str
    purpose: str