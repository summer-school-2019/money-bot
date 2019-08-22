from aiogram import Dispatcher, types, Bot
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import ChatNotFound, ChatAdminRequired

from money_bot.utils import markups, db_utils
from money_bot.utils import models
from money_bot.utils.states import GlobalStates, AddTasksStates
from money_bot.utils.strings import ADD_TASKS_MENU_TEXT


async def entry_point(message: types.Message, last_message=None):
    """

    :param message:
    :param last_message: If last_message is None, bot create new message, so if function get last_message,
    it means that bot need to edit created message
    :return:
    """
    await message.answer(ADD_TASKS_MENU_TEXT["welcome"])
    await AddTasksStates.enter_group_id.set()


async def enter_group_id(message: types.Message, state: FSMContext):
    try:
        group_id = int(message.text)
        if await db_utils.is_task_exists(group_id):
            await message.answer(ADD_TASKS_MENU_TEXT["task_exists"])
            return
        async with state.proxy() as storage:
            storage['group_id'] = group_id
        await message.answer(ADD_TASKS_MENU_TEXT["give_me_admin"], reply_markup=markups.get_check_admin_markup())
        await AddTasksStates.check_for_admin.set()
    except ValueError:
        await message.answer(ADD_TASKS_MENU_TEXT["incorrect_group_id"])


async def check_for_admin(query: types.CallbackQuery, state: FSMContext):
    await query.answer()
    bot = Bot.get_current()
    try:
        async with state.proxy() as storage:
            await bot.get_chat_member(storage["group_id"], query.message.chat.id)
            chat = await bot.get_chat(storage["group_id"])
            task = models.Task(chat_id=storage["group_id"], channel_name=chat.title, url=await chat.get_url())
            await task.commit()
            await bot.send_message(query.message.chat.id, ADD_TASKS_MENU_TEXT["add_successful"])
    except (ChatNotFound, ChatAdminRequired):
        await bot.edit_message_text(ADD_TASKS_MENU_TEXT["admin_failed"],
                                    query.message.chat.id,
                                    query.message.message_id,
                                    reply_markup=markups.get_check_admin_markup())


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(entry_point, state=GlobalStates.add_tasks_btn)
    dp.register_message_handler(enter_group_id, state=AddTasksStates.enter_group_id)
    dp.register_callback_query_handler(check_for_admin,
                                       markups.add_tasks_factory.filter(data="0"),
                                       state=AddTasksStates.check_for_admin)
