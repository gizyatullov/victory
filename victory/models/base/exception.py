from typing import Optional

from fastapi import HTTPException
from starlette import status

__all__ = ["BaseAPIException"]


class BaseAPIException(HTTPException):
    message: Optional[str] = "Base API Exception"
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(
        self, message: Optional[str] = None, status_code: Optional[int] = None
    ):
        if message is not None:
            self.message = message
        if status_code is not None:
            self.status_code = status_code

        super().__init__(status_code=self.status_code, detail=self.message)
