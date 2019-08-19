from money_bot.handlers import commands_handlers, main_menu_buttons_handlers


def register_all_handlers(dp):
    commands_handlers.register_handlers(dp)
    main_menu_buttons_handlers.register_handlers(dp)
