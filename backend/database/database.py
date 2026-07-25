from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config.settings import settings

# ---------------------------------------------------------------------
# Database Engine
# ---------------------------------------------------------------------

engine_kwargs = {}

# SQLite requires this connection argument.
# PostgreSQL ignores it.
if settings.database_url.startswith("sqlite"):
    engine_kwargs["connect_args"] = {
        "check_same_thread": False,
    }

engine = create_engine(
    settings.database_url,
    **engine_kwargs,
)

# ---------------------------------------------------------------------
# Session Factory
# ---------------------------------------------------------------------

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# ---------------------------------------------------------------------
# Base Class
# ---------------------------------------------------------------------

Base = declarative_base()


# ---------------------------------------------------------------------
# Database Dependency
# ---------------------------------------------------------------------


def get_db():
    """
    FastAPI dependency that provides a database session.
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
