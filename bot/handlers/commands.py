from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name='commands-router')


@router.message(Command('start'))
async def start_cmd(message: Message):
    await message.answer('Сәләм! Мин ясалма акыл!\nМиңа теләсә нинди сорау бирегез һәм мин татар телендә җавап бирермен')
