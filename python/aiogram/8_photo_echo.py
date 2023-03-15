from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
DEBUG = config.get('DEFAULT', 'debug')
BOT_TOKEN = config.get('BOT', 'token')


bot = Bot(BOT_TOKEN)
dp = Dispatcher()


async def start_command(message: Message):
    await message.reply('what do you want')


async def send_photo_echo(message:Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)




async def send_any_echo(message:Message):
    await message.answer(f'msg from {message.from_user.id}')
    try:
        await message.send_copy(chat_id=message.from_user.id)
    except Exception as e:
        await message.reply(f'Данный тип сообщения не поддерживается методом send_copy')

dp.message.register(start_command, Command(commands=['start']))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_any_echo)

if __name__ == '__main__':
    dp.run_polling(bot)