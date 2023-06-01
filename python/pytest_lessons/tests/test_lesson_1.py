from utils.lesson_1 import division
import pytest

# Простые тесты
@pytest.mark.parametrize(
    "a, b, expected_result", [
    (10, 2, 5),
    (12, 3, 4),
    (16, 4, 4),
    (20, 5, 4),
    (1,  2, 0.5)
    ])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize(
        "a, b, excepted_exception",[
            (10,0,ZeroDivisionError),
            ('a',2,TypeError)
        ]
)
def test_division_error(a, b, excepted_exception):
    with pytest.raises(excepted_exception):
        division(a, b)


def test_equal():
    assert 1 == 1, "Not equal!!!!"


def test_error():
    assert 1 != 2, "example of error message"