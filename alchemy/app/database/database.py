import asyncio
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.config import settings

sync_engine = create_engine(
    settings.db.dsn_psycopg,
    echo=True,  # Пишет параллельно в консоль все запросы
    pool_size=5,  # Максимальное кол-во подключений
    max_overflow=10  # Можно создать дополнительно 10 подключений
)

async_engine = create_async_engine(
    settings.db.dsn_psycopg,
    echo=True,  # Пишет параллельно в консоль все запросы
    pool_size=5,  # Максимальное кол-во подключений
    max_overflow=10  # Можно создать дополнительно 10 подключений
)


with sync_engine.connect() as conn:
    query = text("SELECT VERSION()")
    result = conn.execute(query)
    print(f"{result.mappings().first()}")


async def get_version():
    async with async_engine.connect() as conn:
        query = text("SELECT VERSION()")
        result = await conn.execute(query)
        print(f"{result.scalar()}")


asyncio.run(get_version())
