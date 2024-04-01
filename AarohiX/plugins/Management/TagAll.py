import asyncio
from pyrogram.enums import ChatType, ChatMemberStatus
from AarohiX import app
from pyrogram import filters
from AarohiX.utils.admin_check import admin_filter


SPAM_CHATS = {}

@app.on_message(filters.command(["تاك", "all"], prefixes=["/", "@", "", "#"]) & admin_filter)
async def tag_all_users(_, message):
    global SPAM_CHATS
    chat_id = message.chat.id
    if len(message.text.split()) == 1:
        await message.reply_text("**◍ قم بعمل رييلي علي الرساله مثل :*@all تيتو \n\n √*")
        return

    text = message.text.split(None, 1)[1]
    if text:
        await message.reply_text("**◍ تم بدأ عمل المنشن بنجاح**\n\n**๏ يتم عمل تاك كل 7 ثواني لعدم التهنيج**\n\n**➥ لايقاف التاج ارسل » ايقاف المنشن**")

    SPAM_CHATS[chat_id] = True
    f = True
    while f:
        if SPAM_CHATS.get(chat_id) == False:
            await message.reply_text("**◍ تم ايقاف المنشن بنجاح \n\n√**")
            break
        usernum = 0
        usertxt = ""
        try:
            async for m in app.get_chat_members(message.chat.id):
                if m.user.is_bot:
                    continue
                usernum+= 1
                usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
                if usernum == 5:
                    await app.send_message(message.chat.id, f'{text}\n{usertxt}\n\n|| ➥ ᴏғғ ᴛᴀɢɢɪɴɢ ʙʏ » /stoputag ||')
                    usernum = 0
                    usertxt = ""
                    await asyncio.sleep(7)
        except Exception as e:
            print(e)

@app.on_message(filters.command(["ايقاف المنشن", "ايقاف التاك", "وقف المنشن", "offuall", "utagoff", "ualloff"], prefixes=["/", "", "@", "#"]) & admin_filter)
async def stop_tagging(_, message):
    global SPAM_CHATS
    chat_id = message.chat.id
    if SPAM_CHATS.get(chat_id) == True:
        SPAM_CHATS[chat_id] = False
        return await message.reply_text("**◍ الرجاء الانتظار حتي ايقاف التاج \n\n √**")
    else:
        await message.reply_text("**◍ تم بنجاح الايقاف \n\n √**")