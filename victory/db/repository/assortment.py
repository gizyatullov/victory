from typing import List

from victory import models
from victory.db.repository.connection import get_cursor
from victory.db.repository.handlers.collect_response import collect_response

__all__ = ["AssortmentRepository"]


class AssortmentRepository:
    @classmethod
    @collect_response
    async def create(cls, cmd: models.CreateAssortmentCommand) -> models.Assortment:
        q = """
                        insert into assortment(
                            name, measureunit
                        ) values (
                            %(name)s,
                            %(measureunit)s
                        )
                        returning id, name, measureunit;
                    """
        async with get_cursor() as c:
            await c.execute(q, cmd.to_dict(show_secrets=True))
            return await c.fetchone()

    @classmethod
    @collect_response
    async def read_all(cls) -> List[models.Assortment]:
        q = """
                    select id, name, measureunit
                    from assortment;
                """
        async with get_cursor() as c:
            await c.execute(q)
            return await c.fetchall()
