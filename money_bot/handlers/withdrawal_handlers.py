import re

from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext

from money_bot.utils import db_utils, strings, states

try:
    from money_bot import local_config as config
except ImportError:
    from money_bot import example_config as config


def get_phone_number(message: types.Message):
    if len(message.text) == 12:
        if message.text[0] == "+":
            if len(re.search(r"(\d+)", message.text).group(0)) == 11:
                return message.text
    return None


async def get_money_amount(message: types.Message):
    if re.search(r"(\d+)", message.text).group(0) == message.text:
        if int(message.text) <= await db_utils.get_user_money_amount(message.from_user.id):
            return int(message.text)
    return None


def make_transaction():
    pass


async def withdraw_money(phone_number, money_amount, message):
    await message.answer(f"phone_number=\"{phone_number}\"\nmoney_amount=\"{money_amount}\"")


async def entry_point(message: types.Message):
    bot = await Bot.get_current().me
    withdrawal_text = strings.WITHDRAWAL_TEXT.format(
        user_money_amount=await db_utils.get_user_money_amount(message.from_user.id),
        user_referee_amount=await db_utils.get_user_referees_amount(message.from_user.id),
        money_amount_to_enable_withdrawal=config.MONEY_AMOUNT_TO_ENABLE_WITHDRAWAL,
        user_status=await db_utils.get_user_verify_status(message.from_user.id),
    )
    if await db_utils.get_user_referees_amount(message.from_user.id) < config.REFEREES_TO_ENABLE_WITHDRAWAL:
        await message.answer(
            withdrawal_text +
            strings.WITHDRAWAL_REFEREES_AMOUNT_PROBLEM_TEXT.format(
                required_referees_amount=config.REFEREES_TO_ENABLE_WITHDRAWAL,
                referral_link=strings.INVITE_LINK.format(bot_name=bot.username, referrer_id=message.from_user.id),
            )
        )
    elif await db_utils.get_user_money_amount(message.from_user.id) < config.MONEY_AMOUNT_TO_ENABLE_WITHDRAWAL:
        await message.answer(
            withdrawal_text +
            strings.WITHDRAWAL_MONEY_AMOUNT_PROBLEM_TEXT.format(
                required_money_amount=config.MONEY_AMOUNT_TO_ENABLE_WITHDRAWAL,
            )
        )
    elif config.REVIEW_MODE:
        await message.answer(strings.REVIEW_MODE_WARNING_TEXT)
    else:
        await states.WithdrawalStates.phone_number.set()
        await message.answer(strings.WITHDRAWAL_ASK_NUMBER_TEXT)


async def process_withdrawal_phone_number(message: types.Message, state: FSMContext):
    phone_number = get_phone_number(message)
    if phone_number:
        async with state.proxy() as data:
            data["phone_number"] = phone_number
        await states.WithdrawalStates.money_amount.set()
        await message.answer(strings.WITHDRAWAL_ASK_MONEY_AMOUNT_TEXT)
    else:
        await message.answer(strings.WITHDRAWAL_ASK_PHONE_NUMBER_ERROR_TEXT)


async def process_withdrawal_money_amount(message: types.Message, state: FSMContext):
    money_amount = await get_money_amount(message)
    if money_amount:
        async with state.proxy() as data:
            phone_number = data["phone_number"]
        await withdraw_money(phone_number, money_amount, message)
    else:
        await message.answer(strings.WITHDRAWAL_ASK_MONEY_AMOUNT_ERROR_TEXT)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(entry_point, state=states.GlobalStates.invite_btn)
    dp.register_message_handler(process_withdrawal_phone_number, state=states.WithdrawalStates.phone_number)
    dp.register_message_handler(process_withdrawal_money_amount, state=states.WithdrawalStates.money_amount)
