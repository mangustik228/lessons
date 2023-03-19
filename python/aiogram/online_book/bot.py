import json
from config.config import BOT_TOKEN
from loguru import logger
from aiogram import Bot, Dispatcher
import asyncio 
from keyboards import set_main_menu
import handlers


async def main():
    logger.debug(f'start program')
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    dp.startup.register(set_main_menu)
    dp.include_router(handlers.client.router)
    dp.include_router(handlers.other.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
    ...
