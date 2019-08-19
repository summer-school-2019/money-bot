import re

from aiogram import Dispatcher, types

from money_bot.utils import markups, states
from money_bot.utils.models import User


async def cmd_start_referral(message: types.Message, regexp_command):
    await states.Form.main_menu_ans.set()
    current_user = await User.find_one({"user_id": message.from_user.id})
    try:
        if not current_user.referrer_id:
            referrer_user = await User.find_one({"user_id": int(regexp_command.group(1))})
            current_user.referrer_id = referrer_user.user_id
            await current_user.commit()
    # OverflowError, ValueError, AttributeError
    except:
        pass
    keyboard_markup = markups.get_main_menu_markup()
    await message.answer(
        f"Привет, {message.from_user.id} - {message.from_user.first_name} {message.from_user.last_name}!",
        reply_markup=keyboard_markup
    )


async def cmd_start(message: types.Message):
    await states.Form.main_menu_ans.set()
    keyboard_markup = markups.get_main_menu_markup()
    await message.answer(
        f"Привет, {message.from_user.id} - {message.from_user.first_name} {message.from_user.last_name}!",
        reply_markup=keyboard_markup
    )


# async def cmd_start(message: types.Message):
#     await states.Form.main_menu_ans.set()
#     if re.match(r"/start referrer_id_([0-9]*)", message.text):
#         current_user = await User.find_one({"user_id": message.from_user.id})
#         print(re.search(r"([0-9]*)", message.text).group(0) + "----------------------------------------------------")
#         try:
#             if not current_user.referrer_id:
#                 referrer_user = await User.find_one({
#                     "user_id": int(re.search(r"([0-9]*)", message.text).group(0))
#                 })
#                 current_user.referrer_id = referrer_user.user_id
#                 await current_user.commit()
#         except:
#             pass
#     keyboard_markup = markups.get_main_menu_markup()
#     await message.answer(
#         f"Привет, {message.from_user.id} - {message.from_user.first_name} {message.from_user.last_name}!",
#         reply_markup=keyboard_markup
#     )


def register_handlers(handler_dp: Dispatcher):
    handler_dp.register_message_handler(
        cmd_start_referral, commands="start", regexp_commands=["referrer_id_([0-9]*)"], state="*"
    )
    handler_dp.register_message_handler(cmd_start, commands="start", state="*")
