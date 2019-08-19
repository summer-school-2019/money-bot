import logging

from aiogram import Bot, Dispatcher
from motor import MotorClient
from umongo import Instance

try:
    from money_bot import local_config as config
except ImportError:
    from money_bot import example_config as config

logging.basicConfig(level=logging.DEBUG)

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot)
db = MotorClient(config.DB_HOST)[config.DB_NAME]
instance = Instance(db)
