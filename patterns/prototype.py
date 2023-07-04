
from loguru import logger


class Address:
    def __init__(self, country: str, city: str, street_address: str):
        self.street_address = street_address
        self.city = city
        self.country = country

    def __str__(self):
        return f"country {self.country}. city {self.city}\n{self.street_address}"


class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    def __str__(self):
        return f'--- {self.name} ---\nLives at {self.address}'


def main():
    john = Person("John", Address("Russia", "Moscow", "Yaltinskay str.10"))
    logger.debug(f'\n{john}')


if __name__ == '__main__':
    main()
