from aiogram import Dispatcher, types

from money_bot.initialization import bot
from money_bot.utils import db_utils
from money_bot.utils import markups
from money_bot.utils.models import Task, User
from money_bot.utils.states import GlobalStates
from money_bot.utils.strings import EARN_MENU_TEXT, EARN_MENU_BUTTONS_LABELS


async def entry_point(message: types.Message, new=False):
    if new:
        task = await db_utils.get_next_task(message.from_user.id)
    else:
        task = await db_utils.get_current_task(message.from_user.id)
    await bot.send_message(
        message.chat.id, EARN_MENU_TEXT["new_task"].format(task.channel_name), reply_markup=markups.get_earn_markup(task)
    )


async def check_task(query: types.CallbackQuery, callback_data: dict):
    task = await db_utils.get_current_user(query.from_user.id)
    if callback_data['skip'] == '0':
        if bot.get_chat_member(Task.chat_id, User.user_id) is not None:
            User.money += 20
            await bot.send_message(query.message.chat.id,
                                   EARN_MENU_TEXT["group_check_success"],
                                   reply_markup=markups.get_earn_markup(task))
        else:
            await bot.send_message(
                query.message.chat.id, EARN_MENU_TEXT["group_check_failed"],
                reply_markup=markups.get_earn_markup(task)
            )
    else:
        pass

    await bot.send_message(query.message.chat.id, "Хочешь получить еще задание?", reply_markup=markups.get_earn_markup())


async def get_new_task(query: types.CallbackQuery):
    if query.data == "Да":
        pass
    else:
        pass


def register_all_handlers(dp: Dispatcher):
    dp.register_message_handler(entry_point, state=GlobalStates.earn_menu)
    dp.register_callback_query_handler(check_task, markups.earn_factory.filter(), state=GlobalStates.earn_menu)
    dp.register_callback_query_handler(get_new_task, markups.earn_agree_factory.filter(), state=GlobalStates.earn_menu)
