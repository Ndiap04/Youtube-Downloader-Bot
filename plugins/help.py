from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"🌹 **Panduan Bot**\n ➡️ **Kirim Link Video Youtube Yang Kamu Inginkan**\n ➡️ **Tentukan Resolusi Video Yang Kamu Inginkan**\n ➡️ **Bot Tidak Dapat Mendownload Playlist Dari Youtube**\n➡️ **Untuk Memulai Download Silakan Kirim Link Pada Bot**"
    await message.reply_text(helptxt)
