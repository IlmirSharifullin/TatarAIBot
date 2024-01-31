from aiogram import Router, F
from aiogram.types import Message

import db.funcs as db
from db.models import AIModeEnum

router = Router(name='switch-languages-router')


@router.message(F.text == 'Татарча')
async def switch_tt(message: Message):
    try:
        user = await db.update_user_mode(message.from_user.id, AIModeEnum.TT)
    except Exception as ex:
        print(ex)
        await message.answer('Произошла ошибка, попробуйте позже')
    else:
        await message.answer('Татарча сөйләшәм')


@router.message(F.text == 'Русский')
async def switch_tt(message: Message):
    try:
        user = await db.update_user_mode(message.from_user.id, AIModeEnum.RU)
    except Exception as ex:
        print(ex)
        await message.answer('Произошла ошибка, попробуйте позже')
    else:
        await message.answer('Отвечаю на русском языке')
