from database.user_models import User
from repositories.user_repository import UserRepository


def test_get_by_email(db_session):
    repository = UserRepository(db_session)

    user = User(
        email="getbyemail@example.com",
        full_name="John Doe",
        password_hash="hashed_password",
    )

    repository.create(user)

    found_user = repository.get_by_email("getbyemail@example.com")

    assert found_user is not None
    assert found_user.email == "getbyemail@example.com"
