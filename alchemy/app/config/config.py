import os
from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict
import dotenv

dotenv.load_dotenv()


def get_prefix():
    return "TEST_DB_" if os.getenv("MODE") == "TEST" else "DB_"


class _Database(BaseSettings):
    model_config = SettingsConfigDict(env_prefix=get_prefix())
    host: str
    port: int
    name: str
    user: str
    password: str

    @property
    def dsn_psycopg(self):
        return f"postgresql+psycopg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"

    @property
    def dsn_asyncpg(self):
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


class _Settings(BaseSettings):
    db: _Database = _Database()
    MODE: Literal["DEV", "TEST", "PROD"]


settings = _Settings()
