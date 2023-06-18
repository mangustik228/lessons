import time
from loguru import logger
import pytest
from app.utils import devision



@pytest.mark.skip('Просто скипнуть тест')
def test_some_test():
    ...

@pytest.mark.parametrize(
    'a,b,result',[
        (2,1,2),
        (5,2,2.5),
        (8,2,4)
    ])
def test_devision(a,b,result):
    assert devision(a,b) == result

def test_error():
    time.sleep(1)
    with pytest.raises(TypeError): 
        devision(1,'a')


def test_zero_devizion():
    with pytest.raises(ZeroDivisionError, match='division by zero'):
        devision(1,0)