# This is the bot for any markups
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


def earn_keyboard(task):
    return types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton("Подписаться", url=task.url),
        types.InlineKeyboardButton("Забрать награду", callback_data="Забрать награду"),
        types.InlineKeyboardButton("Пропустить задание", callback_data="Пропустить задание"),
    )

def agree_new_task_keyboard():
    return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton("Да", callback_data="Да"), types.InlineKeyboardButton("Нет", callback_data="Нет")
    )
