import asyncio


import random


from AarohiX import app


from pyrogram.types import (InlineKeyboardButton,


                            InlineKeyboardMarkup, Message)


from pyrogram import filters, Client





@app.on_message(
    filters.command(["مميزات","مميزات تيتو"], "")
& filters.group
 )
async def mmmezat(client, message):
        await message.reply_text(f"""**⦿ قايمه مميزات سورس تيتو :\n
╮⦿  المطور
│᚜⦿ سؤال
│᚜⦿ مين في الكول 
│᚜⦿ تفعيل الاذان
│᚜⦿ كت
│᚜⦿ احكام
│᚜⦿ افتح الكول
│᚜⦿ احرف
│᚜⦿ الرابط
│᚜⦿ البنك 
│᚜⦿ منع تصفيه تلقائي
│᚜⦿ رفع مشرف
│᚜⦿ شعر
│᚜⦿ نادي المطور
│᚜⦿ زخرفه
│᚜⦿ مميزات
│᚜⦿ همسه
│᚜⦿ يوت
│᚜⦿ تحميل
│᚜⦿ لو خيروك
│᚜⦿ معلومات الجروب
│᚜⦿ طرد كتم
│᚜⦿ تلكراف ميديا
│᚜⦿ اسكرين 
│᚜⦿ صراحه
│᚜⦿ صور
│᚜⦿ صور بنات 
│᚜⦿ صور شباب
│᚜⦿ السورس 
│᚜⦿ كتم
│᚜⦿ اقتباس
│᚜⦿ هيدرات
│᚜⦿ اذكار 
╯⦿  بث مباشر للقنوات 
[𝗦𝗼𝘂𝗿𝗰𝗲 𝗧𝗲𝘁𝗼](https://t.me/WX_PM) """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴛᴇᴛσ", url=f"https://t.me/WZAERE"),                        
                 ],[
                InlineKeyboardButton(
                        "close", callback_data="close"),
               ],
          ]
        ),
    )

