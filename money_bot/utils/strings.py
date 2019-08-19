try:
    from money_bot import local_config as config
except ImportError:
    from money_bot import example_config as config


MAIN_MENU_BUTTONS_LABELS = {
    "earn": "earn",
    "play": "play",
    "balance": "balance",
    "invite": "invite friends",
    "withdrawal": "withdrawal",
    "rules": "rules",
}
EARN_MENU_TEXT = {
    "new_task": "Подпишись на группу {} и заработай " + str(config.MONEY_FOR_GROUP) + " монет!"
}
