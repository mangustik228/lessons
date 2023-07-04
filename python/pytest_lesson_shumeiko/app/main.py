from typing import Literal
from loguru import logger
from app.utils.functions import foo
import app.utils as utils
from pydantic import BaseSettings
from dotenv import load_dotenv
from app.config.config import settings


class _Settings(BaseSettings):
    MODE: Literal['dev', "test", "prod"]


def main():
    logger.debug(settings.db)


def bar():
    return 5


if __name__ == '__main__':
    main()
