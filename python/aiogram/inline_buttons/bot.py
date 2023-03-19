from config.config import BOT_TOKEN
from aiogram import Bot, Dispatcher
import asyncio
import handlers

async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(handlers.client.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())