import pytest
from lesson_16.firma_simple_number import ferma, check_simple


@pytest.mark.parametrize(
    "n, result",
    [
        (1, True),
        (2, True),
        (5, True),
        (25, False),
        (33, False),
        (11, True),
        (83, True),
        (4, False)
    ]
)
def test_ferma(n, result):
    assert ferma(n) == result


@pytest.mark.parametrize(
    "n, result",
    [
        (1, True),
        (2, True),
        (5, True),
        (25, False),
        (33, False),
        (11, True),
        (83, True),
        (4, False)
    ]
)
def test_check_simple(n, result):
    assert check_simple(n) == result
