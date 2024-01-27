import asyncio
import logging
import traceback

import requests
from aiogram import Bot, Dispatcher
from aiogram.types import ErrorEvent
from aiogram.utils.callback_answer import CallbackAnswerMiddleware

from bot.config import BOT_TOKEN
from bot.handlers import callbacks, commands, messages
from config import LOGS_CHANNEL_ID


def log_to_channel(msg, type='info'):
    res = requests.post('https://api.telegram.org/bot6621958158:AAFIALtB_WkdK1YbXZ_dBfkLxzVR6xAjPK0/sendMessage',
                        params={'text': ('ERROR:\n' if type == 'error' else 'INFO:\n') + str(msg),
                                'chat_id': LOGS_CHANNEL_ID})
    return res.content

async def main():
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s  ',
        datefmt='%d-%b-%y %H:%M:%S',
        level=logging.INFO
    )

    bot = Bot(BOT_TOKEN, parse_mode='markdown')
    dp = Dispatcher()

    dp.callback_query.middleware(CallbackAnswerMiddleware())

    dp.include_routers(callbacks.router, commands.router, messages.router)

    @dp.error()
    async def error_handler(event: ErrorEvent):
        logging.error(traceback.format_exc())

        print(traceback.format_exc())

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
