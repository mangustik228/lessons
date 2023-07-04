from typing import AsyncGenerator
from loguru import logger
from app.config.config import get_settings
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


class Base(DeclarativeBase):
    ...


engine = create_async_engine(get_settings().db.dsn)

async_session_maker = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False)


async def get_session():
    async with async_session_maker() as session:
        yield session
    logger.debug(f'session closed')
