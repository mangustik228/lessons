import asyncio
from aiogram import Bot, Dispatcher 
from config.config import config
import handlers


async def main():
    bot = Bot(config.bot.token)
    dp = Dispatcher()


    dp.include_router(handlers.clients.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())