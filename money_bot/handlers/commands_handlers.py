import re

from aiogram import Bot, Dispatcher, types

from money_bot.utils import db_utils, markups, strings

try:
    from money_bot import local_config as config
except ImportError:
    from money_bot import example_config as config


def get_referrer_id(message_text: str):
    referrer_id_arg = re.search(r"referrer_id_(\d+)", message_text)
    return int(re.search(r"(\d+)", referrer_id_arg.group(0)).group(0)) if referrer_id_arg else None


async def process_setting_referrer_id(user_id: int, referrer_id: int):
    if user_id != referrer_id:
        current_user = await db_utils.get_user_by_id(user_id)
        if await db_utils.is_user_in_db(referrer_id):
            if not current_user.referrer_id:
                await db_utils.change_money_amount(referrer_id, config.REFERRAL_REWARD)
                await db_utils.set_referrer_id(user_id, referrer_id)
                return
    await db_utils.set_referrer_id(user_id, -1)


async def cmd_start(message: types.Message):
    referrer_id = get_referrer_id(message.text)
    bot = await Bot.get_current().me
    if referrer_id:
        await process_setting_referrer_id(message.from_user.id, referrer_id)
    else:
        await db_utils.set_referrer_id(message.from_user.id, -1)
    keyboard_markup = markups.get_main_menu_markup()
    await message.answer(
        f"Привет, {message.from_user.first_name} {message.from_user.last_name}!", reply_markup=keyboard_markup
    )
    await message.answer(
        strings.START_COMMAND_TEXT.format(
            required_referees_amount=config.REFEREES_TO_ENABLE_WITHDRAWAL,
            user_referee_amount=await db_utils.get_user_referees_amount(message.from_user.id),
            invite_link=strings.INVITE_LINK.format(bot_name=bot.username, referrer_id=message.from_user.id),
        )
    )


def register_handlers(handler_dp: Dispatcher):
    handler_dp.register_message_handler(cmd_start, commands="start", state="*")
