from database.database import Base, engine

from database import (
    activity_models,  # noqa: F401
    goal_models,  # noqa: F401
    models,  # noqa: F401
)
from database.training_models import TrainingSession  # noqa: F401

print("Creating database...")

Base.metadata.create_all(
    bind=engine,
)

print("Database created successfully!")
