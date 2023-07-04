import pytest
from codewars_3 import score


@pytest.mark.parametrize(
    "value, result",
    [
        ([5, 1, 3, 4, 1], 250),
        ([1, 1, 1, 3, 1], 1100),
        ([2, 3, 4, 6, 2], 0),
        ([4, 4, 4, 3, 3], 400),
        ([2, 4, 4, 5, 4], 450),
    ]
)
def test_score(value, result):
    assert score(value) == result
