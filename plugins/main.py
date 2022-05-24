import os
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message
import config

# -----------------------------------------------------------------------------------

Help_text = """<u>🌟**Available Commands**</u>
👉 /spotify - **To Download Songs from Spotify.🔥\nEg** : `/spotify Faded`

👉 /s - **To download audio songs from YouTube (Fastest method).💞\nEg** : `/s Believer`

👉 /v - **To download best Quality videos.🎦\nEg** : `/v Believer`

👉 /saavn - **To Download Songs from Jiosaavn.🎶\nEg** : `/saavn Verithanam`

👉 /lyrics - **To Get Song Lyrics.**

👉 /yts - **To Search Given Query in YouTube**.😋\n`/yts Avengers`"""

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
                InlineKeyboardButton("Developer 🤠", url="https://telegram.dog/config.OWNER}"),
                InlineKeyboardButton("Source 😪", callback_data="source")
            ],
            [
                InlineKeyboardButton('sᴇᴀʀᴄʜ ɪɴʟɪɴᴇ', switch_inline_query_current_chat=f'')
            ]
        ]
    )
    await message.reply_text(text=config.START_MSG.format(message.from_user.mention), quote=True, reply_markup=joinButton)


@Client.on_message(filters.command('help')  & filters.private)
async def help(client, message):
       Help_buttons = InlineKeyboardMarkup([[InlineKeyboardButton('𝗖𝗹𝗼𝘀𝗲 ❌', callback_data="close")]])
       await message.reply_text(text=Help_text, reply_markup=Help_buttons, quote=True)


@Client.on_message(filters.command('about')  & filters.private)
async def about(client, message):
       About_buttons = InlineKeyboardMarkup([[InlineKeyboardButton('𝗖𝗹𝗼𝘀𝗲 ❌', callback_data="close")]])
       await message.reply_text(text=About_text, reply_markup=About_buttons, quote=True)
