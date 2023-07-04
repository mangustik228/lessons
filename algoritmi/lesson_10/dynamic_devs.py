from functools import lru_cache
from loguru import logger


@lru_cache
def fib_rec(n):
    return fib_rec(n-1)+fib_rec(n-2) if n > 2 else 1


def fib_loop(n):
    result = [1, 1]
    for _ in range(n-2):
        result.append(sum(result))
        result.pop(0)
    return result[-1]


def smith(n: int):  # Кузнечик
    result = [1, 1]
    for _ in range(n-1):
        result.append(sum(result[-2:]))
    return result


def main():
    logger.debug(fib_rec(7))
    logger.debug(fib_loop(7))
    logger.debug(smith(15))
    logger.debug(5 + int(bool(None)))


if __name__ == '__main__':
    main()
