"""
division
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        """
    CREATE TABLE public.division (
    id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name varchar(255) NOT NULL
    );
    """,
        """
         DROP TABLE IF EXISTS division;
         """,
    )
]
