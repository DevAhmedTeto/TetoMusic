from pyrogram import Client
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from AarohiX import app
import os

@app.on_message(filters.command(["مح"], ""))
async def maker(client: Client, message: Message):
    await message.reply_video(
        video="https://telegra.ph/file/83e7bdf0e2dad83402160.mp4",
        caption="-القميل هذا  @{message.from_user.mention} 🫧\n- بعتلك بوسه يا  ❲  ❳ \n عيب كده اي المحن ده 🤭",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "المقبول 🫧", url=f"t.me/t7_au"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "القـابل 🤭", url=f"t.me/t7_au"
                    ),
                ],
            ]
        ),
    )
