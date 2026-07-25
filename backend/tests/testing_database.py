from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ---------------------------------------------------------------------
# Test Database Configuration
# ---------------------------------------------------------------------

TEST_DATABASE_URL = "sqlite:///./test_performance_coach.db"

test_engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=test_engine,
)

# ---------------------------------------------------------------------
# Test Database Dependency
# ---------------------------------------------------------------------


def get_test_db():
    """
    FastAPI dependency that provides a test database session.
    """
    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()
