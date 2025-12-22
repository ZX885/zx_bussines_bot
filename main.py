import telebot
import sqlite3
# import requests
# import webbrowser
# from telebot import types

bot = telebot.TeleBot('')
print('Running the bot............')

name = 'None'

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('zx.sql')
    cur = conn.cursor()
    
    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегистрируем! Введите имя')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()
    
    conn = sqlite3.connect('zx.sql')
    cur = conn.cursor()
    
    cur.execute(
        f"INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (name, password)
        )
    conn.commit()
    cur.close()
    conn.close()
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован!', reply_markup=markup)
    # bot.register_next_step_handler(message, user_pass)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    conn = sqlite3.connect('zx.sql')
    cur = conn.cursor()
    
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    
    info = ''
    for el in users:
        info += f'Имя: {el[1]}, пароль: {el[2]}\n'
    cur.close()
    conn.close()
    
    bot.send_message(call.message.chat.id, info)


# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton('Перейти на сайт')
#     markup.row(btn1)
#     btn2 = types.KeyboardButton('Удалить фото')
#     btn3 = types.KeyboardButton('Изменить текст')
#     markup.row(btn2, btn3)
#     file = open('./zx.jpg', 'rb')
#     bot.send_photo(message.chat.id, file)
#     bot.send_message(message.chat.id, 'Привет 😂', reply_markup=markup)
#     bot.register_next_step_handler(message, on_click)

# ======================================================================================   
# @bot.message_handler(commands=['help'])
# def help(message):
#     mess = f"""
#     Добро пожаловать <b>{message.from_user.first_name} {message.from_user.last_name}</b>
# Полезные команды:
#     /start
#     /help
#     /site
#     /random_img       
# По всем вопросам @AKM_SHOOT
#     """
#     bot.send_message(message.chat.id, mess,parse_mode='html')
# ===============================================================================
# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://www.youtube.com/channel/UCCEDRfofQS-DBurQ_MpBTkA')
#     markup.row(btn1)
#     btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
#     btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edite')
#     markup.row(btn2, btn3)
#     bot.reply_to(message, 'Какая красивое фото', reply_markup=markup)




bot.polling(non_stop=True)
