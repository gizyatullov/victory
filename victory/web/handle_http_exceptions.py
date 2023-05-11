from fastapi import Request
from fastapi.responses import JSONResponse

from victory.models.base import BaseAPIException

__all__ = [
    "handle_api_exceptions",
]


def handle_api_exceptions(request: Request, exc: BaseAPIException) -> JSONResponse:
    """Handle all internal exceptions which inherited from
    `BaseAPIException`."""
    _ = request

    return JSONResponse(status_code=exc.status_code, content={"message": exc.message})
