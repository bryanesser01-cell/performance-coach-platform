import pytest
from unittest.mock import MagicMock, patch

from api.services.auth_service import AuthService
from core.exceptions import UnauthorizedError
from database.user_models import User
from schemas.auth import UserLogin


def test_register_success(): ...


def test_register_duplicate_email(): ...


@patch("api.services.auth_service.create_access_token")
@patch("api.services.auth_service.verify_password")
def test_login_success(
    mock_verify_password,
    mock_create_access_token,
): ...


@patch("api.services.auth_service.verify_password")
def test_login_invalid_password(
    mock_verify_password,
):
    # Arrange
    repository = MagicMock()

    repository.get_by_email.return_value = User(
        id=1,
        email="test@example.com",
        full_name="Test User",
        password_hash="hashed_password",
    )

    mock_verify_password.return_value = False

    service = AuthService(repository)

    login = UserLogin(
        email="test@example.com",
        password="WrongPassword",
    )

    # Act / Assert
    with pytest.raises(
        UnauthorizedError,
        match="Invalid email or password.",
    ):
        service.login(login)

    repository.get_by_email.assert_called_once_with("test@example.com")

    mock_verify_password.assert_called_once_with(
        "WrongPassword",
        "hashed_password",
    )


def test_login_unknown_email():
    # Arrange
    repository = MagicMock()

    repository.get_by_email.return_value = None

    service = AuthService(repository)

    login = UserLogin(
        email="unknown@example.com",
        password="Password123",
    )

    # Act / Assert
    with pytest.raises(
        UnauthorizedError,
        match="Invalid email or password.",
    ):
        service.login(login)

    repository.get_by_email.assert_called_once_with("unknown@example.com")
