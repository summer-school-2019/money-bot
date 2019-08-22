from money_bot.handlers import (
    balance_handlers,
    commands_handlers,
    earn_handlers,
    invite_handlers,
    main_menu_buttons_handlers,
    add_tasks_handlers
)


def register_all_handlers(dp):
    commands_handlers.register_handlers(dp)
    main_menu_buttons_handlers.register_handlers(dp)
    earn_handlers.register_handlers(dp)
    invite_handlers.register_handlers(dp)
    balance_handlers.register_handlers(dp)
    add_tasks_handlers.register_handlers(dp)
