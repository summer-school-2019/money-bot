from aiogram import Dispatcher, types

from money_bot.initialization import bot
from money_bot.utils import db_utils, markups
from money_bot.utils.states import GlobalStates
from money_bot.utils.strings import EARN_MENU_TEXT, config


async def entry_point(message: types.Message, new=False, last_message=None, user_id=None):
    if user_id is None:
        user_id = types.User.get_current().id
    user = await db_utils.get_current_user(user_id)
    if new or user.current_task_id == -1:
        task = await db_utils.get_next_task(user_id)
    else:
        task = await db_utils.get_current_task(user_id)
    if task is None:
        if last_message is None:
            await bot.send_message(message.chat.id, EARN_MENU_TEXT["no_tasks"])
        else:
            await bot.edit_message_text(EARN_MENU_TEXT["no_tasks"], message.chat.id, last_message)
        return
    if last_message is None:
        await bot.send_message(
            message.chat.id,
            EARN_MENU_TEXT["new_task"].format(task.channel_name),
            reply_markup=markups.get_earn_markup(task),
        )
    else:
        await bot.edit_message_text(
            EARN_MENU_TEXT["new_task"].format(task.channel_name),
            message.chat.id,
            last_message,
            reply_markup=markups.get_earn_markup(task),
        )


async def check_task(query: types.CallbackQuery, callback_data: dict):
    await query.answer()
    task = await db_utils.get_current_task(query.from_user.id)
    user = await db_utils.get_current_user(query.from_user.id)
    if callback_data["skip"] == "0":
        chat_member = await bot.get_chat_member(task.chat_id, user.user_id)
        if chat_member is not None and chat_member.is_chat_member():
            user.money += config.MONEY_FOR_GROUP
            user.current_task_id += 1
            await user.commit()
            await bot.edit_message_text(
                EARN_MENU_TEXT["group_check_success"],
                query.message.chat.id,
                query.message.message_id,
                reply_markup=markups.get_next_task_markup(),
            )
        else:
            await bot.edit_message_text(
                EARN_MENU_TEXT["group_check_failed"],
                query.message.chat.id,
                query.message.message_id,
                reply_markup=markups.get_next_task_markup(),
            )
    elif callback_data["skip"] == "1":
        user.current_task_id += 1
        await user.commit()
        await bot.edit_message_text(
            EARN_MENU_TEXT["task_cancelled"],
            query.message.chat.id,
            query.message.message_id,
            reply_markup=markups.get_next_task_markup(),
        )
    else:
        await entry_point(query.message, last_message=query.message.message_id, user_id=query.message.chat.id)


def register_all_handlers(dp: Dispatcher):
    dp.register_message_handler(entry_point, state=GlobalStates.earn_menu)
    dp.register_callback_query_handler(check_task, markups.earn_factory.filter(), state=GlobalStates.earn_menu)
