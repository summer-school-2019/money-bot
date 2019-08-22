from aiogram import Dispatcher, types

from money_bot.handlers import (
    add_tasks_handlers,
    balance_handlers,
    earn_handlers,
    game_handlers,
    invite_handlers,
    rules_handlers,
)
from money_bot.utils import states
from money_bot.utils.strings import MAIN_MENU_BUTTONS_LABELS


async def process_earn_btn(message: types.Message):
    await states.GlobalStates.earn_btn.set()
    await earn_handlers.entry_point(message)


async def process_play_btn(message: types.Message):
    await states.GlobalStates.play_btn.set()
    await game_handlers.entry_point(message)


async def process_balance_btn(message: types.Message):
    await states.GlobalStates.balance_btn.set()
    await balance_handlers.entry_point(message)


async def process_invite_btn(message: types.Message):
    await states.GlobalStates.invite_btn.set()
    await invite_handlers.entry_point(message)


async def process_withdrawal_btn(message: types.Message):
    await states.GlobalStates.withdrawal_btn.set()
    await withdrawal_handlers.entry_point(message)


async def process_rules_btn(message: types.Message):
    await states.GlobalStates.rules_btn.set()
    await rules_handlers.entry_point(message)


async def proccess_add_tasks_btn(message: types.Message):
    await states.GlobalStates.add_tasks_btn.set()
    await add_tasks_handlers.entry_point(message)


def register_handlers(handler_dp: Dispatcher):
    handler_dp.register_message_handler(process_earn_btn, text=MAIN_MENU_BUTTONS_LABELS["earn"], state="*")
    handler_dp.register_message_handler(process_play_btn, text=MAIN_MENU_BUTTONS_LABELS["play"], state="*")
    handler_dp.register_message_handler(process_balance_btn, text=MAIN_MENU_BUTTONS_LABELS["balance"], state="*")
    handler_dp.register_message_handler(process_invite_btn, text=MAIN_MENU_BUTTONS_LABELS["invite"], state="*")
    handler_dp.register_message_handler(process_withdrawal_btn, text=MAIN_MENU_BUTTONS_LABELS["withdrawal"], state="*")
    handler_dp.register_message_handler(process_rules_btn, text=MAIN_MENU_BUTTONS_LABELS["rules"], state="*")
    handler_dp.register_message_handler(proccess_add_tasks_btn, text=MAIN_MENU_BUTTONS_LABELS["add_tasks"], state="*")
