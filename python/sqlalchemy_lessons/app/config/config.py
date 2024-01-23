from pydantic import BaseModel
from pydantic_settings import BaseSettings
from configparser import ConfigParser
from dotenv import load_dotenv
from typing import Literal

load_dotenv()

CONFIG_PATH = "config.ini"

_config_ini = ConfigParser()
_config_ini.read(CONFIG_PATH)


class _Logs(BaseModel):
    rotation: str = _config_ini.get('logs', 'rotation')
    level: str = _config_ini.get('logs', 'level')
    telegram: bool = _config_ini.getboolean('logs', 'telegram')
    retention: bool = _config_ini.get('logs', 'retention')


class _Settings(BaseSettings):
    MODE: Literal['DEV', "TEST", "PROD"] = 'DEV'
    logs: _Logs = _Logs()
    name: str = _config_ini.get('default', 'name')


settings = _Settings()
