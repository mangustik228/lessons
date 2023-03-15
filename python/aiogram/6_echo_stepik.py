from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message 
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
DEBUG = config.get('DEFAULT', 'debug')
BOT_TOKEN = config.get('BOT', 'token')

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('hello')

@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('hmm...')

@dp.message()
async def send_echo(message: Message):
    await message.reply(message.text)

if __name__ == '__main__':
    dp.run_polling(bot)