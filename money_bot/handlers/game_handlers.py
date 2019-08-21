import random

from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher import FSMContext

from money_bot.utils import markups
from money_bot.utils.states import GlobalStates
from money_bot.utils.strings import GAME_MENU_TEXT
from money_bot.utils import db_utils

try:
    from money_bot import local_config as config
except ImportError:
    from money_bot import example_config as config


async def entry_point(message: types.Message, state: FSMContext):
    user = await db_utils.get_user_by_id(message.chat.id)
    if user.money < config.MONEY_TO_START_GAME:
        await message.answer(GAME_MENU_TEXT["no_money_to_start"])
        return
    async with state.proxy() as storage:
        storage["bet"] = 10
        await message.answer(
            GAME_MENU_TEXT["show_bet"].format(money=user.money, bet=storage["bet"]),
            reply_markup=markups.get_game_main_markup(),
        )


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

    if callback_data["action"] in ["play", "play_again"]:


        if callback_data["action"] == "play_again":
            if user.money < config.MONEY_TO_START_GAME:
                await bot.edit_message_text(
                    "\U0001F915 Sorry! You have now money \U0001F915",
                    query.message.chat.id,
                    query.message.message_id,
                )
            else:
                await bot.edit_message_text(
                    f"\U0001F4B8 You have somE!!!!!!!! money now! \U0001F4B8",
                    query.message.chat.id,
                    query.message.message_id,
                    reply_markup=markups.get_game_main_markup()
                )
        else:
            await bot.edit_message_text(
                "\U000026D4	your bet is too big! \U000026D4",
                query.message.chat.id,
                query.message.message_id,
                reply_markup=markups.get_game_main_markup(),
            )


async def check_bitcoin(query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    user = await db_utils.get_user_by_id(query.message.chat.id)  # very useful comment
    bot = Bot.get_current()
    async with state.proxy() as storage:
        number = random.randint(0, 20)
        if user.money >= storage["bet"]:
            if callback_data["action"] not in ["up", "down", "play_again"]:
                await bot.edit_message_text(
                    "Bitcoin will fall or grow?",
                    query.message.chat.id,
                    query.message.message_id,
                    reply_markup=markups.get_bitcoin_markup(),
                )
            if callback_data["action"] == "up" and number >= 5:

                await bot.edit_message_text(
                    "\U0001F601 You win {b} money! \U0001F601".format(b=storage["bet"]),
                    query.message.chat.id,
                    query.message.message_id,
                    reply_markup=markups.get_play_again_markup(),
                )
                    # TODO have such function for adding money
                user.money += storage["bet"]
                await user.commit()

            elif callback_data["action"] == "down" and number < 5:

                await bot.edit_message_text(
                    "\U0001F601 You win {b} money! \U0001F601".format(b=storage["bet"]),
                    query.message.chat.id,
                    query.message.message_id,
                    reply_markup=markups.get_play_again_markup(),
                )

                user.money += storage["bet"]
                await user.commit()

            elif callback_data["action"] == "down" and number >= 5:

                await bot.edit_message_text(
                    "\U0001F614 You lose {b} money! \U0001F614".format(b=storage["bet"]),
                    query.message.chat.id,
                    query.message.message_id,
                    reply_markup=markups.get_play_again_markup(),
            )

            user.money -= storage["bet"]
            await user.commit()

        elif callback_data["action"] == "up" and number < 5:

            await bot.edit_message_text(
                "\U0001F614 You lose {b} money! \U0001F614".format(b=storage["bet"]),
                query.message.chat.id,
                query.message.message_id,
                reply_markup=markups.get_play_again_markup(),
            )

            user.money -= storage["bet"]
            await user.commit()


def register_handlers(handler_dp: Dispatcher):
    handler_dp.register_message_handler(entry_point, state=GlobalStates.play_btn)
    handler_dp.register_callback_query_handler(callback_results, markups.game_factory.filter(),
                                               state=GlobalStates.play_btn)
    handler_dp.register_callback_query_handler(check_bitcoin, markups.game_bitcoin_factory.filter(),
                                               state=GlobalStates.play_btn)
