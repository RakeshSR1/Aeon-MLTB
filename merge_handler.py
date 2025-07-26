# bot/merge_handler.py
import os
from pyrogram import Client, filters

# Replace with your Telegram user ID or list of admin IDs
OWNER_ID = 123456789

@Client.on_message(filters.command("merge") & filters.user(OWNER_ID))
async def merge_handler(client, message):
    await message.reply("Merging videos...")

    # List your video files (these should already be downloaded)
    video_files = ["part1.mp4", "part2.mp4", "part3.mp4"]
    output_file = "merged.mp4"

    # Call the moviepy-based merge script
    os.system(f"python3 merge_videos.py {' '.join(video_files)} {output_file}")

    await message.reply_video(video=output_file, caption="✅ Merged video")
