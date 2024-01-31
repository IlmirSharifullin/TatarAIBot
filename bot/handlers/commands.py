from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
import db.funcs as db
from bot.keyboards import switch_language_keyboard

router = Router(name='commands-router')


@router.message(Command('start'))
async def start_cmd(message: Message):
    user = await db.get_user_by_chat_id(message.from_user.id)
    if not user:
        await db.insert_user(message.from_user.id)

    await message.answer('''Сәлам! Мин татар һәм рус телләрендә аралаша белүче ясалма интеллект. Түбәндә мин җавап бирәчәк телне сайлагыз.

Привет! Я искусственный интеллект, который умеет общаться на татарском и русском языках. Ниже выберите язык, на котором я буду давать ответы.''',
                         reply_markup=switch_language_keyboard)
