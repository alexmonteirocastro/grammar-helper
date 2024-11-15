import os
import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

# This is the Alembic Config object
config = context.config

# Add your models directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Import settings and update config
from app.config import settings

# Import Base and models
from app.database import Base  # Import Base
from app.models.polish_cases import (  # Import your models explicitly
    GrammaticalCase,
    Noun,
    NounForm,
)

config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# Set metadata for migrations
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
