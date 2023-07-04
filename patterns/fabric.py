from math import cos, sin

from loguru import logger


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @staticmethod
    def new_cartesiona_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))

    def __repr__(self):
        return f'x = {self.x:8.4f} | y = {self.y:8.4f}'


def main():
    point_1 = Point.new_cartesiona_point(1, 2)
    point_2 = Point.new_polar_point(1, 2)
    logger.debug(f'\n{point_1 = }\n{point_2 = }')


if __name__ == '__main__':
    main()
