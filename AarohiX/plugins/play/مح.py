from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config
from pyrogram.errors import FloodWait



@app.on_message(command("مح"))
async def tnzelnmla(client:Client, message:Message):
  if message.reply_to_message.from_user.mention in zog:
    zog.remove(message.reply_to_message.from_user.mention)
     await message.reply_video(
        video="https://telegra.ph/file/83e7bdf0e2dad83402160.mp4",
        caption="•القميل هذا ✨♥ https://t.me/{message.from_user.username} \n※ بعتلك بوسه يا 😘♥ @ \nعيب كده اي المحن ده 😹",
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
