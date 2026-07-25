from app.security.jwt import create_access_token
from core.exceptions import (
    UnauthorizedError,
    ValidationError,
)
from core.security import (
    hash_password,
    verify_password,
)
from database.user_models import User
from repositories.user_repository import UserRepository
from schemas.auth import (
    Token,
    UserLogin,
    UserRegister,
)
from schemas.user_schema import UserResponse


class AuthService:
    """
    Service responsible for user registration and authentication.
    """

    def __init__(
        self,
        repository: UserRepository,
    ):
        self.repository = repository

    def register(
        self,
        user: UserRegister,
    ) -> UserResponse:
        """
        Register a new user.
        """
        if self.repository.get_by_email(user.email):
            raise ValidationError("Email is already registered.")

        new_user = User(
            email=user.email,
            full_name=user.full_name,
            password_hash=hash_password(
                user.password,
            ),
        )

        created_user = self.repository.create(
            new_user,
        )

        return UserResponse.model_validate(
            created_user,
        )

    def login(
        self,
        user: UserLogin,
    ) -> Token:
        """
        Authenticate a user and return a JWT access token.
        """
        existing_user = self.repository.get_by_email(
            user.email,
        )

        if existing_user is None or not verify_password(
            user.password,
            existing_user.password_hash,
        ):
            raise UnauthorizedError("Invalid email or password.")

        access_token = create_access_token(
            {
                "sub": str(existing_user.id),
                "email": existing_user.email,
            }
        )

        return Token(
            access_token=access_token,
            token_type="bearer",
        )
