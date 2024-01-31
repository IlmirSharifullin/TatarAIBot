import datetime

from aiogram import Router
from aiogram.types import Message

from db.models import AIModeEnum
from gpt.__main__ import get_gpt_response
from translater.__main__ import get_translation, detect_language

import db.funcs as db

router = Router(name='messages-router')


@router.message()
async def all_messages(message: Message):
    user = await db.get_user_by_chat_id(message.from_user.id)
    mode = AIModeEnum(user.mode)

    start_time = datetime.datetime.now()

    debug_info = []
    language = detect_language(message.text)
    language_detect_time = datetime.datetime.now()
    debug_info.append(f'detect_language: {language_detect_time - start_time}\n{language}')

    if mode == AIModeEnum.TT:
        msg = await message.answer('Бер-ике секунд бирегез инде⏳')
    else:
        msg = await message.answer('Подождите пару секунд⏳')

    if language == 'tt':
        text = get_translation([message.text], 'tt', 'ru')[0]
        debug_info.append('translation:' + str(datetime.datetime.now() - start_time))
    else:
        text = message.text

    gpt_response = get_gpt_response(text=text)
    debug_info.append('gpt response:' + str(datetime.datetime.now() - start_time))

    if mode == AIModeEnum.TT:
        resp = get_translation([gpt_response], 'ru', 'tt')[0]
        debug_info.append('translation2:' + str(datetime.datetime.now() - start_time))
    elif mode == AIModeEnum.RU:
        resp = gpt_response
    else:
        return await msg.delete()

    await msg.edit_text(text=resp, parse_mode=None)
