from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, JSON
from datetime import datetime

# Команда для инициализации миграции `alembic init migrations`
# 
# Меняем в `alembic.ini` на актуальный(пример):
# sqlalchemy.url = mysql://%(DB_USER)s:%(DB_PASS)s@%(DB_HOST)s:%(DB_PORT)s/%(DB_NAME)s
# 
# В файле migrations/env.py:
# from models.models import metadata
# ...
# section = config.config_ini_section
# config.set_section_option(section, "DB_HOST", DB_HOST)
# config.set_section_option(section, "DB_PORT", DB_PORT)
# config.set_section_option(section, "DB_USER", DB_USER)
# config.set_section_option(section, "DB_NAME", DB_NAME)
# config.set_section_option(section, "DB_PASS", DB_PASS)
# ...
# target_metadata = metadata
# 
# Создаем бд
# alembic revision --autogenerate -m "Database creation"
# 
# Создаем миграцию
# alembic upgrade ХЕШ_ВЕРСИИ (берем из version)





metadata = MetaData()

roles = Table(
    'roles',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('permissions', JSON)
)

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String, nullable=False),
    Column('username', String, nullable=False),
    Column('password', String, nullable=False),
    Column('registered_at', TIMESTAMP, default=datetime.utcnow),
    Column('role_id', Integer, ForeignKey('roles.id'))
)
