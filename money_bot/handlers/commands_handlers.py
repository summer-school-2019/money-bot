from aiogram import Dispatcher, types
from money_bot.utils import states
from money_bot.utils import markups


async def cmd_start(message: types.Message):
    await states.Form.main_menu_ans.set()
    keyboard_markup = markups.get_main_menu_markup()
    await message.answer("*keyboard shows up*", reply_markup=keyboard_markup)


def register_handlers(handler_dp: Dispatcher):
    handler_dp.register_message_handler(cmd_start, commands="start", state="*")
