import config.db as db

from aiogram import Bot, Dispatcher
from datetime import datetime
from config.config import token, admin_oleksandr
from keyboards.replies import *


bot = Bot(token, parse_mode='markdown')
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message):
    db.cursor.execute(f"SELECT name FROM users where id = {message.from_user.id}")
    if db.cursor.fetchone() is None:
        db.InsertValue(message.from_user.first_name, message.from_user.id, datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
        for row in db.cursor.execute(f"SELECT joiningDate FROM users where id={message.from_user.id}"):
            print('New user:', message.from_user.id, '|', row[0])
            await message.answer('🦉 *Вітаю* {username}\n\nДавай будемо вчитися разом!\n\n_Обирай потрібний пункт та починаймо пізнавати польську мову разом 😊_\n\n📧 Адміністратор: {admin}'.format(
                username=f'[{message.from_user.full_name}](tg://user?id={message.from_user.id})',
                admin=f'[Oleksandr](tg://user?id={admin_oleksandr})',
            ), reply_markup=menuMain,
            disable_web_page_preview=True)
    else:
        await message.answer('🦉 *Вітаю* {username}\n\nДавай будемо вчитися разом!\n\n_Обирай потрібний пункт та починаймо пізнавати польську мову разом 😊_\n\n📧 Адміністратор: {admin}'.format(
                username=f'[{message.from_user.full_name}](tg://user?id={message.from_user.id})',
                admin=f'[Oleksandr](tg://user?id={admin_oleksandr})',
            ), reply_markup=menuMain, 
            disable_web_page_preview=True)


def register_handlers_mainMenu(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
