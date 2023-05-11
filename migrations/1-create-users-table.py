"""
create-users-table
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        """
    CREATE TABLE public.users (
    uid uuid PRIMARY KEY NOT NULL,
    username varchar(128) UNIQUE NOT NULL,
    password varchar(128) NOT NULL);
    """,
        """
         DROP TABLE IF EXISTS users;
         """,
    )
]
