from dataclasses import dataclass, field
from typing import Any
import uuid

from loguru import logger


class GoodsMethodsFactory:
    @staticmethod
    def get_init_measure():
        return [0, 0, 0]


@dataclass
class Product:
    uid: Any
    price: Any = None
    weight: Any = None


@dataclass
class Book(Product):
    title: str = ''
    author: str = ''
    price: float | int = 0
    weight: int | float = 0
    measure: list = field(
        default_factory=GoodsMethodsFactory.get_init_measure)


def main():
    b = Book(uuid.uuid4(), price=25, weight=3.2, title="Hello", author="world")
    logger.info(b)


if __name__ == '__main__':
    main()
