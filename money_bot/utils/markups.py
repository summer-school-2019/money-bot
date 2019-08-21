from aiogram import types
from aiogram.utils.callback_data import CallbackData

from money_bot.utils.strings import MAIN_MENU_BUTTONS_LABELS

earn_factory = CallbackData("earn", "skip")
game_factory = CallbackData("game", "action", "value")
game_bitcoin_factory = CallbackData("game_bitcoin", "up")


def get_main_menu_markup():
    btns_text = [
        MAIN_MENU_BUTTONS_LABELS["earn"],
        MAIN_MENU_BUTTONS_LABELS["play"],
        MAIN_MENU_BUTTONS_LABELS["balance"],
        MAIN_MENU_BUTTONS_LABELS["invite"],
        MAIN_MENU_BUTTONS_LABELS["withdrawal"],
        MAIN_MENU_BUTTONS_LABELS["rules"],
    ]

    keyboard_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard_markup.add(*[types.KeyboardButton(btn_text) for btn_text in btns_text])
    return keyboard_markup


def get_earn_markup(task):
    return types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton("Подписаться", url=task.url),
        types.InlineKeyboardButton("Забрать награду", callback_data=earn_factory.new(skip=0)),
        types.InlineKeyboardButton("Пропустить задание", callback_data=earn_factory.new(skip=1)),
    )


def get_next_task_markup():
    return types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton("Еще задания", callback_data=earn_factory.new(skip=2))
    )


def get_game_main_markup():
    return types.InlineKeyboardMarkup(row_width=4).add(
        types.InlineKeyboardButton(
            "1", callback_data=game_factory.new(action="make", value="1")
        ),
        types.InlineKeyboardButton(
            "10", callback_data=game_factory.new(action="make", value="10")
        ),
        types.InlineKeyboardButton(
            "50", callback_data=game_factory.new(action="make", value="50")
        ),
        types.InlineKeyboardButton(
            "100", callback_data=game_factory.new(action="make", value="100")
        ),
        types.InlineKeyboardButton(
            "1000", callback_data=game_factory.new(action="make", value="1000")
        ),
        types.InlineKeyboardButton(
            "+ 1", callback_data=game_factory.new(action="change", value="1")
        ),
        types.InlineKeyboardButton(
            "+ 5", callback_data=game_factory.new(action="change", value="5")
        ),
        types.InlineKeyboardButton(
            "- 1", callback_data=game_factory.new(action="change", value="-1")
        ),
        types.InlineKeyboardButton(
            "- 5", callback_data=game_factory.new(action="change", value="-5")
        ),
        types.InlineKeyboardButton(
            "\U0001F3B2 play \U0001F3B2",
            callback_data=game_factory.new(action="play", value="-"),
        ),
        types.InlineKeyboardButton(
            "\U0001F4DC rules \U0001F4DC",
            callback_data=game_factory.new(action="show_rules", value="-"),
        ),
    )


def get_menu_button_markup():
    return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton(
            "\U0001F519 menu \U0001F519",
            callback_data=game_factory.new(action="menu", value="-"),
        )
    )


def get_bitcoin_markup():
    return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton(
            "\U00002B06 grow \U00002B06",
            callback_data=game_bitcoin_factory.new(up=1),
        ),
        types.InlineKeyboardButton(
            "\U00002B07 fall \U00002B07",
            callback_data=game_bitcoin_factory.new(up=0),
        ),
    )


def get_play_again_markup():
    return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton(
            "\U0001F3B0 play again! \U0001F3B0",
            callback_data=game_factory.new(action="play_again", value="-"),
        )
    )
