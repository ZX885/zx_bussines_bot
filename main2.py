import asyncio
from aiogram import Bot, Dispatcher, types, F

from app.handlers import router


print('Running a bot...........')


async def main():
    bot = Bot('7328354559:AAHAxbG9MyD00Nx0ba7vf3crw6OT3_FsEUg') # Подключаемся к боту через токен
    dp = Dispatcher() # Наш обработчик, роутер, помошник
    dp.include_router(router)
    await dp.start_polling(bot) # Поллинг - наш скрипт обращается к серверу телеграм-- не пришло ли обновление


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot off')
