from enum import Enum

from sqlalchemy import Column, Integer
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class UserStatusEnum(Enum):
    BANNED = 0
    OK = 1
    ADMIN = 555
    MAIN_ADMIN = 777


class AIModeEnum(Enum):
    TT = 0
    RU = 1


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False, default=UserStatusEnum.OK.value)
    mode = Column(Integer, nullable=False, default=AIModeEnum.TT.value)

