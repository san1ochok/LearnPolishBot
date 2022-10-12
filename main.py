import config.db as db
from aiogram import Bot, Dispatcher, executor
from datetime import datetime
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config.config import token

from config.db import CreateDB

from keyboards.replies import *
from handlers.client.mainMenu import *
from handlers.admin.mailing import *


storage = MemoryStorage()
bot = Bot(token, parse_mode='markdown')
dp = Dispatcher(bot, storage=storage)


register_handlers_mainMenu(dp)
register_handlers_mailing(dp)


@dp.message_handler()
async def any_msg(message):
    await message.answer('Упс...🦉 Схоже, що такої команди не існує')

if __name__ == '__main__':
    CreateDB()
    executor.start_polling(dp, skip_updates=True)
