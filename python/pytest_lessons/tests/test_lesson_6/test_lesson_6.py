from utils.lesson_6 import some_func, url 
from tests.src.schemas.lesson_6 import ResponseLesson

def test_some_func():
    response = some_func(url)
    assert ResponseLesson(**response) 