from functools import lru_cache
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class _DbConnection(BaseSettings):
    DB_HOST: str
    DB_USER: str
    DB_PASS: str
    DB_PORT: str
    DB_NAME: str

    @property
    def dsn(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    @property
    def dsn_sync(self):
        return f'postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


class Settings(BaseSettings):
    db: _DbConnection = _DbConnection()


@lru_cache
def get_settings():
    return Settings()
