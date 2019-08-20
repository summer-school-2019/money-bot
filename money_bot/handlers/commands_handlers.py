import re

from aiogram import Dispatcher, types

from money_bot.utils import markups, states
from money_bot.utils.models import User


def get_referrer_id_from_message_text(message_text):
    command_args = message_text.split()[1::] if "/start" in message_text.split() else None
    if command_args:
        referrer_id = list(filter(lambda x: re.search(r"referrer_id_(\d+)", message_text), command_args))[0][12::]
        if referrer_id:
            return int(referrer_id)
        return None


async def set_referrer_id_to_db(current_user_id, referrer_id):
    current_user = await User.find_one({"user_id": current_user_id})
    try:
        if not current_user.referrer_id:
            referrer_user = await User.find_one({"user_id": referrer_id})
            current_user.referrer_id = referrer_user.user_id
            await current_user.commit()
    except (OverflowError, ValueError, AttributeError):
        pass


async def cmd_start(message: types.Message):
    referrer_id = get_referrer_id_from_message_text(message.text)
    if referrer_id:
        await set_referrer_id_to_db(message.from_user.id, referrer_id)

    keyboard_markup = markups.get_main_menu_markup()
    await message.answer(
        f"Привет, {message.from_user.id} - {message.from_user.first_name} {message.from_user.last_name}!",
        reply_markup=keyboard_markup
    )


def register_handlers(handler_dp: Dispatcher):
    handler_dp.register_message_handler(cmd_start, commands="start", state="*")
