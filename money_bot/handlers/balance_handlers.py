from aiogram import Dispatcher, types

from money_bot.utils import db_utils
from money_bot.utils.states import GlobalStates
from money_bot.utils.strings import BALANCE_MENU_TEXT


async def entry_point(message: types.Message):
    user = await db_utils.get_user_by_id(message.from_user.id)
    await message.answer(
        BALANCE_MENU_TEXT["balance_info"].format(
            money=user.money, invited_count=await db_utils.get_user_referees_amount(user.user_id)
        )
    )


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(entry_point, state=GlobalStates.balance_btn)
