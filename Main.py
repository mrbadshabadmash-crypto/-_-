import logging
import asyncio
from telegram.ext import Application, CommandHandler
from pyrogram import Client
from pytgcalls import PyTgCalls
from config import BOT_TOKEN, API_ID, API_HASH, STRING_SESSION
from handlers import (
    start_command, help_command, play_command, vplay_command,
    pause_command, resume_command, skip_command, stop_command,
    queue_command, volume_command, join_command, leave_command
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Pyrogram Client
app = Client(STRING_SESSION, api_id=API_ID, api_hash=API_HASH)

# PyTgCalls
call = PyTgCalls(app)

# Telegram Bot
bot_app = Application.builder().token(BOT_TOKEN).build()

# Commands
bot_app.add_handler(CommandHandler("start", start_command))
bot_app.add_handler(CommandHandler("help", help_command))
bot_app.add_handler(CommandHandler("play", play_command))
bot_app.add_handler(CommandHandler("vplay", vplay_command))
bot_app.add_handler(CommandHandler("pause", pause_command))
bot_app.add_handler(CommandHandler("resume", resume_command))
bot_app.add_handler(CommandHandler("skip", skip_command))
bot_app.add_handler(CommandHandler("stop", stop_command))
bot_app.add_handler(CommandHandler("queue", queue_command))
bot_app.add_handler(CommandHandler("volume", volume_command))
bot_app.add_handler(CommandHandler("join", join_command))
bot_app.add_handler(CommandHandler("leave", leave_command))

async def run_bot():
    await bot_app.initialize()
    await bot_app.start()
    await call.start()
    logging.info("🎵 TG Music Bot is running!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(run_bot())
