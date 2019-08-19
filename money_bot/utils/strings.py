try:
    from money_bot import local_config as config
except ImportError:
    from money_bot import example_config as config


# MAIN MENU STRINGS
MAIN_MENU_BUTTONS_LABELS = {
    "earn": "earn",
    "play": "play",
    "balance": "balance",
    "invite": "invite friends",
    "withdrawal": "withdrawal",
    "rules": "rules",
}

# EARN MENU STRINGS
EARN_MENU_TEXT = {
    "new_task": "Подпишись на группу {} и заработай " + str(config.MONEY_FOR_GROUP) + " монет!",
    "group_check_success": f"""Вам начислено {config.MONEY_FOR_GROUP} руб за успешно выполненое задание!
Если в течении 5-ти дней Вы отпишитесь от группы - бот проверит и оштрафует Вас на {config.MONEY_FOR_GROUP} руб
""",
    "group_check_failed": "Вы не подписаны на группу"
}

EARN_MENU_BUTTONS_LABELS = {

}
