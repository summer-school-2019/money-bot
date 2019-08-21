from aiogram.dispatcher.filters.state import State, StatesGroup


class GlobalStates(StatesGroup):
    earn_btn = State()
    play_btn = State()
    balance_btn = State()
    invite_btn = State()
    withdrawal_btn = State()
    rules_btn = State()
