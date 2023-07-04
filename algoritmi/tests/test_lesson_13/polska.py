import pytest
from lesson_13.reverse_polska import polska_notation


@pytest.mark.parametrize(
    "lst, result",
    [
        ([5, 2, "+"], 7),
        ([2, 7, 5, "*", "+"], 37),
        ([2, 7, "+", 5, "*"], 45),
        ([5, 2, "-"], 3)
    ]
)
def test_polska_notation(lst, result):
    assert polska_notation(lst) == result
