from typing import Any

from fastapi import APIRouter, status

from victory import models
from victory.db.repository.user import UserRepository

__all__ = ["router"]

router = APIRouter()


@router.post(
    "/",
    response_model=models.User,
    status_code=status.HTTP_201_CREATED,
    summary="Create user",
    response_model_exclude={"password"},
)
async def create_user(cmd: models.CreateUserCommand) -> Any:
    await cmd.set_hash_password()
    return await UserRepository.create(cmd=cmd)
