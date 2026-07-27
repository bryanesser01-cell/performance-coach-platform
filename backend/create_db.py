from database.base import Base

# Import all ORM models so SQLAlchemy knows about them
from database.models import *  # noqa: F401,F403
from database.session import engine
from database.training_models import *  # noqa: F401,F403

print("Creating PostgreSQL database tables...")

Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")
