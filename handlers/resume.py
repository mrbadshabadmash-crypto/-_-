from telegram import Update
from telegram.ext import ContextTypes
from modules.player import resume_track

async def resume_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    result = await resume_track(chat_id)
    
    if result["success"]:
        await update.message.reply_text("▶️ Playback resumed")
    else:
        await update.message.reply_text(f"❌ {result['error']}")
