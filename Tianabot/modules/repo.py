from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from Tianabot import pbot, START_IMG, SUPPORT_CHAT


@pbot.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_photo(
        photo=START_IMG,
        caption=f"""✨😍 **Hey I'm 『 𝐑ᴏᴍΛ𝐍𝐂Ξ 』✨😍** 

**👑Owner : [iMzaynKING](https://t.me/iMzaynKING)**
**⚡Python Version :** `{y()}`
**⚡Library Version :** `{o}`
**⚡Telethon Version :** `{s}`
**⚡Pyrogram Version :** `{z}`

**💞Click on Button Bellow For More💞**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="💎❰𝐒ᴏᴜʀᴄᴇ❱", url=f"https://t.me/KING_BOTz"), 
                    InlineKeyboardButton(
                        "⭕️❰𝐒ᴜᴘᴘᴏʀᴛ❱", url=f"https://t.me/TAMIL_CHATBOX")
                ]
            ]
        )
    )
