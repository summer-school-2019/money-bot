from aiogram.dispatcher.filters.state import State, StatesGroup


class Form(StatesGroup):
    main_menu_ans = State()
    earn_menu_ans = State()
    play_menu_ans = State()
    balance_menu_ans = State()
    invite_menu_ans = State()
    withdrawal_menu_ans = State()
    rules_menu_ans = State()
