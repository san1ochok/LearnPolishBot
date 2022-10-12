from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton,InlineKeyboardButton, ReplyKeyboardRemove

btnABC = KeyboardButton('⚡ Алфавіт')
btnBasics = KeyboardButton('🔥 База')
btnExamplesOfDialogs = KeyboardButton('💬 Діалогів')
btnInfo = KeyboardButton('🦉 Інфо')

menuMain = ReplyKeyboardMarkup(resize_keyboard=True).add(btnABC).add(btnBasics, btnExamplesOfDialogs).add(btnInfo)
