# This is a file for any states for FSM
from aiogram.dispatcher.filters.state import State, StatesGroup


class GlobalStates(StatesGroup):
    main_menu_ans = State()
    earn_menu = State()
    play_menu_ans = State()
    balance_menu_ans = State()
    invite_menu_ans = State()
    withdrawal_menu_ans = State()
    rules_menu_ans = State()
