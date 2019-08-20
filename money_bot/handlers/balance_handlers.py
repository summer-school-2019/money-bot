from aiogram import Dispatcher, types

from money_bot.utils import db_utils
from money_bot.utils.states import GlobalStates
from money_bot.utils.strings import BALANCE_MENU_TEXT


async def entry_point(message: types.Message):
    user = await db_utils.get_user_by_id(message.from_user.id)
    await message.answer(BALANCE_MENU_TEXT["balance_info"].format(
        user.money,
        await db_utils.get_invited_count(user.user_id)
    ))


def register_all_handlers(dp: Dispatcher):
    dp.register_message_handler(entry_point, state=GlobalStates.balance_menu)
