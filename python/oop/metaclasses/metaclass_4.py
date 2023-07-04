
import json
from loguru import logger


class Meta(type):

    def create_local_attrs(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

    def __init__(cls, name, bases, attrs: dict):
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs


class Women(metaclass=Meta):
    title = "Заголовок"
    content = "Контент"
    photo = "Фото"


def main():
    w = Women()
    pretty_form = json.dumps(w.__dict__, indent=4, ensure_ascii=False)
    logger.debug(pretty_form)
    w.photo


if __name__ == '__main__':
    main()
