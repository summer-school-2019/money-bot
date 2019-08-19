from aiogram import executor

from money_bot.initialization import dp
from money_bot.utils import register_all_handlers

register_all_handlers.register_all_handlers(dp)


if __name__ == "__main__":
    executor.start_polling(dp)
