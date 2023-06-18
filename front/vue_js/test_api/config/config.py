from functools import lru_cache
from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    _db_url: str = './models/database.sqlite'

    @property
    def async_dsn(self):
        return f"sqlite+aiosqlite:///{self._db_url}"

    @property
    def sync_dsn(self):
        return f"sqlite:///{self._db_url}"


@lru_cache
def get_settings() -> Settings:
    return Settings()
