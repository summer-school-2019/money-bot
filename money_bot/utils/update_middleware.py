from aiogram import Dispatcher, types
from aiogram.dispatcher.middlewares import BaseMiddleware

from money_bot.utils.models import User


async def update_user(user_id, **kwargs):
    user = await User.find_one({"user_id": user_id})

    if user is None:
        new_user = User(user_id=user_id, **kwargs)
        await new_user.commit()
    else:
        for k, v in kwargs.items():
            setattr(user, k, v)
        await user.commit()


class UpdateUserMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: types.Message, data: dict):
        await update_user(
            user_id=message.chat.id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            username=message.from_user.username,
        )

    async def on_pre_process_callback_query(self, callback_query: types.CallbackQuery, data: dict):
        if callback_query.message and callback_query.message.from_user:
            await update_user(
                user_id=callback_query.message.chat.id,
                first_name=callback_query.from_user.first_name,
                last_name=callback_query.from_user.last_name,
                username=callback_query.from_user.username,
            )


def on_startup(dp: Dispatcher):
    dp.middleware.setup(UpdateUserMiddleware())
