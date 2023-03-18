from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter, Text
from aiogram.types import Message 
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
DEBUG = config.get('DEFAULT', 'debug')
BOT_TOKEN = config.get('BOT', 'token')
MY_ID = config.getint('BOT', 'my_id')
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict:
        numbers = []
        for word in message.text.split():
            normalized_word = word.replace('.', '').replace(',', '').strip()
            if normalized_word.isdigit():
                numbers.append(normalized_word)
        if numbers:
            return {"numbers":numbers}
        else: 
            return False
        

async def process_if_numbers(message: Message, numbers: dict):
    await message.answer(f'{numbers}')

async def process_if_not_numbers(message: Message):
    await message.answer(f'No numbers')


dp.message.register(process_if_numbers, NumbersInMessage(), Text(startswith="найди числа", ignore_case=True))
dp.message.register(process_if_not_numbers, Text(startswith="найди числа", ignore_case=True))


dp.run_polling(bot)
