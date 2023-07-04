

import json

from loguru import logger


class Meta:
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            self.__dict__[key] = value


class Women(Meta):
    title = "Заголовок"
    content = "Контент"
    photo = "Фото"


def main():
    w = Women(title="Hello", content="content", world="jopa")
    pretty_form = json.dumps(w.__dict__, indent=4, ensure_ascii=False)
    logger.debug(pretty_form)
    w.photo


if __name__ == '__main__':
    main()
