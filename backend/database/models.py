"""
Imports all SQLAlchemy models so they are registered with SQLAlchemy's metadata.

Alembic imports this module to discover every database table when generating
or applying migrations.
"""

from database.athlete_models import Athlete
from database.goal_models import Goal
from database.performance_cycle_models import PerformanceCycle
from database.training_models import TrainingSession
from database.user_models import User

__all__ = [
    "User",
    "Athlete",
    "Goal",
    "TrainingSession",
    "PerformanceCycle",
]
