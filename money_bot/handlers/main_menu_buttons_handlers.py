from aiogram import Dispatcher, types

from money_bot.utils import states
from money_bot.utils.strings import MAIN_MENU_BUTTONS_LABELS


async def process_earn_btn(message: types.Message):
    await states.Form.earn_menu_ans.set()
    await message.answer(f'"{message.text}" clicked')


async def process_play_btn(message: types.Message):
    await states.Form.play_menu_ans.set()
    await message.answer(f'"{message.text}" clicked')


async def process_balance_btn(message: types.Message):
    await states.Form.balance_menu_ans.set()
    await message.answer(f'"{message.text}" clicked')


async def process_invite_btn(message: types.Message):
    await states.Form.invite_menu_ans.set()
    await message.answer(f'"{message.text}" clicked')


async def process_withdrawal_btn(message: types.Message):
    await states.Form.withdrawal_menu_ans.set()
    await message.answer(f'"{message.text}" clicked')


async def process_rules_btn(message: types.Message):
    await states.Form.rules_menu_ans.set()
    await message.answer(f'"{message.text}" clicked')


def register_handlers(handler_dp: Dispatcher):
    handler_dp.register_message_handler(
        process_earn_btn, text=MAIN_MENU_BUTTONS_LABELS["earn"], state=states.Form.main_menu_ans
    )
    handler_dp.register_message_handler(
        process_play_btn, text=MAIN_MENU_BUTTONS_LABELS["play"], state=states.Form.main_menu_ans
    )
    handler_dp.register_message_handler(
        process_balance_btn, text=MAIN_MENU_BUTTONS_LABELS["balance"], state=states.Form.main_menu_ans
    )
    handler_dp.register_message_handler(
        process_invite_btn, text=MAIN_MENU_BUTTONS_LABELS["invite"], state=states.Form.main_menu_ans
    )
    handler_dp.register_message_handler(
        process_withdrawal_btn, text=MAIN_MENU_BUTTONS_LABELS["withdrawal"], state=states.Form.main_menu_ans
    )
    handler_dp.register_message_handler(
        process_rules_btn, text=MAIN_MENU_BUTTONS_LABELS["rules"], state=states.Form.main_menu_ans
    )
