from telegram import Update
from telegram.ext import ContextTypes
from modules.player import skip_track

async def skip_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    result = await skip_track(chat_id)
    
    if result["success"]:
        await update.message.reply_text("⏭️ Skipped to next track")
    else:
        await update.message.reply_text(f"❌ {result['error']}")
