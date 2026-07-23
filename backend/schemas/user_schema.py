from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):
    """
    Schema used when creating a new user.
    """

    email: EmailStr
    full_name: str
    password: str


class UserResponse(BaseModel):
    """
    Schema returned to the client.
    """

    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    full_name: str


class UserLogin(BaseModel):
    """
    Schema used when logging in.
    """

    email: EmailStr
    password: str


class Token(BaseModel):
    """
    JWT access token returned after successful login.
    """

    access_token: str
    token_type: str