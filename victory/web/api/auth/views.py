from typing import Any

from fastapi import APIRouter, Security, status
from fastapi_jwt import JwtAuthorizationCredentials

from victory import models
from victory.db.repository.user import UserRepository
from victory.models.base import BaseAPIException
from victory.web.auth import access_security, refresh_security

__all__ = ["router"]

router = APIRouter()


@router.post(
    "/",
    response_model=models.TokenPair,
    status_code=status.HTTP_200_OK,
    summary="Auth user",
)
async def auth_user(cmd: models.AuthCommand) -> Any:
    user = await UserRepository.read_by_username(
        models.ReadUserByUserNameQuery(username=cmd.username)
    )
    if await user.check_password(password=cmd.password):
        return models.TokenPair(
            access_token=access_security.create_access_token(
                subject={}, unique_identifier=user.username
            ),
            refresh_token=refresh_security.create_refresh_token(
                subject={}, unique_identifier=user.username
            ),
        )
    raise BaseAPIException(
        status_code=status.HTTP_403_FORBIDDEN,
        message="possibly an incorrect login password pair",
    )


@router.post(
    "/refresh",
    response_model=models.TokenPair,
    status_code=status.HTTP_200_OK,
    summary="Refresh token pair",
)
async def refresh_token_pair(
    credentials: JwtAuthorizationCredentials = Security(refresh_security),
) -> Any:
    return models.TokenPair(
        access_token=access_security.create_access_token(
            subject={}, unique_identifier=credentials.jti
        ),
        refresh_token=refresh_security.create_refresh_token(
            subject={}, unique_identifier=credentials.jti
        ),
    )
