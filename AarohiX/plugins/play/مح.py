from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config


@app.on_message(filters.command("مح") &  filters.private & SUDOERS)
)
async def maker(client: Client, message: Message):
    await message.reply_video(
        video="https://telegra.ph/file/dd1298fa95a28d6962705.jpg",
        caption="※ هذا القميل {message.from_user.mention} \n※ بعتلك بوسه يا 😘♥ [{user.first_name}](tg://user?id={user.id})\n عيب كده اي المحن ده 😹",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "المقبول 🤭", url=f"القميل[{user.first_name}](tg://user?id={user.id})"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "القابل", url=f"القميله{message.from_user.mention}"
                    ),
                ],
            ]
        ),
    )
