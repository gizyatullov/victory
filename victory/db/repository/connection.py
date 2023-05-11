from contextlib import asynccontextmanager

from aiopg import Cursor
from psycopg2.extras import RealDictCursor  # type: ignore

from victory.db.connectors import postgresql
from victory.db.connectors.postgresql import Postgresql

__all__ = ["get_cursor"]


@asynccontextmanager
async def get_cursor(
    postgres: Postgresql = postgresql,
) -> Cursor:
    """Get async connection to postgresql of pool."""

    async with postgres.get_connect() as connection:
        async with connection.cursor(cursor_factory=RealDictCursor) as c:
            yield c
