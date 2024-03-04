from pyrogram import Client, filters
from configs.heart import HEART
from configs.pb import HANDLERS
from PB.plugins.utils.utils import *


@Client.on_message(filters.command(commands='heart', prefixes=HANDLERS) & filters.me)
async def heart(_, message: pyrogram.types.Message) -> None:
    for frame in HEART:
        await try_edit_message(message, frame)
        await asyncio.sleep(0.16)
