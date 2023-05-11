import bcrypt
from pydantic import UUID4, PositiveInt
from pydantic.fields import Field

from victory.models.base import BaseModel

__all__ = [
    "CreateUserCommand",
    "UserFields",
    "User",
    "ReadUserByUserNameQuery",
]


class UserFields:
    uid = Field(description="User uid.", example="4ee60f1f-880c-4b9c-8b83-d9d6d2c30034")
    username = Field(description="User Login", example="varick")
    password = Field(
        description="User password",
        example="strong password",
        min_length=8,
        max_length=256,
    )


class BaseUser(BaseModel):
    """Base model for user."""


class User(BaseUser):
    uid: UUID4 = UserFields.uid
    username: str = UserFields.username
    password: str = UserFields.password

    async def check_password(self, password: str) -> bool:
        password_bytes = password.encode("utf-8")
        hashed_bytes = self.password.encode("utf-8")
        return bcrypt.checkpw(password_bytes, hashed_bytes)


# Commands.
class CreateUserCommand(BaseUser):
    username: str = UserFields.username
    password: str = UserFields.password

    async def set_hash_password(self) -> None:
        password_bytes = self.password.encode("utf-8")
        self.password = bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")


# Query
class ReadUserByUserNameQuery(BaseUser):
    username: str = UserFields.username
