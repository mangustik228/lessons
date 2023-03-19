from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon import LEXICON
from utils import BOOK

def create_bookmarks_keyboard(*args: int) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    # Наполнение клавиатуры закладками
    for btn in sorted(args):
        kb_builder.row(InlineKeyboardButton(
            text=f'{btn} - {BOOK[btn][:100]}',
            callback_data=str(btn)
        ))
    # Добавление кнопок редактирования и Отменить
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON['edit_bookmarks_button'],
            callback_data='edit_bookmarks'
        ),
        InlineKeyboardButton(
            text=LEXICON['cancel'],
            callback_data='cancel'
        ),
        width=2
    )
    return kb_builder.as_markup()

def create_edit_keyboard(*args: int) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопка закладками 
    for button in sorted(args):
        kb_builder.row(
            InlineKeyboardButton(
                text=f'{LEXICON["del"]} {button} - {BOOK[button][:100]}',
                callback_data=f'{button}del'
            )
        )
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON['cancel'],
            callback_data='cancel'
        )
    )
    return kb_builder.as_markup()



