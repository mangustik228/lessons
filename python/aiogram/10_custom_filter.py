from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter
from aiogram.types import Message
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
DEBUG = config.get('DEFAULT', 'debug')
BOT_TOKEN = config.get('BOT', 'token')
MY_ID = config.getint('BOT', 'my_id')
ADMINS = [MY_ID]
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

class isAdmin(BaseFilter):
    def __init__(self, admins: list):
        self.admin_ids = admins 

    async def __call__(self, msg: Message) -> bool:
        return msg.from_user.id in self.admin_ids


async def answer_to_admin(msg: Message):
    print(msg.json(exclude_none=True, indent=4))
    await msg.answer('Hello admin')
    print(msg.json(exclude_none=True, indent=4))

async def answer_to_no_admin(msg: Message):
    print(msg.json(exclude_none=True, indent=4))
    await msg.answer('No Hello admin')


dp.message.register(answer_to_admin, isAdmin(ADMINS))
dp.message.register(answer_to_no_admin)


if __name__ == '__main__':
    dp.run_polling(bot)