import random

from aiogram import Bot, Dispatcher, types
from aiogram.utils.callback_data import CallbackData

from money_bot.utils import db_utils
from money_bot.utils.states import GlobalStates

change_sum = CallbackData("sum", "action", "value")


def main_game_keyboard():
    return types.InlineKeyboardMarkup(row_width=4).add(
        types.InlineKeyboardButton("1", callback_data=change_sum.new(action="make", value="1")),
        types.InlineKeyboardButton("10", callback_data=change_sum.new(action="make", value="10")),
        types.InlineKeyboardButton("50", callback_data=change_sum.new(action="make", value="50")),
        types.InlineKeyboardButton("100", callback_data=change_sum.new(action="make", value="100")),
        types.InlineKeyboardButton("1000", callback_data=change_sum.new(action="make", value="1000")),
        types.InlineKeyboardButton("+ 1", callback_data=change_sum.new(action="plus", value="1")),
        types.InlineKeyboardButton("+ 5", callback_data=change_sum.new(action="plus", value="5")),
        types.InlineKeyboardButton("- 1", callback_data=change_sum.new(action="minus", value="1")),
        types.InlineKeyboardButton("- 5", callback_data=change_sum.new(action="minus", value="5")),
        types.InlineKeyboardButton(
            "\U0001F3B2 play \U0001F3B2", callback_data=change_sum.new(action="play", value="-")
        ),
        types.InlineKeyboardButton(
            "\U0001F4DC rules \U0001F4DC", callback_data=change_sum.new(action="show_rules", value="-")
        ),
    )


def get_menu_button():
    return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton(
            "\U0001F519 menu \U0001F519", callback_data=change_sum.new(action="menu", value="-")
        )
    )


def bitcoin():
    return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton("\U00002B06 grow \U00002B06", callback_data=change_sum.new(action="up", value="-")),
        types.InlineKeyboardButton(
            "\U00002B07 fall \U00002B07", callback_data=change_sum.new(action="down", value="-")
        ),
    )


def play_again():
    return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton(
            "\U0001F3B0 Играть снова! \U0001F3B0", callback_data=change_sum.new(action="play_again", value="-")
        )
    )


async def entry_point(message: types.Message):
    bot = Bot.get_current()
    user = await db_utils.get_user_by_id(message.from_user.id)
    await bot.send_message(
        message.chat.id,
        f"\U0001F4B8       У вас есть {user.money} рублей!         \U0001F4B8",
        reply_markup=main_game_keyboard(),
    )


async def callback_results(query: types.CallbackQuery, callback_data: dict):
    bot = Bot.get_current()
    user = await db_utils.get_user_by_id(query.message.chat.id)
    await query.answer()

    if callback_data["action"] in ["make", "plus", "minus", "show_current_sum"]:

        if callback_data["action"] == "make" and callback_data["value"] == "1":
            user.current_bet = 1
            await user.commit()

        if callback_data["action"] == "make" and callback_data["value"] == "10":
            user.current_bet = 10
            await user.commit()

        if callback_data["action"] == "make" and callback_data["value"] == "50":
            user.current_bet = 50
            await user.commit()

        if callback_data["action"] == "make" and callback_data["value"] == "100":
            user.current_bet = 100
            await user.commit()

        if callback_data["action"] == "make" and callback_data["value"] == "1000":
            user.current_bet = 1000
            await user.commit()

        if callback_data["action"] == "plus" and callback_data["value"] == "1":
            user.current_bet += 1
            await user.commit()

        if callback_data["action"] == "plus" and callback_data["value"] == "5":
            user.current_bet += 5
            await user.commit()

        if callback_data["action"] == "minus" and callback_data["value"] == "1":
            if user.current_bet >= 1:
                user.current_bet -= 1
                await user.commit()

        if callback_data["action"] == "minus" and callback_data["value"] == "5":
            if user.current_bet >= 5:
                user.current_bet -= 5
                await user.commit()
            else:
                user.current_bet = 0
                await user.commit()

        await bot.edit_message_text(
            f"\U0001F4B8 У вас есть {user.money} рублей и ваша ставка {user.current_bet} рублей \U0001F4B8",
            query.message.chat.id,
            query.message.message_id,
            reply_markup=main_game_keyboard(),
        )
    if callback_data["action"] == "show_rules":

        await bot.send_message(
            query.message.chat.id,
            "Курс биткоина меняется каждую секунду!\nУгадай как он изменится и выиграй деньги!\nВы не можете поставить больше, чем у вас есть.",
            reply_markup=get_menu_button(),
        )

    if callback_data["action"] == "menu":
        await bot.send_message(
            query.message.chat.id,
            f"\U0001F4B8 У вас есть {user.money} рублей! \U0001F4B8",
            reply_markup=main_game_keyboard(),
        )

    if callback_data["action"] in ["play", "up", "down", "play_again"]:
        if user.money >= user.current_bet:
            number = random.randint(0, 20)
            if callback_data["action"] not in ["up", "down", "play_again"]:
                await bot.edit_message_text(
                    "Биткоин вырастет или упадет?",
                    query.message.chat.id,
                    query.message.message_id,
                    reply_markup=bitcoin(),
                )
            if callback_data["action"] == "up" and number > 5:

                await bot.edit_message_text(
                    f"\U0001F601 Вы выиграли {user.current_bet} рублей! \U0001F601",
                    query.message.chat.id,
                    query.message.message_id,
                    reply_markup=play_again(),
                )

                user.money += user.current_bet
                await user.commit()
                await db_utils.change_money_amount(query.from_user.id, user.current_bet)

            elif callback_data["action"] == "down" and number < 5:

                await bot.edit_message_text(
                    f"\U0001F601 Вы выиграли {user.current_bet} рублей! \U0001F601",
                    query.message.chat.id,
                    query.message.message_id,
                    reply_markup=play_again(),
                )

                user.money += user.current_bet
                await user.commit()
                await db_utils.change_money_amount(query.from_user.id, user.current_bet)

            elif callback_data["action"] == "down" and number > 5:

                await bot.edit_message_text(
                    f"\U0001F614 Вы потеряли {user.current_bet} рублей! \U0001F614",
                    query.message.chat.id,
                    query.message.message_id,
                    reply_markup=play_again(),
                )

                user.money -= user.current_bet
                await user.commit()
                await db_utils.change_money_amount(query.from_user.id, -user.current_bet)

            elif callback_data["action"] == "up" and number < 5:

                await bot.edit_message_text(
                    f"\U0001F614 Вы проиграли {user.current_bet} рублей! \U0001F614",
                    query.message.chat.id,
                    query.message.message_id,
                    reply_markup=play_again(),
                )

                user.money -= user.current_bet
                await user.commit()
                await db_utils.change_money_amount(query.from_user.id, -user.current_bet)

            if callback_data["action"] == "play_again":
                if user.money < 1:
                    await bot.edit_message_text(
                        "\U0001F915 У вас недостаточно денег \U0001F915",
                        query.message.chat.id,
                        query.message.message_id,
                    )
                else:
                    await bot.edit_message_text(
                        f"\U0001F4B8 У вас есть {user.money} рублей! \U0001F4B8",
                        query.message.chat.id,
                        query.message.message_id,
                        reply_markup=main_game_keyboard(),
                    )
        else:
            await bot.edit_message_text(
                "\U000026D4	Ваша ставка слишком большая! \U000026D4",
                query.message.chat.id,
                query.message.message_id,
                reply_markup=main_game_keyboard(),
            )


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(entry_point, state=GlobalStates.play_btn)
    dp.register_callback_query_handler(
        callback_results,
        change_sum.filter(
            action=[
                "make",
                "plus",
                "show_current_sum",
                "minus",
                "play",
                "menu",
                "up",
                "down",
                "play_again",
                "show_rules",
            ]
        ),
        state=GlobalStates.play_btn,
    )
