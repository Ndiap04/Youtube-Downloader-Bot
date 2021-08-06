from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
  return ctx.replyWithPhoto({ url: 'https://telegra.ph/file/c3f19e89e109e1534b02a.jpg' 
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("👿 Channel", url="https://t.me/fckyoupeople1")],
        [InlineKeyboardButton(
            "🌹 Donasi", url="https://t.me/pikyus1")]
    ])
    welcomed = f"Halo🐣 <b>{message.from_user.first_name}</b>\n 🐈 **Saya Adalah Bot Yang Dapat Mengunduh Lagu Dan Video**\n😉 **Cukup Ketik /help Untuk Mengetahui Perintahnya**"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
