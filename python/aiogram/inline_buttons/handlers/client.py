from aiogram import Router, F 
from aiogram.types import Message, CallbackQuery
import keyboards

router = Router()




async def greeting_message(message: Message):
    await message.answer(text='privet')


async def url_buttons(message: Message):
    await message.answer(
        text='Это тест инлайн-кнопок', 
        reply_markup=keyboards.client.url_buttons())


async def echo(message: Message):
    await message.answer(text='echo')


async def callback_buttons(message: Message):
    await message.answer(
        text='Это тест callback-кнопок',
        reply_markup=keyboards.client.callback_buttons())


async def press_first_callback_button(callback: CallbackQuery):
    await callback.answer(text=f'{callback.data = }')
    await callback.answer(text='it was first button')


async def press_second_callback_button(callback: CallbackQuery):
    await callback.answer(text='It second button', show_alert=True)


async def inline_builder(message: Message):
    await message.answer(text='this message create with InlineKeyboardBuilder',
                         reply_markup=keyboards.client.inline_builder())


router.message.register(greeting_message, F.text == "hello world")
router.message.register(url_buttons, F.text == "url")
router.message.register(callback_buttons, F.text == "callback")
router.message.register(inline_builder, F.text == 'builder')
router.callback_query.register(press_first_callback_button, F.data == 'callback_data_1')
router.callback_query.register(press_second_callback_button, F.data == 'callback_data_2')
router.message.register(echo)