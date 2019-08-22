import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
QIWI_TOKEN = os.getenv("QIWI_TOKEN")

WEBHOOK_HOST = os.getenv("WEBHOOK_HOST")
WEBHOOK_PORT = os.getenv("PORT")
WEBHOOK_PATH = f"/{BOT_TOKEN}"
WEBHOOK_URL = WEBHOOK_HOST + WEBHOOK_PATH
SERVER_HOST = "0.0.0.0"

CLUSTER_NAME = ""
DB_NAME = os.getenv("DB_NAME")
DB_USER_NAME = ""
DB_USER_PASSWORD = ""
DB_HOST = os.getenv("MONGODB_HOST")

JOIN_GROUP_REWARD = 20
REFERRAL_REWARD = 50
REFEREES_TO_ENABLE_WITHDRAWAL = 3
MONEY_AMOUNT_TO_ENABLE_WITHDRAWAL = 100
REVIEW_MODE_MONEY_AMOUNT = 1

REVIEW_MODE = True
