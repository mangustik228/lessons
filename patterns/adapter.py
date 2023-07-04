import json

from loguru import logger

# JSON


class Old:
    @staticmethod
    def get():
        return json.dumps({"method_1": 1})


class New:
    def get(self):
        return {"method_new": 1}


class Adapter(New):
    def get(self):
        return str(super(Adapter, self).get())


def main():
    some = Adapter().get()
    if isinstance(some, str):
        logger.info(f'Получил строку, как и ожидал. {some}')
    if isinstance(some, dict):
        raise TypeError('Ждал словарь')


if __name__ == '__main__':
    main()
