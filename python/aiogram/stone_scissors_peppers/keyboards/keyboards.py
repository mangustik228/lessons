from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon import LEXICON_RU

def answer_kb():
    kb_builder = ReplyKeyboardBuilder()
    btn_1 = KeyboardButton(text = LEXICON_RU['start_game'])
    btn_2 = KeyboardButton(text = LEXICON_RU['no_game'])
    kb_builder.row(btn_1, btn_2)
    return kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

def game_kb():
    kb_builder = ReplyKeyboardBuilder()
    btn_1 = KeyboardButton(text=LEXICON_RU['stone'])
    btn_2 = KeyboardButton(text=LEXICON_RU['scissors'])
    btn_3 = KeyboardButton(text=LEXICON_RU['peppers'])
    kb_builder.row(btn_1, btn_2, btn_3)
    return kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
