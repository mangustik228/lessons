from loguru import logger


def create_class_point(name: str, base: tuple, attrs: dict[str, any]):
    attrs.update({"MAX_COORD": 100, "MIN_COORD": 12})
    return type(name, base, attrs)


class Point(metaclass=create_class_point):
    def get_coords(self):
        return (self.MAX_COORD, self.MIN_COORD)


def main():
    pt = Point()
    logger.info(pt)
    logger.info(pt.get_coords())
    logger.info(f'{pt.__dict__}')


if __name__ == '__main__':
    main()
