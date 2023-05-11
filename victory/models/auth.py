from pydantic.fields import Field

from victory.models.base import BaseModel

from .user import UserFields

__all__ = [
    "TokenPair",
    "AuthCommand",
    "RefreshTokenPair",
]


class AuthFields:
    access_token = Field(description="Bearer access token", example="")
    refresh_token = Field(description="Bearer refresh token", example="")
    token_type = Field(description="", example="bearer", default="bearer")


class BaseAuth(BaseModel):
    """Base model for auth."""


class TokenPair(BaseAuth):
    access_token: str = AuthFields.access_token
    refresh_token: str = AuthFields.refresh_token
    token_type: str = AuthFields.token_type


# Commands.
class AuthCommand(BaseAuth):
    username: str = UserFields.username
    password: str = UserFields.password


class RefreshTokenPair(BaseAuth):
    refresh_token: str = AuthFields.refresh_token
