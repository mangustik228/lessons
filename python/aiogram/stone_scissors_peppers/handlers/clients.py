from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import Router, F
from aiogram.filters import CommandStart, Command, Text
from lexicon import LEXICON_RU
from keyboards import answer_kb, game_kb
from service import check_win

router = Router()


async def process_start(message: Message):
    await message.answer(LEXICON_RU['question'], reply_markup=answer_kb())

async def start_game(message: Message):
    await message.delete()
    await message.answer('Ходи', reply_markup=game_kb())

async def turn_game(message: Message):
    bot_result, result = check_win(message)
    await message.answer(text= f'Я кинул {bot_result}')
    if result == 'win':
        await message.answer(text = LEXICON_RU['win'], reply_markup=answer_kb())
    if result == 'lose':
        await message.answer(text = LEXICON_RU['lose'], reply_markup=answer_kb())
    if result == 'retry':
        await message.answer(text = LEXICON_RU['retry'], reply_markup=game_kb())

async def finish_game(message: Message):
    await message.answer(text='Ну ок, если что пиши', reply_markup=ReplyKeyboardRemove())


async def empty_message(message: Message):
    await message.answer(text=LEXICON_RU['empty_message'], reply_markup=game_kb())



router.message.register(process_start, CommandStart())
router.message.register(start_game, Text(LEXICON_RU['start_game']))
router.message.register(turn_game, F.text.in_(
    {LEXICON_RU['stone'], LEXICON_RU['scissors'], LEXICON_RU['peppers']}))
router.message.register(finish_game, F.text == LEXICON_RU['no_game'])
router.message.register(empty_message)