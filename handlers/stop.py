from telegram import Update
from telegram.ext import ContextTypes
from modules.player import stop_playback

async def stop_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    result = await stop_playback(chat_id)
    
    if result["success"]:
        await update.message.reply_text("⏹️ Playback stopped and queue cleared")
    else:
        await update.message.reply_text(f"❌ {result['error']}")
