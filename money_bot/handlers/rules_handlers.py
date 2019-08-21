from aiogram import Bot, Dispatcher, types

from money_bot.utils import db_utils, strings
from money_bot.utils.states import GlobalStates

try:
    from money_bot import local_config as config
except ImportError:
    from money_bot import example_config as config


async def entry_point(message: types.Message):
    bot = await Bot.get_current().me
    user_referee_amount = await db_utils.get_user_referees_amount(message.from_user.id)
    user_money_amount = await db_utils.get_user_money_amount(message.from_user.id)
    await message.answer(
        strings.RULES_BUTTON_TEXT.format(
            required_referee_amount=config.REFEREES_TO_ENABLE_WITHDRAWAL,
            user_referee_amount=user_referee_amount,
            user_referral_link=strings.INVITE_LINK.format(bot_name=bot.username, referrer_id=message.from_user.id),
            referral_fee=config.REFERRAL_REWARD,
            money_to_enable_withdrawal=config.MONEY_AMOUNT_TO_ENABLE_WITHDRAWAL,
            user_money_amount=user_money_amount,
        )
    )


def register_all_handlers(dp: Dispatcher):
    dp.register_message_handler(entry_point, state=GlobalStates.rules_btn)
