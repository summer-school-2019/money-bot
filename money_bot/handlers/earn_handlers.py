from money_bot.initialization import bot
from money_bot.utils import markups
from money_bot.utils.models import Task, User
from money_bot.utils.states import EarnStates
from aiogram import Dispatcher, types


async def entry_point(message: types.Message):

    task = await Task.find_one()
    await bot.send_message(
        message.chat.id,
        f"Подпишись на группу {task.channel_name} и заработай 20 монет!", reply_markup=markups.earn_keyboard(task))
    await EarnStates.making_a_decision.set()


async def second_menu(query: types.CallbackQuery):
    if query.data == "Получить награду":
        if bot.get_chat_member(Task.chat_id, User.user_id) is not None:
            User.money += 20
            await bot.send_message(query.message.chat.id, "Поздравляем!", reply_markup=markups.earn_keyboard())
            await EarnStates.giving_a_task.set()
        else:
            await bot.send_message(query.message.chat.id, "Вы не подписаны на группу", reply_markup=markups.earn_keyboard())
            await EarnStates.giving_a_task.set()
    if query.data == "Пропустить задание":
        await EarnStates.giving_a_task.set()
    if query.data == "Вернуться в меню":
        await EarnStates.main_menu.set()

    await bot.send_message(query.message.chat.id, "Хочешь получить еще задание?", reply_markup=markups.earn_keyboard())
    await EarnStates.button_result.set()


async def get_new_task(query: types.CallbackQuery):
    if query.data == "Да":
        await EarnStates.making_a_decision.set()
    else:
        await EarnStates.main_menu.set()


def register_all_handlers(dp: Dispatcher):
    dp.register_message_handler(entry_point, state=EarnStates.giving_a_task)
    dp.register_callback_query_handler(second_menu, state=EarnStates.making_a_decision)
    dp.register_callback_query_handler(get_new_task, state=EarnStates.button_result)