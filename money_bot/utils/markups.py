from aiogram import types

from money_bot.utils.strings import MAIN_MENU_BUTTONS_LABELS


def get_main_menu_markup():
    btns_text = [
        MAIN_MENU_BUTTONS_LABELS["earn"],
        MAIN_MENU_BUTTONS_LABELS["play"],
        MAIN_MENU_BUTTONS_LABELS["balance"],
        MAIN_MENU_BUTTONS_LABELS["invite"],
        MAIN_MENU_BUTTONS_LABELS["withdrawal"],
        MAIN_MENU_BUTTONS_LABELS["rules"],
    ]

    keyboard_markup = types.ReplyKeyboardMarkup(row_width=2)
    keyboard_markup.add(*[types.KeyboardButton(btn_text) for btn_text in btns_text])
    return keyboard_markup
