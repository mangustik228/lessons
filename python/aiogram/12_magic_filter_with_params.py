from aiogram import Bot, Dispatcher, F
from aiogram.filters import BaseFilter, Text
from aiogram.types import Message, PhotoSize
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
DEBUG = config.get('DEFAULT', 'debug')
BOT_TOKEN = config.get('BOT', 'token')
MY_ID = config.getint('BOT', 'my_id')
bot = Bot(BOT_TOKEN)
dp = Dispatcher()


async def process_if_photo(message: Message, photo_min: PhotoSize):
    print(photo_min)
    await message.answer_photo(photo_min.file_id)

dp.message.register(process_if_photo, F.photo[0].as_('photo_min'))


dp.run_polling(bot)
