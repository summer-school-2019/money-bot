from aiogram import Dispatcher, types

from money_bot.utils import states
from money_bot.utils.strings import MAIN_MENU_BUTTONS_LABELS


async def process_earn_btn(message: types.Message):
    await states.Form.earn_menu_ans.set()
    await message.answer(f"")


def register_handlers(handler_dp: Dispatcher):
    handler_dp.register_message_handler(process_earn_btn, state=states.Form.main_menu_ans)
