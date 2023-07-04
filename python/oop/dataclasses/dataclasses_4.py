from dataclasses import make_dataclass

from loguru import logger


CarData = make_dataclass(
    "Car",
    fields=[("model", int), "max_speed", "price"],
    namespace={"get_max_speed": lambda self: self.max_speed})


def main():
    car = CarData(model="BMW", max_speed=5, price=150)
    logger.info(f"{car = }")
    logger.info(car.get_max_speed)


if __name__ == '__main__':
    main()
