import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from money_bot.utils.markups import get_keyboard, get_keyboard_1
from money_bot.utils.models import Task, User

logging.basicConfig(level=logging.INFO)


TOKEN = "938216489:AAHfQx8ZR5rnzLs9QJc23bZvT3BoOpZ0Vjo"
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


class states_group(StatesGroup):
    new_task_ok = State()
    new_task = State()
    main_menu = State()
    button_result = State()
    main_menu = State()


@dp.message_handler(state=states_group.new_task_ok, commands="/start")
async def menu(message: types.Message, state: FSMContext):
    get_keyboard()

    await bot.send_message(
        message.chat.id, "Подпишись на группу --имя группы-- и заработай 20 монет!", reply_markup=get_keyboard()
    )
    await states_group.new_task.set()


@dp.callback_query_handler(state=states_group.new_task)
async def second_menu(querry: types.CallbackQuery):
    if querry.data == "Получить награду":
        if bot.get_chat_member(Task.chat_id, User.user_id) is not None:
            User.money += 20
            await bot.send_message(querry.message.chat.id, "Поздравляем!", reply_markup=get_keyboard())
            await states_group.new_task.set()
        else:
            await bot.send_message(querry.message.chat.id, "Вы не подписаны на группу", reply_markup=get_keyboard())
            await states_group.new_task.set()
    if querry.data == "Пропустить задание":
        await states_group.new_task.set()
    if querry.data == "Вернуться в меню":
        await states_group.main_menu.set()
    get_keyboard_1()

    await bot.send_message(querry.message.chat.id, "Хочешь получить еще задание?", reply_markup=get_keyboard())
    await states_group.button_result.set()


@dp.callback_query_handler(state=states_group.button_result)
async def get_new_task(querry: types.CallbackQuery):
    if querry.data == "Да":
        await states_group.new_task_ok.set()
    else:
        await states_group.main_menu.set()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
