from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton,InlineKeyboardButton, ReplyKeyboardRemove

btnAddPhoto = InlineKeyboardButton('📸 Додати фото', callback_data='add_photo')
btnNext = InlineKeyboardButton('Відправити 😎', callback_data='next')
btnQuit = InlineKeyboardButton('Відміна 🚫', callback_data='quit')

menuMailing = InlineKeyboardMarkup(resize_keyboard=True).add(btnAddPhoto, btnNext).add(btnQuit)
menuMailing2 = InlineKeyboardMarkup(resize_keyboard=True).add(btnNext, btnQuit)
menuCancel = InlineKeyboardMarkup(resize_keyboard=True).add(btnQuit)