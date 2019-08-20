import re

from aiogram import Dispatcher, types

from money_bot.example_config import INVITE_REWARD_MONEY_AMOUNT
from money_bot.utils import db_utils, markups


def get_referrer_id(message_text: str):
    referrer_id_arg = re.search(r"referrer_id_(\d+)", message_text)
    return int(re.search(r"(\d+)", referrer_id_arg.group(0)).group(0)) if referrer_id_arg else None


async def process_setting_referrer_id(user_id: int, referrer_id: int):
    if user_id != referrer_id:
        current_user = await db_utils.get_user_by_id(user_id)
        if await db_utils.is_user_in_db(referrer_id):
            if not current_user.referrer_id:
                await db_utils.increase_money_amount(referrer_id, INVITE_REWARD_MONEY_AMOUNT)
                await db_utils.set_referrer_id(user_id, referrer_id)
                return
    await db_utils.set_referrer_id(user_id, -1)


async def cmd_start(message: types.Message):
    referrer_id = get_referrer_id(message.text)
    if referrer_id:
        await process_setting_referrer_id(message.from_user.id, referrer_id)
    else:
        await db_utils.set_referrer_id(message.from_user.id, -1)
    keyboard_markup = markups.get_main_menu_markup()
    await message.answer(
        f"Привет, {message.from_user.id} - {message.from_user.first_name} {message.from_user.last_name}!",
        reply_markup=keyboard_markup,
    )


def register_handlers(handler_dp: Dispatcher):
    handler_dp.register_message_handler(cmd_start, commands="start", state="*")
