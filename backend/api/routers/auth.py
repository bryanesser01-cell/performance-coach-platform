from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api.dependencies.auth import get_current_user
from api.services.auth_service import (
    register_user,
    login_user,
)
from database.database import get_db
from database.user_models import User
from schemas.user_schema import (
    UserCreate,
    UserLogin,
    UserResponse,
    Token,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    summary="Register",
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    """
    Register a new user.
    """
    return register_user(db, user)


@router.post(
    "/login",
    response_model=Token,
    summary="Login",
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    """
    Authenticate a user and return a JWT access token.
    """
    credentials = UserLogin(
        email=form_data.username,
        password=form_data.password,
    )

    return login_user(db, credentials)


@router.get(
    "/me",
    response_model=UserResponse,
    summary="Get current user",
)
def get_me(
    current_user: User = Depends(get_current_user),
):
    """
    Return the currently authenticated user.
    """
    return UserResponse.model_validate(current_user)