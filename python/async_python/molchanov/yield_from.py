'''
yield from 
'''


from functools import wraps
from typing import Any, Callable, Generator


def coro(func):
    @wraps(func)
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


def subgen():
    msg = None
    while True:
        try:
            msg = yield msg
        except StopIteration:
            print("my_exception coming")
            break
        if msg == "world":
            break
    return 42


@coro
def delegator(g: Generator):
    result = yield from g
    yield result


s = subgen()
d = delegator(s)

for i in ["hello", "jopa", "world"]:
    result = d.send(i)
    print(result)
