from aiogram import Dispatcher, types

from money_bot import initialization as init
from money_bot.utils import states
from money_bot.utils.models import User
from money_bot.utils.strings import MAIN_MENU_BUTTONS_LABELS


async def process_earn_btn(message: types.Message):
    await states.Form.earn_btn_ans.set()
    await message.answer(f'"{message.text}" clicked')


async def process_play_btn(message: types.Message):
    await states.Form.play_btn_ans.set()
    await message.answer(f'"{message.text}" clicked')


async def process_balance_btn(message: types.Message):
    await message.answer(f'"{message.text}" clicked')


async def process_invite_btn(message: types.Message):
    bot = await init.bot.me
    current_user = await User.find_one({"user_id": message.from_user.id})
    referral_link = f"https://t.me/{bot.username}?start=referrer_id_{current_user.user_id}"
    await message.answer(referral_link)


async def process_withdrawal_btn(message: types.Message):
    await message.answer(f'"{message.text}" clicked')


async def process_rules_btn(message: types.Message):
    await message.answer(f'"{message.text}" clicked')


def register_handlers(handler_dp: Dispatcher):
    handler_dp.register_message_handler(process_earn_btn, text=MAIN_MENU_BUTTONS_LABELS["earn"], state="*")
    handler_dp.register_message_handler(process_play_btn, text=MAIN_MENU_BUTTONS_LABELS["play"], state="*")
    handler_dp.register_message_handler(process_balance_btn, text=MAIN_MENU_BUTTONS_LABELS["balance"], state="*")
    handler_dp.register_message_handler(process_invite_btn, text=MAIN_MENU_BUTTONS_LABELS["invite"], state="*")
    handler_dp.register_message_handler(process_withdrawal_btn, text=MAIN_MENU_BUTTONS_LABELS["withdrawal"], state="*")
    handler_dp.register_message_handler(process_rules_btn, text=MAIN_MENU_BUTTONS_LABELS["rules"], state="*")
