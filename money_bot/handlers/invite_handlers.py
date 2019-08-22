from aiogram import Bot, Dispatcher, types

from money_bot.utils import db_utils, strings
from money_bot.utils.states import GlobalStates

try:
    from money_bot import local_config as config
except ImportError:
    from money_bot import example_config as config


async def entry_point(message: types.Message):
    bot = await Bot.get_current().me
    await message.answer(
        strings.INVITE_BUTTON_TEXT.format(
            referral_reward=config.REFERRAL_REWARD,
            user_referees_amount=await db_utils.get_user_referees_amount(message.from_user.id),
            referral_link=strings.INVITE_LINK.format(bot_name=bot.username, referrer_id=message.from_user.id),
        )
    )


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(entry_point, state=GlobalStates.invite_btn)
