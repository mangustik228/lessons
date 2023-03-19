from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def url_buttons():
    url_btn_1 = InlineKeyboardButton(
        text ='link to stepik',
        url = 'https://stepik.org/120924'
        )
    url_btn_2 = InlineKeyboardButton(
        text = 'link to my web site',
        url = 'http://mangust228.ru'
        )
    kb = InlineKeyboardMarkup(inline_keyboard=[[url_btn_1],[url_btn_2]])
    return kb


def callback_buttons():
    btn_1 = InlineKeyboardButton(
        text='btn_1',
        callback_data='callback_data_1'
    )
    btn_2 = InlineKeyboardButton(
        text='btn_2',
        callback_data='callback_data_2'
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[[btn_1, btn_2]])
    return kb

def inline_builder():
    kb_builder = InlineKeyboardBuilder()
    btns = [InlineKeyboardButton(text=f'btn_{i}', callback_data=f'callback_{i}') for i in range(10)]
    kb_builder.row(*btns, width=2)
    return kb_builder.as_markup()