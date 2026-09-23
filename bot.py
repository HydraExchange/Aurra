import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from database import init_db
from handlers.start import router as start_router


async def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN не найден в .env")

    # Создаём таблицы SQLite
    init_db()

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Подключаем обработчики
    dp.include_router(start_router)

    print("AURORA EXCHANGE запущен.")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())