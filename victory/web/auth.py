import datetime

from fastapi_jwt import JwtAccessBearer, JwtRefreshBearer

from victory.settings import settings

__all__ = [
    "access_security",
    "refresh_security",
]

access_validity_period = datetime.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRES)
refresh_validity_period = datetime.timedelta(days=settings.REFRESH_TOKEN_EXPIRES)

access_security = JwtAccessBearer(
    secret_key=settings.JWT_SECRET_KEY.get_secret_value(),
    auto_error=True,
    access_expires_delta=access_validity_period,
)
refresh_security = JwtRefreshBearer(
    secret_key=settings.JWT_SECRET_KEY.get_secret_value(),
    auto_error=True,
    refresh_expires_delta=refresh_validity_period,
)
