from aiogram.dispatcher.filters.state import State, StatesGroup


class Form(StatesGroup):
    earn_btn_ans = State()
    play_btn_ans = State()
