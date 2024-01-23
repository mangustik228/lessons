'''
example with exception
'''

from typing import Callable, Generator

from traitlets import Any


def coroutine(func: Callable[..., Generator[Any, None, None]]):
    def inner(*args, **kwargs) -> Generator:
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


@coroutine
def average():
    count = 0
    summ = 0
    average = None
    while True:
        try:
            value = yield average
        except StopIteration:
            print("Done")
            break
        else:
            count += 1
            summ += value
            average = round(summ / count, 2)
    return average


a = average()
for i in range(15):
    result = a.send(i)
    print(result)
    try:
        a.throw(StopIteration)
    except StopIteration as e:
        print("Average", e.value)
        break
