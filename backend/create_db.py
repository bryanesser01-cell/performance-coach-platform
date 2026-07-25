from database.database import Base, engine

# Import models so SQLAlchemy registers them with Base.metadata
from database import models  # noqa: F401
from database import goal_models  # noqa: F401
from database.training_models import TrainingSession  # noqa: F401

print("Creating database...")

Base.metadata.create_all(bind=engine)

print("Database created successfully!")
