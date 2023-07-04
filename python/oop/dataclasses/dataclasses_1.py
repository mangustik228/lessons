from dataclasses import dataclass, field
from pydantic import BaseModel
from loguru import logger


@dataclass
class Thing:
    name: str
    price: float
    weight: int
    dims: list = field(default_factory=list)


def main():
    thing_1 = Thing(name="table", weight=30, price=35000.)
    thing_2 = Thing(name="table", weight=30, price=35000.)
    logger.debug(thing_1 == thing_2)
    thing_1.dims.append(2)
    thing_2.dims.append(2)
    logger.debug(thing_1 == thing_2)
    thing_2.dims.append(3)
    logger.debug(thing_1)
    logger.debug(thing_2)


if __name__ == '__main__':
    main()
