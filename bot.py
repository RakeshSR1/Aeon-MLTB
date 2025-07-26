from pyrogram import Client, filters

API_ID = "23272804"
API_HASH = "bbd029520a44a558573fb76375c6d681"
BOT_TOKEN = "8016890106:AAECqZzikJ6DkXXSkEsNAKU5r9qVWUpwbMA"
DOMAIN = "https://LocalHost:800"

app = Client("FileToLinkBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.document | filters.video | filters.audio)
async def save_file(client, message):
    media = message.document or message.video or message.audio
    filename = media.file_name or f"{message.message_id}.bin"
    path = f"downloads/{filename}"
    await message.download(file_name=path)

    link = f"{DOMAIN}/file/{message.message_id}/{filename}"
    await message.reply_text(f"🔗 Your File Link:\n{link}")


app.run()

# gdrive_uploader
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from gdrive_uploader import upload_to_gdrive

API_ID = 23272804  # Replace with your API_ID
API_HASH = "bbd029520a44a558573fb76375c6d681"  # Replace with your API_HASH
BOT_TOKEN = (
    "8016890106:AAECqZzikJ6DkXXSkEsNAKU5r9qVWUpwbMA"  # Replace with your bot token
)

bot = Client("leechbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
temp_files = {}


@bot.on_message(filters.document)
async def receive_file(bot, message):
    file = await message.download()
    temp_files[message.id] = file

    await message.reply(
        "Do you want GDrive Link?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📤 Yes, Upload to GDrive", callback_data=f"gup_{message.id}"
                    )
                ]
            ]
        ),
    )


@bot.on_callback_query(filters.regex("gup_"))
async def handle_upload(bot, query):
    msg_id = int(query.data.split("_")[1])
    file_path = temp_files.get(msg_id)

    if not file_path:
        await query.message.edit("❌ File not found or expired.")
        return

    await query.message.edit("⏳ Uploading to Google Drive...")
    link = upload_to_gdrive(file_path)

    if link:
        await query.message.edit(f"✅ File Uploaded:\n{link}")
    else:
        await query.message.edit("❌ Upload failed.")


bot.run()
