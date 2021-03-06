import os
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message
import config

OWNER = config.OWNER

# -----------------------------------------------------------------------------------

Help_text = """<u>ð**Available Commands**</u>
ð /spotify - **To Download Songs from Spotify.ð¥\nEg** : `/spotify Faded`

ð /s - **To download audio songs from YouTube (Fastest method).ð\nEg** : `/s Believer`

ð /v - **To download best Quality videos.ð¦\nEg** : `/v Believer`

ð /saavn - **To Download Songs from Jiosaavn.ð¶\nEg** : `/saavn Verithanam`

ð /lyrics - **To Get Song Lyrics.**

ð /yts - **To Search Given Query in YouTube**.ð\n`/yts Avengers`"""

# ------------------------------------------------------------------------------------


About_text = """--<u>**About Me ð**</u>--
ð É´á´á´á´ : `Music Downloader`

ð§âð» á´á´á´ á´Êá´á´á´Ê : [Peter Parker](https://t.me/Peterparker6)

ð Êá´É´É¢á´á´É¢á´ : `Python3`

ð sá´Êá´ á´Ê : [Heroku](https://heroku.com/)

ð® ÊÉªÊÊá´ÊÊ : [Pyrogram](https://docs.pyrogram.org/)

ð¨ Êá´ÉªÊá´ sá´á´á´s : `V1.0 [Stable]`

â­ sá´á´Êá´á´ á´á´á´á´ : [ð¤¥Click here](https://github.com)"""

# ------------------------------------------------------------------------------------

@Client.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "close":
        await update.message.delete(True)
        try:
            await update.message.reply_to_message.delete(True)
        except BaseException:
            pass

@Client.on_message(filters.command("start") & filters.private)
async def startprivate(client, message):
    chat_id = message.from_user.id
    joinButton = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Developer ð¤ ", url=f'https://telegram.dog/{OWNER}'),
                InlineKeyboardButton("Source ðª", callback_data="source")
            ],
            [
                InlineKeyboardButton('sá´á´Êá´Ê ÉªÉ´ÊÉªÉ´á´', switch_inline_query_current_chat=f'')
            ]
        ]
    )
    await message.reply_text(text=config.START_MSG.format(message.from_user.mention), quote=True, reply_markup=joinButton)


@Client.on_message(filters.command('help')  & filters.private)
async def help(client, message):
       Help_buttons = InlineKeyboardMarkup([[InlineKeyboardButton('ðð¹ð¼ðð² â', callback_data="close")]])
       await message.reply_text(text=Help_text, reply_markup=Help_buttons, quote=True)


@Client.on_message(filters.command('about')  & filters.private)
async def about(client, message):
       About_buttons = InlineKeyboardMarkup([[InlineKeyboardButton('ðð¹ð¼ðð² â', callback_data="close")]])
       await message.reply_text(text=About_text, reply_markup=About_buttons, quote=True)
