

import random
from loguru import logger


class Material:
    materials = ["wood", "metal", "something", "dsp"]

    @classmethod
    def random(cls):
        qty = random.randint(0, 5)
        return [random.choice(cls.materials) for _ in range(qty)]


class _Builder:
    def build(self, material):
        logger.debug(f'[{material:10}] Building material...')


class _Vendor:
    def take_material(self, money):
        logger.debug(f'Taking materials ... Spend {int(money)}')
        return Material.random()


class _Investor:
    def investing(self):
        logger.debug(f'Investing ...')
        return random.randint(0, 5000)


class Facade:
    def __init__(self):
        self.investor = _Investor()
        self.builder = _Builder()
        self.vendor = _Vendor()
        self.money = 0

    def start_project(self):
        for _ in range(2):
            self.money += self.investor.investing()

        for _ in range(3):
            materials = self.vendor.take_material(self.money / 4)
            for material in materials:
                self.builder.build(material)


def main():
    facade = Facade()
    facade.start_project()


if __name__ == '__main__':
    main()
