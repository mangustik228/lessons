from random import randint 
from lexicon import LEXICON_RU
from aiogram.types import Message

def bot_turn():
    return [LEXICON_RU['stone'],LEXICON_RU['scissors'],LEXICON_RU['peppers']][randint(0,2)]

def check_win(message: Message):
    bot_result = bot_turn()
    if bot_result == message.text:
        return bot_result, 'retry'
    if bot_result == LEXICON_RU['stone']:
        return bot_result, check_stone_win(message)
    if bot_result == LEXICON_RU['scissors']:
        return bot_result, check_scrissors_win(message)
    if bot_result == LEXICON_RU['peppers']:
        return bot_result, check_pepper_win(message)
    

def check_stone_win(message: Message):
    return 'win' if message.text == LEXICON_RU['peppers'] else 'lose'

def check_scrissors_win(message: Message):
    return 'win' if message.text == LEXICON_RU['stone'] else 'lose'

def check_pepper_win(message: Message):
    return 'win' if message.text == LEXICON_RU['scissors'] else 'lose'


