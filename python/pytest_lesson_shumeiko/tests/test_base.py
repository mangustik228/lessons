import json
from loguru import logger
from app.main import bar
from app.utils.functions import foo
from app.config.config import settings


def test_settings():
    logger.debug(settings.db)
    assert settings.db.name == "test"


def test_json_file():
    with open('tests/src/some_js.json', 'r') as file:
        data = json.load(file)
    with open('tests/src/new.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
    with open('tests/src/new.json', 'r') as file:
        data = json.load(file)
    logger.debug(data)
