from configparser import ConfigParser
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


config = ConfigParser()
config.read('config.ini')
DEBUG = config.get('DEFAULT', 'debug')
BOT_TOKEN = config.get('BOT', 'token')
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

async def process_start_command(message: Message):
    await message.answer('hello! You are started bot!')

async def process_help_command(message: Message):
    await message.answer('This is help')

async def echo(message: Message):
    await message.answer(message.text)


dp.message.register(process_help_command, Command(commands=['help']))
dp.message.register(process_start_command, Command(commands=['start']))
dp.message.register(echo)

if __name__ == '__main__':
    dp.run_polling(bot)