import pytest
from lesson_12.livenstein import livenstein


@pytest.mark.parametrize(
    "A,B,result",
    [
        ('молоко', 'колокол', 2),
        ('мир', 'грызня', 6),
        ("кот", "крот", 1)
    ]
)
def test_livenstein(A, B, result):
    assert result == livenstein(A, B)
