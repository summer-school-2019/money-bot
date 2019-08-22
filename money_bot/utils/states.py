from aiogram.dispatcher.filters.state import State, StatesGroup


class GlobalStates(StatesGroup):
    earn_btn = State()
    play_btn = State()
    balance_btn = State()
    invite_btn = State()
    withdrawal_btn = State()
    rules_btn = State()
    add_tasks_btn = State()


class WithdrawalStates(StatesGroup):
    phone_number = State()
    money_amount = State()


class AddTasksStates(StatesGroup):
    enter_group_id = State()
    check_for_admin = State()
