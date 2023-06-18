from typing import AsyncGenerator
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from config.config import get_settings

engine = create_async_engine(get_settings().async_dsn)

async_session_maker = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=True  # Удаление объектов после commita... А иногда это не нужно
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

Base = declarative_base()


class DatabaseCv(Base):
    __tablename__ = "cv"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    text = Column(String)
    user_id = Column(Integer)
