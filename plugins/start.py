from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🅲🅷🅰🅽🅽🅴🅻", url="https://t.me/fckyoupeople1")],
    ])
    welcomed = f"**Hai!!**<b>{message.from_user.first_name}</b>\nꜱᴀʏᴀ ᴀᴅᴀʟᴀʜ ʙᴏᴛ ʏᴀɴɢ ᴅᴀᴘᴀᴛ ᴍᴇɴɢᴜɴᴅᴜʜ ʟᴀɢᴜ ᴅᴀɴ ᴠɪᴅᴇᴏ ᴅᴀʀɪ [ʏᴏᴜᴛᴜʙᴇ](https://telegra.ph/file/b9d14184caad443f63d59.mp4), ᴄᴜᴋᴜᴘ ᴋᴇᴛɪᴋ /ʜᴇʟᴘ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ᴘᴇʀɪɴᴛᴀʜɴʏᴀ."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
