from database.database import Base, engine
from database import models
from database import goal_models
from database.training_models import TrainingSession

print("Creating database...")

Base.metadata.create_all(bind=engine)

print("Database created successfully!")