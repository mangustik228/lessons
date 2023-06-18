from typing import Literal
from src.enums.user_enums import Statuses
from faker import Faker


class PlayerLocalization:
    def __init__(self, lang: Literal["en_EN", "ru_RU"] = "en_EN"):
        self.faker = Faker(locale=lang)
        self.result = {
            "nickname": self.faker.first_name()
        }

    def build(self):
        return self.result


class Player:
    def __init__(self) -> None:
        self.result = {
            "localize": {
                "en": PlayerLocalization("en_EN").build(),
                "ru": PlayerLocalization("ru_RU").build(),
            }
        }

    def reset(self):
        self.set_status().set_balance().set_avatar()
        return self

    def set_status(self, status=Statuses.ACTIVE.value):
        self.result["accout_status"] = status
        return self

    def set_balance(self, balance: int = 0):
        self.result['balance'] = balance
        return self

    def set_avatar(self, avatar: str = "https://google.com/"):
        self.result['avatar'] = avatar
        return self

    def build(self):
        return self.result


z = Player().build()
print(f'{z = }')
