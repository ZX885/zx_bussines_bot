from aiogram import  F, Router, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from aiogram.filters import CommandStart, Command

import app.keyboards as kb

router = Router()


@router.message(CommandStart()) # должен ловить сообщение 
async def start(message: Message):
    # await message.answer('Hello', reply_markup=kb.main)
    await message.reply("""
 Добро пожаловать в ZX Bussines bot
Бот создан для личных целей и учебы.🔍

/help 💁 для помощи
/app 📟 наши сайты
/tracker 💪 трекер тренировок

Если будут вобпросы тг на 👉 https://t.me/AKM_SHOOT

""")

@router.message(Command('help'))
async def help(message: Message):
    await message.answer('''
/start 👆 для запуска бота
/app 📟 наши сайты
/tracker 💪 трекер тренировок
    ''')

@router.message(Command('app'))
async def app(message: Message):
    markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='ZX Portfolio',web_app=WebAppInfo(url='https://zx885portfolio.netlify.app/'))],
        [KeyboardButton(text='ZX Marketplace',web_app=WebAppInfo(url='https://thunderous-biscuit-249b2e.netlify.app'))],
        [KeyboardButton(text='Channel',web_app=WebAppInfo(url='https://t.me/super_car_o_0'))],
        [KeyboardButton(text='Трекер тренировок',web_app=WebAppInfo(url='https://web-seven-sandy-84.vercel.app'))]
        ],resize_keyboard=True)
    await message.answer('Наши сайты 📟!', reply_markup=markup)

@router.message(Command('tracker'))
async def tracker(message: Message):
    markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Открыть трекер',web_app=WebAppInfo(url='https://web-seven-sandy-84.vercel.app'))]
        ],resize_keyboard=True)
    await message.answer('Трекер тренировок 💪 — ставь цели и качай персонажа на 100 дней!', reply_markup=markup)
