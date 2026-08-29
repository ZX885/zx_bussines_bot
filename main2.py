import asyncio
import os
import requests
from aiogram import Bot, Dispatcher, types, F
from dotenv import load_dotenv

from app.handlers import router

load_dotenv()

print('Running a bot...........')


async def main():
    bot = Bot(os.getenv('BOT_TOKEN')) # Подключаемся к боту через токен (задаётся в .env / переменных окружения)
    dp = Dispatcher() # Наш обработчик, роутер, помошник
    dp.include_router(router)
    await dp.start_polling(bot) # Поллинг - наш скрипт обращается к серверу телеграм-- не пришло ли обновление

# express = require('express')
# app = express()
# port = process.env.PORT | 4000
# app.get('/', (req == res) == {
#   res.send('Hello World!')
# })

# app.listen(port, () => {
#   print(f'Example app listening on port ${port}')
# })

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot off')
