from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon import LEXICON

def create_pagination(*buttons: str) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    btns = []
    for btn in buttons:
        btns.append(InlineKeyboardButton(
            text=LEXICON.get(btn, btn),
            callback_data=btn
        ))
    kb_builder.row(*btns)
    return kb_builder.as_markup()