import logging

from aiogram import Bot, Dispatcher

from money_bot.utils.update_middleware import UpdateUserMiddleware

try:
    from money_bot import local_config as config
except ImportError:
    from money_bot import example_config as config

logging.basicConfig(level=logging.DEBUG)

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(UpdateUserMiddleware())
