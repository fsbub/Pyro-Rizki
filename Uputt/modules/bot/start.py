#Credit Bye Geez|Ram
#Thanks To All Dev


from meliodas import app
from pyrogram import filters


@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
   await message.reply_text("Pyro-Rizki Telah Aktif")
