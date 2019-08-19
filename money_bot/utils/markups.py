# This is the bot for any markups
from aiogram import types

from money_bot.utils.models import Task


def get_keyboard():
    return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton("Подписаться", url=Task.url),
        types.InlineKeyboardButton("Забрать награду", callback_data="Забрать награду"),
        types.InlineKeyboardButton("Пропустить задание", callback_data="Пропустить задание"),
        types.InlineKeyboardButton("Вернуться в меню", callback_data="Вернуться в меню"),
    )


def get_keyboard_1():
    return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton("Да", callback_data="Да"), types.InlineKeyboardButton("Нет", callback_data="Нет")
    )
