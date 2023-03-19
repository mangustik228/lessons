from aiogram import Router
from lexicon import LEXICON
from aiogram.types import Message

router = Router()

async def echo(message: Message):
    await message.answer(text = LEXICON['echo'])

router.message.register(echo)