import asyncio
import pyrogram
from pyrogram.errors import MessageIdInvalid, FloodWait
from PIL import Image, ImageFont, ImageDraw
from typing import Any


async def try_edit_message(message: pyrogram.types.Message, text: str) -> None:
    try:
        await message.edit_text(text)
    except MessageIdInvalid:
        print('[!] Message id invalid')
    except FloodWait as error:
        await asyncio.sleep(error.value)


async def create_postcard(
        image_path: str = None,
        font_path: str = None,
        font_size: int = None,
        xy: tuple[float, float] = (None, None),
        text: str = None,
        fill: Any | None = None,
        file_name: str = None,
) -> None:
    with Image.open(image_path) as image:
        font = ImageFont.truetype(font=font_path, size=font_size)

        draw = ImageDraw.Draw(image)
        draw.text(
            xy=xy,
            text=text,
            fill=fill,
            font=font,
        )

        image.save(file_name)
