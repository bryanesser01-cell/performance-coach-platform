from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from api.dependencies.types import (
    AuthServiceDep,
    CurrentUser,
)
from schemas.auth import (
    Token,
    UserLogin,
    UserRegister,
)
from schemas.user_schema import UserResponse

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
)
def register(
    user: UserRegister,
    service: AuthServiceDep,
):
    """
    Register a new user.
    """
    return service.register(user)


@router.post(
    "/login",
    response_model=Token,
    summary="Authenticate a user",
)
def login(
    service: AuthServiceDep,
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    """
    Authenticate a user.
    """
    credentials = UserLogin(
        email=form_data.username,
        password=form_data.password,
    )

    return service.login(credentials)


@router.get(
    "/me",
    response_model=UserResponse,
    summary="Get current user",
)
def get_me(
    current_user: CurrentUser,
):
    """
    Retrieve the authenticated user.
    """
    return UserResponse.model_validate(current_user)
