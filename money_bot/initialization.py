import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from money_bot.utils import register_all_handlers, update_middleware


async def on_startup():
    await bot.set_webhook(config.WEBHOOK_URL)


try:
    from money_bot import local_config as config
except ImportError:
    from money_bot import example_config as config

logging.basicConfig(level=logging.DEBUG)

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

update_middleware.on_startup(dp)

register_all_handlers.register_all_handlers(dp)
