from pyrogram.types import InlineKeyboardButton
from Uputt import CMD_HELP
class Data:

    text_help_menu = (
        "**Menu Inline Pyro-Rizki**\n**Prefixes:** ., ?, !, *"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("ᴘᴇɴᴄᴇᴛ ᴀᴊᴀ", callback_data="reopen")]]
