import config.db as db

from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config.config import token
from keyboards.replies import *
from keyboards.inlines import *
from states.mailing import bot_mailing

storage = MemoryStorage()
bot = Bot(token, parse_mode='markdown')
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(text='mail')
async def start_mailing(message):
    rows = db.cursor.execute('SELECT id FROM users').fetchall()
    await message.answer(f'⚡ Введи текст для розсилки з *Markdown-маркуванням*:\n\nНаразі в боті `{len(rows)}` користувачів')
    await bot_mailing.text.set()



@dp.message_handler(state=bot_mailing.text)
async def mailing_text(message, state: FSMContext):
    answer = message.text
    await state.update_data(text=answer)
    await message.answer(text=answer, reply_markup=menuMailing)
    await bot_mailing.state.set()


@dp.callback_query_handler(text='next', state=bot_mailing.state)
async def startma(call, state: FSMContext):
    rows = db.cursor.execute('SELECT id FROM users').fetchall()
    data = await state.get_data()
    text = data.get('text')
    for row in rows:
        try:
            
            await bot.send_message(row[0], text=text)
        except Exception:
            pass
    await call.message.answer('Успішна розсилка!')


@dp.callback_query_handler(text='add_photo', state=bot_mailing.state)
async def add_photo(call):
    await call.message.answer('Надішли фото')
    await bot_mailing.photo.set()


@dp.message_handler(state=bot_mailing.photo, content_types=types.ContentType.PHOTO)
async def mailing_photo(message, state: FSMContext):
    photo_file_id = message.photo[-1].file_id
    await state.update_data(photo=photo_file_id)
    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo')
    await message.answer_photo(photo=photo, caption=text, reply_markup=menuMailing2)


@dp.callback_query_handler(text='next', state=bot_mailing.photo)
async def startm(call, state: FSMContext):
    rows = db.cursor.execute('SELECT id FROM users').fetchall()
    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo')
    for row in rows:
        try:
            await bot.send_photo(row[0], photo=photo, caption=text)
        except Exception:
            pass
    await call.message.answer('Успішна розсилка!')
    

@dp.message_handler(state=bot_mailing.text)
async def no_photo(message):
    await message.answer('Надішли фото', reply_markup=menuCancel)


@dp.callback_query_handler(text='quit', state=[bot_mailing.text, bot_mailing.photo, bot_mailing.state])
async def quit(call, state: FSMContext):
    await state.finish()
    await call.message.answer('Розсилка відмінена')


def register_handlers_mailing(dp: Dispatcher):
    dp.register_message_handler(start_mailing, text='mail')
    dp.register_message_handler(mailing_text, state=bot_mailing.text)
    dp.register_callback_query_handler(startma, text='next', state=bot_mailing.state)
    dp.register_callback_query_handler(add_photo,text='add_photo', state=bot_mailing.state)
    dp.register_message_handler(mailing_photo, state=bot_mailing.photo, content_types=types.ContentType.PHOTO)
    dp.register_callback_query_handler(startm, text='next', state=bot_mailing.photo)
    dp.register_message_handler(no_photo, state=bot_mailing.text)
    dp.register_callback_query_handler(quit, text='quit', state=[bot_mailing.text, bot_mailing.photo, bot_mailing.state])

