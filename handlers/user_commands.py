from aiogram import Router, F
from aiogram.types import Message

from db.database import db

router = Router()


@router.message(F.text == "/start")
async def start_func(msg: Message):
    user_id = msg.from_user.id
    await db.add_user_if_not_exists(user_id)

    await msg.answer(
        text=f"👋 Hey, <b>{msg.from_user.full_name}</b> !",
        parse_mode="html",
    )
