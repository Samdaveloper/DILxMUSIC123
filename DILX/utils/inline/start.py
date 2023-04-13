from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from DILX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ [✘𓂆𓂇Đ] 🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❣️ʜᴇʟᴩ❣️",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="❤‍🔥sᴇᴛᴛɪɴɢs❤‍🔥", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💝ᴍᴀɪɴᴛᴀɪɴᴇʀ[✘𓂆𓂇Đ]💝", user_id=OWNER),
            InlineKeyboardButton(
                text="🥰sᴜᴩᴩᴏʀᴛ[✘𓂆𓂇Đ]🥰", url=config.SUPPORT_GROUP
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ [✘𓂆𓂇Đ]🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥺ʜᴇʟᴩ🥺", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="💝ᴍᴀɪɴᴛᴀɪɴᴇʀ[✘𓂆𓂇Đ]💝", user_id=OWNER),
            InlineKeyboardButton(
                text="sᴜᴩᴩᴏʀᴛ[✘𓂆𓂇Đ]", url=config.SUPPORT_GROUP
            ),
        ],
        [
            InlineKeyboardButton(
                    text="🤨sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ🤨", url=config.UPSTREAM_REPO
                )
        ],
     ]
    return buttons
