import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from Aarohix import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from Aarohix import app




#write by tito @G_7_Rr
@app.on_message(command(["بوت حذف", "بوت حسابات", "بوت حدف"]) & filters.group & ~filters.edited)
async def svksksa(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/a6137caa707bdb1247d7c.jpg",
        caption=f"""[خش احذف محدش هيمسك فيك يلا غور فداهية 😂❤](https://t.me/LC6BOT)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• اضـغـط لـدخول للـبوت", url=f"https://t.me/LC6BOT")
                ]
           ]
        ),
    )
   
   



    
   
   
   
