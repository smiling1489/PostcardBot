from pyrogram import Client
from dotenv import dotenv_values

ENV_CONFIG = dotenv_values('.env')

PB = Client(
    name='PostcardBot',
    api_id=ENV_CONFIG['API_ID'],
    api_hash=ENV_CONFIG['API_HASH'],
    plugins=dict(root=f'{__name__}/plugins'),
)
