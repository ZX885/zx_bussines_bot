import socket
import asyncio
from aiogram import Bot, Dispatcher, types, F

from app.handlers import router


print('Running a bot...........')


async def main():
    bot = Bot('7328354559:AAHF-zxxsIGWvMW4AUNbzDDnt2Oz6O-5wK4') # Подключаемся к боту через токен
    dp = Dispatcher() # Наш обработчик, роутер, помошник
    dp.include_router(router)
    await dp.start_polling(bot) # Поллинг - наш скрипт обращается к серверу телеграм-- не пришло ли обновление


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot off')
        
        
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())

conn.close()