import random
import pytest


@pytest.mark.parametrize(
    'a', [random.randint(0,2) for _ in range(100)]
)
def test_function(a):
    print(f'{a = }')
    assert a != 1 