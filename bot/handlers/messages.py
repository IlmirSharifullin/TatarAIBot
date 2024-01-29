import datetime

from aiogram import Router
from aiogram.types import Message

from gpt.__main__ import get_gpt_response
from translater.__main__ import get_translation, detect_language

router = Router(name='messages-router')


@router.message()
async def all_messages(message: Message):

    start_time = datetime.datetime.now()

    debug_info = []
    language = detect_language(message.text)
    language_detect_time = datetime.datetime.now()
    debug_info.append(f'detect_language: {language_detect_time - start_time}\n{language}')

    if language == 'tt':
        msg = await message.answer('Бер-ике секунд бирегез инде⏳')

        text = get_translation([message.text], 'tt', 'ru')[0]
        debug_info.append('translation:' + str(datetime.datetime.now() - start_time))
    else:
        msg = await message.answer('Подождите пару секунд⏳')

        text = message.text

    gpt_response = get_gpt_response(text=text)
    debug_info.append('gpt response:' + str(datetime.datetime.now() - start_time))

    if language == 'tt':
        resp = get_translation([gpt_response], 'ru', 'tt')[0]
        debug_info.append('translation2:' + str(datetime.datetime.now() - start_time))
    else:
        resp = gpt_response

    debug_info_str = '\n'.join(debug_info)
    ans = (f'{resp}'
           f'{debug_info_str}')
    print(ans)
    await msg.edit_text(text=ans, parse_mode=None)
