from pyrogram import Client
import config
import os

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    bot = Client(
        "Music-Downloader",
        bot_token=config.BOT_TOKEN,
        api_hash=config.API_HASH,
        api_id=config.API_ID,
        plugins=plugins
    )
    bot.run()
print("Bot Started!!")
