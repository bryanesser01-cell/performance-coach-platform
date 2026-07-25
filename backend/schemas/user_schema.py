from pydantic import BaseModel, ConfigDict, EmailStr


class UserResponse(BaseModel):
    """
    User returned by the API.
    """

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
    email: EmailStr
    full_name: str
