import os
from random import randrange
import pytest
from loguru import logger


@pytest.fixture(scope="session", autouse=True)
def create_file_before_test():
    with open('file.txt', 'w') as file:
        file.write('hello')
        logger.debug(f'Создал файл')


def _delete_file_after_test():
    if os.path.exists('file.txt'):
        os.remove('file.txt')
        logger.debug(f'Файл удален')
    else: 
        logger.debug(f'Файла не было')


@pytest.fixture
def delete_file():
    return _delete_file_after_test


@pytest.fixture(scope="session")
def wrapper_test():
    logger.debug("start fixture")
    yield 42 
    logger.debug("finish fixture")