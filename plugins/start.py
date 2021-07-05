from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("👿 Channel", url="https://t.me/fckyoupeople1")],
        [InlineKeyboardButton(
            "🌹 Donasi", url="https://t.me/pikyus1")]
    ])
    welcomed = f"Hey🐣 <b>{message.from_user.first_name}</b>\n **Saya Dapat MengDownload Video Dari Youtube**\n**Cukup Ketik /help Untuk Mengdownload**"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
