from aiogram import Router
from aiogram.types import Message

from gpt.__main__ import get_gpt_response
from translater.__main__ import get_translation

router = Router(name='messages-router')


@router.message()
async def all_messages(message: Message):
    msg = await message.answer('Бер-ике секунд бирегез инде⏳')

    text_ru = get_translation([message.text], 'tt', 'ru')[0]

    gpt_response = get_gpt_response(text=text_ru)

    resp_tt = get_translation([gpt_response], 'ru', 'tt')[0]

    await msg.edit_text(resp_tt)