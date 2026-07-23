from fastapi import HTTPException
from sqlalchemy.orm import Session

from core.security import hash_password
from database.user_models import User
from repositories.user_repository import UserRepository
from schemas.user_schema import UserCreate, UserResponse


def register_user(
    db: Session,
    user: UserCreate,
) -> UserResponse:

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