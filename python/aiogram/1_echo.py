from configparser import ConfigParser
from aiogram import Bot, types 
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


config = ConfigParser()
config.read('config.ini')
DEBUG = config.getboolean('DEFAULT', 'debug')
TOKEN = config.get('BOT', 'bot_token')

bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, 'hello')


@dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer(message.text) # Ответ
    await message.reply(message.text) # с цитатой
    await bot.send_message(message.from_user.id, message.text) # Написать личное



if DEBUG:
    executor.start_polling(dp, skip_updates=True)