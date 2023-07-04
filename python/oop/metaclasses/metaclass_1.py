

from loguru import logger


def method_1(self):
    logger.success(self.__dict__)


class Some:
    ...


def main():
    A = type("Point", (), {"x": 100, "y": 50})
    pt = A()
    logger.info(f'{type(A) = }')
    logger.info(f'{A = }')
    logger.info(f"{A.x = }")
    logger.info(f'{pt.x =}')

    B = type("NewClass", (Some,), {"x": 50, "my_method": method_1})
    B().my_method()


if __name__ == '__main__':
    main()
