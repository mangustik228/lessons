from configparser import ConfigParser
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from loguru import logger


config = ConfigParser()
config.read('config.ini')
TOKEN = config.get('BOT', 'bot_token')
DEBUG = config.getboolean('DEFAULT', 'debug')
bot = Bot(TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    '''Функция которая всегда отрабатывает при старте'''
    logger.info('BOT START')


@dp.message_handler(commands=['start','help'])
async def command_start(message: types.Message):
    try: 
        await bot.send_message(message.from_user.id, 'You are started bot')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите мне')


@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'среда 13-14')


@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Ленина')


if DEBUG:
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)