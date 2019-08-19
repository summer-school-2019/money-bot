# This is a file for any states for FSM
from aiogram.dispatcher.filters.state import State, StatesGroup
class states_group(StatesGroup):
    new_task_ok = State()
    new_task = State()
    main_menu = State()
    button_result = State()