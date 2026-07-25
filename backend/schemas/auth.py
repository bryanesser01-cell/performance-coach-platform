from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserRegister(BaseModel):
    """
    Request body used to register a new user.
    """

    email: EmailStr

    full_name: str = Field(
        ...,
        min_length=2,
        max_length=100,
    )

    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
    )


class UserLogin(BaseModel):
    """
    Request body used to authenticate a user.
    """

    email: EmailStr

    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
    )


class Token(BaseModel):
    """
    JWT access token returned after authentication.
    """

    model_config = ConfigDict(
        from_attributes=True,
    )

    access_token: str
    token_type: str
