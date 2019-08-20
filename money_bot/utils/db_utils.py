from money_bot.utils.models import User


async def get_user_by_id(user_id):
    return await User.find_one({"user_id": int(user_id)})


async def is_user_in_db(user_id):
    return bool(await get_user_by_id(int(user_id)))


async def set_referrer_id(user_id, referrer_id):
    user = await get_user_by_id(int(user_id))
    user.referrer_id = int(referrer_id)
    await user.commit()


async def increase_money_amount(user_id, increase_value_amount):
    user = await get_user_by_id(int(user_id))
    user.money += increase_value_amount
    await user.commit()