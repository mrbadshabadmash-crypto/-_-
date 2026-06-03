from telegram import Update
from telegram.ext import ContextTypes
from modules.player import pause_track

async def pause_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    result = await pause_track(chat_id)
    
    if result["success"]:
        await update.message.reply_text("⏸️ Playback paused")
    else:
        await update.message.reply_text(f"❌ {result['error']}")
