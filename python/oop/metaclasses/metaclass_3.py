from loguru import logger


class Meta(type):
    def __new__(cls,  name, base, attrs: dict):
        attrs.update({"MAX_COORD": 100, "MIN_COORD": 0})
        return type.__new__(cls, name, base, attrs)


class Point(Meta):
    def get_coords(self):
        return (0, 0)


def main():
    pt = Point()
    logger.debug(f'{pt.get_coords()}')
    logger.success(f'{pt.__dict__}')


if __name__ == '__main__':
    main()
