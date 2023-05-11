from uuid import uuid4

from victory import models
from victory.db.repository.connection import get_cursor
from victory.db.repository.handlers.collect_response import collect_response

__all__ = ["UserRepository"]


class UserRepository:
    @classmethod
    @collect_response
    async def create(cls, cmd: models.CreateUserCommand) -> models.User:
        q = f"""
                insert into users(
                    uid, username, password
                ) values (
                    '{uuid4()}',
                    %(username)s,
                    %(password)s
                )
                returning uid, username, password;
            """
        async with get_cursor() as c:
            await c.execute(q, cmd.to_dict(show_secrets=True))
            return await c.fetchone()

    @classmethod
    @collect_response
    async def read_by_username(
        cls,
        query: models.ReadUserByUserNameQuery,
    ) -> models.User:
        q = """
                select
                    uid, username, password
                from users
                where username = %(username)s;
            """
        async with get_cursor() as c:
            await c.execute(q, query.to_dict(show_secrets=True))
            return await c.fetchone()
