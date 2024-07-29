from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(type=str, text='Admin')],
                                    #  [KeyboardButton(text='Help')],
                                    #  [KeyboardButton(text='Contacts')],
                                    #  KeyboardButton(text='About us')
                                     ],
                           resize_keyboard=True,
                           input_field_placeholder="Выберите опцию...")
