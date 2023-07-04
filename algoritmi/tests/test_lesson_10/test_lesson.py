from loguru import logger
from lesson_10.binary_search import binary_search
from lesson_10.dynamic_devs import fib_loop, fib_rec
import pytest


@pytest.mark.parametrize(
    'lst, search, result',
    [
        ([1, 2, 3, 4, 5, 6, 7], 3, 2),
        ([1, 4, 5, 6, 7, 8, 9, 10], 5, 2),
        ([1, 2, 3, 4, 5, 6, 7], 10, 6),
        ([1, 2, 3, 4, 5, 6, 7], -1, 0),
        ([1, 7], 2, 1),
    ]
)
def test_binary_search(lst, search, result):
    assert binary_search(lst, search) == result


@pytest.mark.parametrize(
    'n, result',
    [
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (10, 55)
    ]
)
def test_fib(n, result):
    assert fib_loop(n) == result
    assert fib_rec(n) == result
