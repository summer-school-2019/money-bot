from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from money_bot.utils import markups
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
        with state.proxy() as storage:
            storage['group_id'] = group_id
        await message.answer(ADD_TASKS_MENU_TEXT["give_me_admin"], reply_markup=markups.get_check_admin_markup())
        await AddTasksStates.check_for_admin.set()
    except TypeError:
        await message.answer(ADD_TASKS_MENU_TEXT["incorrect_group_id"])


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(entry_point, state=GlobalStates.add_tasks_btn)
    dp.register_message_handler(enter_group_id, state=AddTasksStates.enter_group_id)
