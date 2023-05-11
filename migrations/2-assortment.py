"""
assortment
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        """
    CREATE TABLE public.assortment(
    id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name varchar(255) NOT NULL,
    measureunit varchar(5) NOT NULL
    );
    """,
        """
         DROP TABLE IF EXISTS assortment;
         """,
    )
]
