import traceback
from functools import wraps
from typing import Callable

from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from config import async_session_maker
from db.models import User, AIModeEnum


def with_session(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            async with async_session_maker() as session:
                result = await func(*args, session, **kwargs)
                await session.commit()
            return result
        except Exception as ex:
            print(traceback.format_exc())

    return wrapper


@with_session
async def get_user_by_id(id: int, session: AsyncSession):
    query = await session.execute(select(User).filter_by(id=id))
    user = query.scalar()
    return user


@with_session
async def get_user_by_chat_id(chat_id: int, session: AsyncSession):
    query = await session.execute(select(User).filter_by(chat_id=chat_id))
    user = query.scalar()
    return user


@with_session
async def insert_user(chat_id: int, session: AsyncSession):
    user = await session.execute(insert(User).values(chat_id=chat_id).returning(User))
    return user.scalar()


@with_session
async def update_user_mode(chat_id: int, mode: AIModeEnum, session: AsyncSession):
    user = await session.execute(update(User).filter_by(chat_id=chat_id).values(mode=mode.value).returning(User))
    return user.scalar()