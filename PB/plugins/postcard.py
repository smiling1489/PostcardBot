from pyrogram import Client, filters
from configs.pb import HANDLERS
from PB.plugins.utils.utils import *


@Client.on_message(filters.command(commands='postcard', prefixes=HANDLERS) & filters.me)
async def postcard(_, message: pyrogram.types.Message):
    await message.delete()

    await create_postcard(
        image_path=f'{__name__}/../data/postcards/smilingPC.jpg',
        font_path=f'{__name__}/../data/fonts/Pacifico-Regular.ttf',
        font_size=44,
        xy=(70, 6),
        text=message.text.split(sep=" ", maxsplit=1)[1],
        fill=(0, 0, 0, 0),
        file_name='tempPC.jpg',
    )

    await message.reply_photo('tempPC.jpg')
