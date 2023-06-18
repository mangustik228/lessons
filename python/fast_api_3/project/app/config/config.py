from functools import lru_cache
from pydantic import BaseSettings, AnyUrl
from loguru import logger


class Settings(BaseSettings):
    environment: str
    debug: bool
    database_url: AnyUrl | None


settings = Settings()


@lru_cache
def get_settings() -> Settings:
    logger.info('Loading config settings from the environment')
    return Settings()
