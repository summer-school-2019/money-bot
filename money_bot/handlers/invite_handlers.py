from aiogram import Bot, Dispatcher, types

from money_bot.utils import models, strings
from money_bot.utils.states import GlobalStates


async def entry_point(message: types.Message):
    bot = await Bot.get_current().me
    referral_link = strings.INVITE_LINK.format(bot_name=bot.username, referrer_id=message.from_user.id)
    await message.answer(referral_link)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(entry_point, state=GlobalStates.invite_btn)
