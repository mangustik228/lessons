from functools import lru_cache
import os
from typing import Literal
from pydantic import BaseSettings
from configparser import ConfigParser
from dotenv import load_dotenv


load_dotenv()

_config_ini = ConfigParser()
_config_ini.read('config.ini')


class _Database(BaseSettings):
    name: str
    host: str
    port: str
    user: str
    pasw: str

    class Config:
        env_prefix = "TEST_DB_" if os.getenv("MODE") == "test" else "DB_"
        case_sensitive = False


class _Settings(BaseSettings):
    MODE: Literal['dev', "test", "prod"]
    version: str = _config_ini.get('default', 'version')
    db: _Database = _Database()


settings = _Settings()
