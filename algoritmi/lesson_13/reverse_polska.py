from loguru import logger
from .structures import MyStack

# Алгоритм вычисления выражений в постфиксной нотации.
# [5,2,"+"] <=> 5+2
# [2,7,"+",5,"*"] <=> ( 2 + 7 ) * 5
# [2,7,5,"*","+"] <=> 2 + 7 * 5


def polska_notation(lst: list) -> int:
    stack = MyStack()
    for el in lst:
        if isinstance(el, int | float):
            stack.push(el)
            continue
        assert el in "+-/*"
        stack.calculate(el)
    return stack.pop()
