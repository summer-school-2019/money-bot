# This is a file for any states for FSM
from aiogram.dispatcher.filters.state import State, StatesGroup


class GlobalStates(StatesGroup):
    earn_menu = State()
    play_menu = State()
    balance_menu = State()
    invite_menu = State()
    withdrawal_menu = State()
    rules_menu = State()
