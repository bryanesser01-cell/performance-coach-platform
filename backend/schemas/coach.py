from pydantic import BaseModel

from schemas.analysis import PerformanceAnalysis
from schemas.workout import WorkoutRecommendation
from schemas.recommendation import Recommendation


class CoachResponse(BaseModel):
    analysis: PerformanceAnalysis
    workout: WorkoutRecommendation
    recommendations: list[Recommendation]
