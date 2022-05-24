from pyrogram import Client
import config
import os

BOT_TOKEN = config.BOT_TOKEN
API_HASH = config.API_HASH
API_ID = config.API_ID

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    bot = Client(
        "Music-Downloader",
        bot_token=BOT_TOKEN,
        api_hash=API_HASH,
        api_id=API_ID,
        plugins=plugins
    )
    bot.run()
print("Bot Started!!")
