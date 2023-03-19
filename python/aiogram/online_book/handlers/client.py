from copy import deepcopy
from loguru import logger
from aiogram import Router
from aiogram.filters import Command, CommandStart, Text 
from aiogram.types import Message, CallbackQuery
from database import user_dict_template,user_db
from filters import IsDelBookmarkCallbackData, IsDigitCallbackData
from keyboards import (create_edit_keyboard,
                       create_bookmarks_keyboard,
                       create_pagination)
from lexicon import LEXICON
from utils import BOOK


router = Router()


async def command_start(message: Message):
    await message.delete()
    await message.answer(LEXICON['/start'])
    if message.from_user.id not in user_db:
        logger.info(f'Добавлен новый юзер')
        user_db[message.from_user.id] = deepcopy(user_dict_template)


async def command_help(message: Message):
    await message.delete()
    await message.answer(text = LEXICON['/help'])


async def command_beginning(message: Message):
    user_db[message.from_user.id]['page'] = 1 
    text = BOOK[user_db[message.from_user.id]['page']]
    await message.answer(
        text=text,
        reply_markup=create_pagination(
            'backward',
            f'{user_db[message.from_user.id]["page"]}/{len(BOOK)}',
            'forward'
        )
    )

async def command_continue(message: Message):
    text = BOOK[user_db[message.from_user.id]['page']]
    await message.answer(
        text=text,
        reply_markup=create_pagination(
            'backward',
            f'{user_db[message.from_user.id]["page"]}/{len(BOOK)}',
            'forward'
        )
    )


async def command_bookmarks(message: Message):
    logger.info(f'{user_db[message.from_user.id]}')
    if user_db[message.from_user.id]['bookmarks']:
        logger.info(f'{user_db[message.from_user.id]}')
        await message.answer(
            text=LEXICON[message.text],
            reply_markup=create_bookmarks_keyboard(
                *user_db[message.from_user.id]['bookmarks']
            )
        )

async def press_forward(cb: CallbackQuery):
    if user_db[cb.from_user.id]['page'] < len(BOOK):
        user_db[cb.from_user.id]['page'] += 1 
        text = BOOK[user_db[cb.from_user.id]['page']]
        await cb.message.edit_text(
            text=text,
            reply_markup=create_pagination(
                'backward',
                f'{user_db[cb.from_user.id]["page"]}/{len(BOOK)}', 
                'forward'
            )
        )
    await cb.answer()


async def press_backward(cb: CallbackQuery):
    logger.info(f'{user_db[cb.from_user.id]["page"] = }')
    if user_db[cb.from_user.id]['page'] > 1:
        user_db[cb.from_user.id]['page'] -= 1 
        text = BOOK[user_db[cb.from_user.id]['page']]
        await cb.message.edit_text(
            text=text,
            reply_markup=create_pagination(
                'backward',
                f'{user_db[cb.from_user.id]["page"]}/{len(BOOK)}', 
                'forward'
            )
        )
    await cb.answer()


async def press_page(cb:CallbackQuery):
    logger.info(f'{cb.data}')
    user_db[cb.from_user.id]['bookmarks'].add(int(cb.data.split('/')[0])) 
    logger.info(f'{user_db[cb.from_user.id]}')
    await cb.answer()


async def press_bookmark(cb: CallbackQuery):
    text = BOOK[int(cb.data.split('/')[0])]
    user_db[cb.from_user.id]['page'] = int(cb.data.split('/')[0])
    await cb.message.edit_text(
        text=text,
        reply_markup=create_pagination(
            'backward',
            f'{user_db[cb.from_user.id]["page"]}/{len(BOOK)}',
            'forward'
        )
    )
    await cb.answer()

async def press_edit(cb: CallbackQuery):
    await cb.message.edit_text(
        text=LEXICON[cb.data],
        reply_markup=create_edit_keyboard(
            *user_db[cb.from_user.id]['bookmarks']
        )
    )
    await cb.answer()


async def press_cancel(cb: CallbackQuery):
    await cb.message.edit_text(text=LEXICON['cancel_text'])
    await cb.answer()


async def press_del_bookmark(cb: CallbackQuery):
    user_db[cb.from_user.id]['bookmarks'].remove(int(cb.data[:-3]))
    if user_db[cb.from_user.id]['bookmarks']:
        await cb.message.edit_text(
            text=LEXICON['/bookmarks'],
            reply_markup=create_edit_keyboard(
                *user_db[cb.from_user.id]['bookmarks']
            )
        )
    else:
        await cb.message.edit_text(text=LEXICON['no_bookmarks'])
    await cb.answer()



router.message.register(command_start, CommandStart())
router.message.register(command_help, Command('help'))
router.message.register(command_beginning, Command('beginning'))
router.message.register(command_continue, Command('continue'))
router.message.register(command_bookmarks, Command('bookmarks'))
router.callback_query.register(press_forward, Text(text='forward'))
router.callback_query.register(press_backward, Text(text='backward'))
router.callback_query.register(press_page, 
                               lambda x: '/' in x.data and x.data.replace('/', '').isdigit())
router.callback_query.register(press_bookmark, IsDigitCallbackData())
router.callback_query.register(press_edit, Text(text='edit_bookmarks'))
router.callback_query.register(press_cancel, Text(text='cancel'))
router.callback_query.register(press_del_bookmark, IsDelBookmarkCallbackData())
