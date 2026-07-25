from database.user_models import User
from repositories.user_repository import UserRepository
from tests.testing_database import TestingSessionLocal


def test_create_user():
    db = TestingSessionLocal()

    repository = UserRepository(db)

    user = User(
        email="repository@example.com",
        full_name="Repository User",
        password_hash="hashed_password",
    )

    created_user = repository.create(user)

    assert created_user.id is not None
    assert created_user.email == "repository@example.com"
    assert created_user.full_name == "Repository User"

    db.close()
