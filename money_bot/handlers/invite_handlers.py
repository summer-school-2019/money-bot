from aiogram import Bot, Dispatcher, types

from money_bot.utils import models
from money_bot.utils.states import GlobalStates


async def entry_point(message: types.Message):
    bot = await Bot.get_current().me
    current_user = await models.User.find_one({"user_id": message.from_user.id})
    referral_link = f"https://t.me/{bot.username}?start=referrer_id_{current_user.user_id}"
    await message.answer(referral_link)


def register_all_handlers(dp: Dispatcher):
    dp.register_message_handler(entry_point, state=GlobalStates.invite_menu)
