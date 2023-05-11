"""Postgresql connector."""
import typing
from contextlib import asynccontextmanager

import aiopg
from aiopg import Connection

from .base_connector import BaseConnector

__all__ = ["Postgresql"]


class Postgresql(BaseConnector):
    uri: str

    def __init__(self, uri: str):
        self.uri = uri

    @asynccontextmanager
    async def get_connect(self) -> typing.AsyncIterator[Connection]:
        async with aiopg.create_pool(dsn=self.uri) as pool:
            async with pool.acquire() as conn:
                yield conn
