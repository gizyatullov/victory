from typing import List

from victory import models
from victory.db.repository.connection import get_cursor
from victory.db.repository.handlers.collect_response import collect_response

__all__ = ["DivisionRepository"]


class DivisionRepository:
    @classmethod
    @collect_response
    async def create(cls, cmd: models.CreateDivisionCommand) -> models.Division:
        q = """
                    insert into division(
                        name
                    ) values (
                        %(name)s
                    )
                    returning id, name;
                """
        async with get_cursor() as c:
            await c.execute(q, cmd.to_dict(show_secrets=True))
            return await c.fetchone()

    @classmethod
    @collect_response
    async def read_all(cls) -> List[models.Division]:
        q = """
                select id, name
                from division;
            """
        async with get_cursor() as c:
            await c.execute(q)
            return await c.fetchall()
