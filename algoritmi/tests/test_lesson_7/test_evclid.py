
import pytest
from lesson_7.evclid import evclid


@pytest.mark.parametrize(
    "a,b,result",
    [
        (5, 1, 1),
        (36, 6, 6),
        (21, 6, 3),
        (11, 3, 1),
        (25, 10, 5)
    ]
)
def test_evclid(a, b, result):
    assert evclid(a, b) == result
