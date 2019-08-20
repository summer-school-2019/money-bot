# This is the bot for any markups
from aiogram import types
from aiogram.utils.callback_data import CallbackData

from money_bot.utils.strings import MAIN_MENU_BUTTONS_LABELS

earn_factory = CallbackData("earn", "skip")


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
