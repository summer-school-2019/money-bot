from aiogram import executor

from money_bot.initialization import dp

if __name__ == "__main__":
    executor.start_polling(dp)
