"""Migration methods."""

from argparse import ArgumentParser

from yoyo import get_backend, read_migrations

from victory.db.connectors import postgresql
from victory.db.connectors.postgresql import Postgresql


def _apply(backend, migrations):
    """Apply all migrations from `migrations`."""
    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))


def _rollback(backend, migrations):
    """Rollback all migrations."""
    with backend.lock():
        backend.rollback_migrations(backend.to_rollback(migrations))


def _rollback_one(backend, migrations):
    """Rollback one migration."""
    with backend.lock():
        migrations = backend.to_rollback(migrations)
        for migration in migrations:
            backend.rollback_one(migration)
            break


def _reload(backend, migrations):
    """Rollback all and apply all migrations."""
    with backend.lock():
        backend.rollback_migrations(backend.to_rollback(migrations))
        backend.apply_migrations(backend.to_apply(migrations))


def run(
    action,
    _postgresql: Postgresql = postgresql,
):
    """Run ``yoyo-migrations`` based on cli_arguments.

    Notes:
        Before running backend migrations, `run` wiring injections.

    Args:
        action(Callable[..., None]): Target function.
        _postgresql: Factory instance of postgresql driver.

    Returns:
        None
    """

    backend = get_backend(uri=_postgresql.uri)
    migrations = read_migrations("migrations")
    action(backend, migrations)


def parse_cli_args():
    """Parse cli arguments."""

    parser = ArgumentParser(description="Apply migrations")
    parser.add_argument("--rollback", action="store_true", help="Rollback migrations")
    parser.add_argument(
        "--rollback-one",
        action="store_true",
        help="Rollback one migration",
    )
    parser.add_argument(
        "--reload",
        action="store_true",
        help="Rollback all migration and applying again",
    )
    args = parser.parse_args()

    return args


def cli():
    """Dispatch function, based on cli arguments."""

    args = parse_cli_args()

    if args.rollback:
        action = _rollback
    elif args.rollback_one:
        action = _rollback_one
    elif args.reload:
        action = _reload
    else:
        action = _apply

    run(action)


if __name__ == "__main__":
    cli()
