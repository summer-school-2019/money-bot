from aiogram import Dispatcher, types

from money_bot.utils import db_utils
from money_bot.utils.states import GlobalStates
from money_bot.utils.strings import BALANCE_MENU_TEXT


async def entry_point(message: types.Message):
    await message.answer(
        BALANCE_MENU_TEXT["balance_info"].format(
            money=await db_utils.get_user_money_amount(message.from_user.id),
            invited_count=await db_utils.get_user_referees_amount(message.from_user.id),
        )
    )


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(entry_point, state=GlobalStates.balance_btn)
