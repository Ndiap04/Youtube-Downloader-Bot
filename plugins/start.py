from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("👿 Channel", url="https://t.me/fckyoupeople1")],
    ])
    welcomed = f"Halo🐣 <b>{message.from_user.first_name}</b>\n 🐈 **Saya Adalah Bot Yang Dapat Mengunduh Lagu Dan Video Dari** [YouTube](https://telegra.ph/file/4341cfadb0abff6f6e60d.jpg)\n😉 **Cukup Ketik /help Untuk Mengetahui Perintahnya**"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
