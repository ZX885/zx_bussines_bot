from aiogram import  F, Router, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from aiogram.filters import CommandStart, Command

import app.keyboards as kb

router = Router()


@router.message(CommandStart()) # должен ловить сообщение 
async def start(message: Message):
    # await message.answer('Hello', reply_markup=kb.main)
    await message.reply("How are you!")

@router.message(Command('help'))
async def help(message: Message):
    await message.answer('please wait......')

@router.message(Command('app'))
async def app(message: Message):
    markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='web app',web_app=WebAppInfo(url='https://zarrux-company-react-frontend.onrender.com'))],
        [KeyboardButton(text='web app',web_app=WebAppInfo(url='https://itproger.com/telegram.html'))],
        [KeyboardButton(text='Channel',web_app=WebAppInfo(url='https://www.youtube.com/channel/UCCEDRfofQS-DBurQ_MpBTkA'))]
        ],resize_keyboard=True)
    await message.answer('Hello!', reply_markup=markup)
