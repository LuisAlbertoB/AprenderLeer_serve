import sys
from os.path import abspath, dirname

# Añade el directorio del proyecto al path de Python
sys.path.insert(0, dirname(dirname(abspath(__file__))))

from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Importa la Base desde tu módulo de database
from app.database import Base  # ¡Asegúrate que este path sea correcto!

config = context.config
fileConfig(config.config_file_name) if config.config_file_name else None

# Conexión CRUCIAL con tus modelos
target_metadata = Base.metadata  # Usa los metadatos registrados

def run_migrations_offline():
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
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()