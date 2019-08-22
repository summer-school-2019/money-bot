# Config file
BOT_TOKEN = ""

CLUSTER_NAME = ""
DB_NAME = ""
DB_USER_NAME = ""
DB_USER_PASSWORD = ""
DB_HOST = f"mongodb+srv://{DB_USER_NAME}:{DB_USER_PASSWORD}@{CLUSTER_NAME}/{DB_NAME}?retryWrites=true&w=majority"

JOIN_GROUP_REWARD = 1
REFERRAL_REWARD = 2
REFEREES_TO_ENABLE_WITHDRAWAL = 5
MONEY_AMOUNT_TO_ENABLE_WITHDRAWAL = 100
