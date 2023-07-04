

from dataclasses import InitVar, dataclass, field

from loguru import logger


@dataclass
class Vector3D:
    x: int = field(repr=False)  # Не будет отображаться
    y: int = field(compare=False)  # Не будет участвовать при сравнении
    z: int
    calc_len: InitVar[bool] = False
    # Нужно чтоб добавить в __repr__()
    length: float = field(init=False, compare=False, default=0)

    def __post_init__(self, calc_len: bool):
        if calc_len:
            self.length = (self.x**2 + self.y**2 + self.z**2)**0.5
        self.perimetr = self.x + self.y + self.z


def main():
    obj = Vector3D(1, 2, 3)
    obj2 = Vector3D(1, 3, 3)
    # Не добавляет потому что __repr__ обозначился раньше.
    logger.info(f'{obj}')
    logger.info(f'{obj2}')
    logger.info(
        f'is equal? {obj == obj2}. Because y and length: compare: False ')
    logger.info(
        f'{obj.length = }. This is zero because you we use InitVar! look to code ')


if __name__ == '__main__':
    main()
