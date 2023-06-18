from config.config import get_settings
from loguru import logger


def test_db_connection():
    assert "sqlite" in get_settings().sync_dsn
    assert "models" in get_settings().async_dsn
