import random

from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher import FSMContext

from money_bot.utils import markups
from money_bot.utils.strings import GAME_MENU_TEXT
from money_bot.utils import db_utils

b = 0
a = 70


async def entry_point(message: types.Message, state: FSMContext):
    async with state.proxy() as storage:
        storage["bet"] = 10
    await message.answer(
        f"\U0001F4B8 You have {a} money now! \U0001F4B8",
        reply_markup=markups.get_game_main_markup(),
    )  # TODO callback handler for up and down


async def callback_results(query: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await query.answer()
    bot = Bot.get_current()
    user = await db_utils.get_user_by_id(query.message.chat.id)

    async with state.proxy() as storage:

        if callback_data["action"] == "make":
            storage["bet"] = int(callback_data["value"])

        if callback_data["action"] == "change":
            delta = int(callback_data["value"])
            if storage["bet"] + delta >= 0:
                storage["bet"] += delta
            else:
                storage["bet"] = 0
        await bot.edit_message_text(
            GAME_MENU_TEXT["show_bet"].format(money=user.money, bet=storage["bet"]),
            query.message.chat.id,
            query.message.message_id,
            reply_markup=markups.get_game_main_markup(),
        )








    if callback_data["action"] == "show_rules":
        await bot.send_message(
            query.message.chat.id,
            GAME_MENU_TEXT["rules"],
            reply_markup=markups.get_menu_button_markup(),
        )

    if callback_data["action"] == "menu":
        await bot.send_message(
            query.message.chat.id,
            GAME_MENU_TEXT["show_money"].format(money=user.money),
            reply_markup=markups.get_game_main_markup(),
        )

    if callback_data["action"] in ["play", "up", "down", "play_again"]:
        if a >= b:
            number = random.randint(0, 20)
            if callback_data["action"] not in ["up", "down", "play_again"]:
                await bot.edit_message_text(
                    "Bitcoin will fall or grow?",
                    query.message.chat.id,
                    query.message.message_id,
                    reply_markup=bitcoin(),
                )
            if callback_data["action"] == "up" and number > 5:

                await bot.edit_message_text(
                    f"\U0001F601 You win {b} money! \U0001F601",
                    query.message.chat.id,
                    query.message.message_id,
                    reply_markup=play_again(),
                )

                a += b

            elif callback_data["action"] == "down" and number < 5:

                await bot.edit_message_text(
                    f"\U0001F601 You win {b} money! \U0001F601",
                    query.message.chat.id,
                    query.message.message_id,
                    reply_markup=play_again(),
                )

                a += b

            elif callback_data["action"] == "down" and number > 5:

                await bot.edit_message_text(
                    f"\U0001F614 You lose {b} money! \U0001F614",
                    query.message.chat.id,
                    query.message.message_id,
                    reply_markup=play_again(),
                )

                a -= b

            elif callback_data["action"] == "up" and number < 5:

                await bot.edit_message_text(
                    f"\U0001F614 You lose {b} money! \U0001F614",
                    query.message.chat.id,
                    query.message.message_id,
                    reply_markup=play_again(),
                )

                a -= b

            if callback_data["action"] == "play_again":
                if a < 1:
                    await bot.edit_message_text(
                        "\U0001F915 Sorry! You have now money \U0001F915",
                        query.message.chat.id,
                        query.message.message_id,
                    )
                else:
                    await bot.edit_message_text(
                        f"\U0001F4B8 You have {a} money now! \U0001F4B8",
                        query.message.chat.id,
                        query.message.message_id,
                        reply_markup=main_game_keyboard(),
                    )
        else:
            await bot.edit_message_text(
                "\U000026D4	your bet is too big! \U000026D4",
                query.message.chat.id,
                query.message.message_id,
                reply_markup=main_game_keyboard(),
            )


def register_handlers(handler_dp: Dispatcher):
    handler_dp.register_message_handler(entry_point, commands="start")
    handler_dp.register_callback_query_handler(callback_results, markups.game_factory.filter())
