from pyrogram import Client, filters
from config import Config
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply 

@Client.on_message(filters.command('rename'))
async def rename(bot, message):
    message = message.reply_to_message
    msg = await message.reply_text(text="yeni Video ismini yaz", reply_markup=ForceReply(True))
    msg_reply = msg.get_reply()
    new_name = msg_reply.text
    print(new_name)
