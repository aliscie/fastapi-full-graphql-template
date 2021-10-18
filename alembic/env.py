import os
from logging.config import fileConfig

import fastapi
from dotenv import load_dotenv
from icecream import ic
from sqlalchemy import engine_from_config, pool

from alembic import context

from Users import models

#TODO dynamic import apps
# import importlib
# from core.settings import APPS
# for i in APPS:
#     x = importlib.import_module(f'{i}.main')
#     target_metadata = x.models.Base.metadata
from celery_sqlalchemy_scheduler.models import ModelBase
target_metadata = [models.Base.metadata, ModelBase.metadata]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

config = context.config

config.set_main_option("sqlalchemy.url", os.environ["DATABASE_URL"])

fileConfig(config.config_file_name)


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
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
