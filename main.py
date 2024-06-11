import telebot
import requests
import webbrowser
from telebot import types

bot = telebot.TeleBot('7328354559:AAHF-zxxsIGWvMW4AUNbzDDnt2Oz6O-5wK4')
print('Running the bot............')
RANDOM_IMAGE = "/random_img"
RANDOM_IMG_URL = "https://picsum.photos/1200"
global IMAGE_COUNTER
IMAGE_COUNTER = 0

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    # bot.send_photo(message.chat.id,photo='zx.jpg')
    bot.send_message(message.chat.id,mess, parse_mode='html')
@bot.message_handler(commands=['help'])
def help(message):
    mess = f"""
    Добро пожаловать <b>{message.from_user.first_name} {message.from_user.last_name}</b>
Полезные команды:
    /start
    /help
    /site
    /random_img
        
По всем вопросам @AKM_SHOOT
    """
    bot.send_message(message.chat.id, mess,parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://www.youtube.com/channel/UCCEDRfofQS-DBurQ_MpBTkA'))
    markup.add(types.InlineKeyboardButton('Удалить фото', callback_data='delete'))
    markup.add(types.InlineKeyboardButton('Изменить текст', callback_data='edite'))
    bot.reply_to(message, 'Какая красивое фото', reply_markup=markup)
    
@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://www.youtube.com/channel/UCCEDRfofQS-DBurQ_MpBTkA')
@bot.message_handler(commands=['random_img'])
def random_img(message):
    if message.text == RANDOM_IMAGE:
        image = get(RANDOM_IMG_URL).content
        context.bot.sendMediaGroup(
            chat_id=message.effective_chat.id,
            media=[InputMediaPhoto(image, caption=f"Random {IMAGE_COUNTER}")]
        )

bot.polling(non_stop=True)