from typing import Iterable
from utils.lesson_5 import getting_post, url
from tests.src.schemas import Post


def test_getting_post():
    result = getting_post(url)
    if isinstance(result, Iterable):
        for item in result:
            Post.validate(item)