from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Saat ini hanya mendukung YouTube Single (tanpa daftar putar) Cukup kirim URL YouTube"
    await message.reply_text(helptxt)
