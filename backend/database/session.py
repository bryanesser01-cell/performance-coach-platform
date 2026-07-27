from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config.settings import settings

engine = create_engine(
    settings.database_url,
    echo=True,  # Set to False in production
)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


def get_db():
    """Provide a SQLAlchemy database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
