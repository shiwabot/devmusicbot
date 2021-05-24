from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery


@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"**Hello, I'm Vc music Player**. I can play music in voice chats. Hit /help to know about my commands.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Commands", callback_data="start_cmds"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Updates", url="https://t.me/Denvil_bots"
                    ),
                    InlineKeyboardButton(
                        "Support", url="https://t.me/MusicBotEnjoy_group"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Add me to your group.", url="t.me/AnieMusic_bot?startgroup=true"
                    )
                ],
            ]
        ))
      
@Client.on_callback_query(filters.regex("^start_cmds$"))
async def start_callback(_, q: CallbackQuery):
    user_id = q.from_user.id
    await q.message.edit_text("Here you can find commands to use me.",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Admin", url="https://telegra.ph/Starpaneltop-05-16"
                    ),
                    InlineKeyboardButton(
                        "Users", url="https://telegra.ph/Starpaneltop-05-16-2"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Close menu", callback_data="start_close"
                    )
                ],
            ]
        ))
    await q.answer("Help menu opened.", show_alert=True)
    return
  
@Client.on_callback_query(filters.regex("^start_close$"))
async def close_callback(_, q: CallbackQuery):
    user_id = q.from_user.id
    await q.message.edit_text("**Menu closed. Send /start to start again.**")
    await q.answer("Closed Menu.", show_alert=True)
    return
  
@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        "Hello, I'm Online ^_^",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "How to use me?", callback_data="start_cmds"
                    )
                ]
            ]
        ),
    )
