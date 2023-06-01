import pytest

@pytest.fixture
def say_hello():
    print('hello_world', end='')
    return 14

