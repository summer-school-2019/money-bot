from aiogram import Bot, Dispatcher, types
from aiogram.utils.exceptions import ChatAdminRequired, ChatNotFound

from money_bot.utils import db_utils, markups
from money_bot.utils.states import GlobalStates
from money_bot.utils.strings import EARN_MENU_TEXT, config


async def entry_point(message: types.Message, new=False, last_message=None, user_id=None):
    """
    :param message:
    :param new: if it's true, bot will give out new task
    :param last_message: If last_message is None, bot create new message, so if function get last_message, 
    it means that bot need to edit created message
    :param user_id:
    :return:
    """
    bot = Bot.get_current()
    if user_id is None:
        user_id = types.User.get_current().id
    user = await db_utils.get_user_by_id(user_id)
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
            EARN_MENU_TEXT["new_task"].format(channel_name=task.channel_name),
            reply_markup=markups.get_earn_markup(task),
        )
    else:
        await bot.edit_message_text(
            EARN_MENU_TEXT["new_task"].format(channel_name=task.channel_name),
            message.chat.id,
            last_message,
            reply_markup=markups.get_earn_markup(task),
        )


async def check_task(query: types.CallbackQuery, callback_data: dict):
    await query.answer()
    bot = Bot.get_current()
    task = await db_utils.get_current_task(query.from_user.id)
    user = await db_utils.get_user_by_id(query.from_user.id)
    if callback_data["skip"] == "0":
        try:
            chat_member = await bot.get_chat_member(task.chat_id, user.user_id)
            if chat_member is not None and chat_member.is_chat_member():
                await db_utils.increase_money_amount(user.user_id, config.MONEY_FOR_GROUP)
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
        except (ChatNotFound, ChatAdminRequired):
            user.current_task_id += 1
            await user.commit()
            await bot.edit_message_text(
                EARN_MENU_TEXT["bad_group"],
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
    dp.register_message_handler(entry_point, state=GlobalStates.earn_btn)
    dp.register_callback_query_handler(check_task, markups.earn_factory.filter(), state=GlobalStates.earn_btn)
