from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import START_TEXT, START_TITLE, START_IMAGE
from database import save_user


router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    user = message.from_user

    # Сохраняем пользователя в SQLite
    save_user(
        telegram_id=user.id,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
    )

    text = f"{START_TITLE}\n\n{START_TEXT}"

    await message.answer(text)