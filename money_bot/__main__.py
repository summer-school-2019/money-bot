import aiogram
from aiogram import executor

from money_bot.initialization import dp, on_startup

try:
    from money_bot import local_config as config
except ImportError:
    from money_bot import example_config as config


if __name__ == "__main__":
    executor.start_webhook(
        dp, on_startup=on_startup, webhook_path=config.WEBHOOK_PATH, host=config.WEBHOOK_HOST, port=config.WEBHOOK_PORT
    )
