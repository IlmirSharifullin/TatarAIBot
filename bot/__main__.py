import asyncio

from aiogram import Bot, Dispatcher
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from bot.config import BOT_TOKEN, DB_URL
from bot.handlers import callbacks, commands, messages
from bot.middlewares.db import DbSessionMiddleware


async def main():
    engine = create_async_engine(url=DB_URL, echo=True)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)

    bot = Bot(BOT_TOKEN, parse_mode='markdown')
    dp = Dispatcher()
    dp.update.middleware(DbSessionMiddleware(session_pool=sessionmaker))

    dp.callback_query.middleware(CallbackAnswerMiddleware())

    dp.include_routers(callbacks.router, commands.router, messages.router)

    await dp.start_polling(bot, allowed_updates=True)


if __name__ == '__main__':
    asyncio.run(main())
