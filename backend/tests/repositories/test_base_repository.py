from database.user_models import User
from repositories.base_repository import BaseRepository


def test_create(db_session):
    repository = BaseRepository(User, db_session)

    user = User(
        email="create@example.com",
        full_name="Create User",
        password_hash="hashed_password",
    )

    created_user = repository.create(user)

    assert created_user.id is not None
    assert created_user.email == "create@example.com"


def test_get_by_id(db_session):
    repository = BaseRepository(User, db_session)

    user = User(
        email="getbyid@example.com",
        full_name="Get By ID",
        password_hash="hashed_password",
    )

    created_user = repository.create(user)

    found_user = repository.get_by_id(created_user.id)

    assert found_user is not None
    assert found_user.id == created_user.id
    assert found_user.email == "getbyid@example.com"


def test_get_all(db_session):
    repository = BaseRepository(User, db_session)

    repository.create(
        User(
            email="user1@example.com",
            full_name="User One",
            password_hash="hashed_password",
        )
    )

    repository.create(
        User(
            email="user2@example.com",
            full_name="User Two",
            password_hash="hashed_password",
        )
    )

    users = repository.get_all()

    assert len(users) == 2


def test_update(db_session):
    repository = BaseRepository(User, db_session)

    user = repository.create(
        User(
            email="update@example.com",
            full_name="Old Name",
            password_hash="hashed_password",
        )
    )

    updated_user = repository.update(
        user,
        {
            "full_name": "New Name",
        },
    )

    assert updated_user.full_name == "New Name"

    refreshed_user = repository.get_by_id(user.id)

    assert refreshed_user is not None
    assert refreshed_user.full_name == "New Name"


def test_delete(db_session):
    repository = BaseRepository(User, db_session)

    user = repository.create(
        User(
            email="delete@example.com",
            full_name="Delete Me",
            password_hash="hashed_password",
        )
    )

    repository.delete(user)

    deleted_user = repository.get_by_id(user.id)

    assert deleted_user is None
