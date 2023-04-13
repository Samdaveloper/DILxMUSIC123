import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from DILX import LOGGER, app, userbot
from DILX.core.call import DIL
from DILX.plugins import ALL_MODULES
from DILX.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("DILX").error(
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("DILX").warning(
            "Sur spotify id aur secret toh daala hi nahi aapne ab toh spotify se nahi chala paaoge gaane By Dil."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("DILX.plugins." + all_module)
    LOGGER("DILX.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await DIL.start()
    try:
        await DIL.stream_decall("https://graph.org/file/98f19edad84aa1a8f8d98.jpg")
    except:
        pass
    try:
        await DIL.stream_call(
            "https://graph.org/file/2216295471987f377677c.jpg"
        )
    except NoActiveGroupCall:
        LOGGER("DILX").error(
            "[ERROR] - \n\nHey Baby, firstly open telegram and turn on voice chat in Logger Group else fu*k off. If you ever ended voice chat in log group i will stop working and users will fu*k you up."
        )
        sys.exit()
    except:
        pass
    await DIL.decorators()
    LOGGER("DILX").info("✘𓂆𓂇Đ")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("DILX").info("Stopping Music Bot...")
