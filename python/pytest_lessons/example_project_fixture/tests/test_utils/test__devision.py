from app.utils import devision 
from loguru import logger 


def test_just_delete_file(delete_file: callable, wrapper_test):
    logger.debug('start test_some_func')
    delete_file()
    logger.debug('finish test_some_func')


def test_wrapping(wrapper_test):
    logger.debug('start test')
    logger.debug(f'{wrapper_test = }')
    logger.debug('finish test')