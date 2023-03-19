from aiogram.types import BotCommand
from aiogram import Bot
from lexicon import MAIN_MENU

async def set_main_menu(bot: Bot):
    menu_btns = []
    for key, value in MAIN_MENU.items():
        menu_btns.append(
            BotCommand(command=key, description=value)
        )
    await bot.set_my_commands(menu_btns)