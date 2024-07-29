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

Если будут вобпросы тг на 👉 https://t.me/AKM_SHOOT

""")

@router.message(Command('help'))
async def help(message: Message):
    await message.answer('''
/start 👆 для запуска бота 
/app 📟 наши сайты
    ''')

@router.message(Command('app'))
async def app(message: Message):
    markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='web app',web_app=WebAppInfo(url='https://online-shop-rwi0.onrender.com'))],
        [KeyboardButton(text='furniture site',web_app=WebAppInfo(url='https://zarrux-company-react-frontend.onrender.com'))],
        [KeyboardButton(text='Channel',web_app=WebAppInfo(url='https://www.youtube.com'))]
        ],resize_keyboard=True)
    await message.answer('Наши сайты 📟!', reply_markup=markup)
