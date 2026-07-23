from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.security.jwt import create_access_token
from core.security import hash_password, verify_password
from database.user_models import User
from repositories.user_repository import UserRepository
from schemas.user_schema import (
    UserCreate,
    UserResponse,
    UserLogin,
    Token,
)


def register_user(
    db: Session,
    user: UserCreate,
) -> UserResponse:
    """
    Register a new user.
    """

    repository = UserRepository(db)

    existing_user = repository.get_by_email(user.email)

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email is already registered",
        )

    new_user = User(
        email=user.email,
        full_name=user.full_name,
        password_hash=hash_password(user.password),
    )

    created_user = repository.create(new_user)

    return UserResponse.model_validate(created_user)


def login_user(
    db: Session,
    user: UserLogin,
) -> Token:
    """
    Authenticate a user and return a JWT access token.
    """

    repository = UserRepository(db)

    existing_user = repository.get_by_email(user.email)

    if existing_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    if not verify_password(
        user.password,
        existing_user.password_hash,
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

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