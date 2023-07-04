from codewars_2 import make_readable


import pytest


@pytest.mark.parametrize(
    "value, result",
    [
        (0, "00:00:00"),
        (5, "00:00:05"),
        (60, "00:01:00"),
        (86399, "23:59:59"),
        (359999, "99:59:59"),
    ]
)
def test_make_readable(value, result):
    assert make_readable(value) == result
    assert make_readable(value) == result
    assert make_readable(value) == result
    assert make_readable(value) == result
    assert make_readable(value) == result
