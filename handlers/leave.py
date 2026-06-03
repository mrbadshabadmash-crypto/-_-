from telegram import Update
from telegram.ext import ContextTypes
from modules.voice_chat import leave_voice_chat

async def leave_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    
    result = await leave_voice_chat(chat_id)
    
    if result["success"]:
        await update.message.reply_text(f"✅ {result['message']}")
    else:
        await update.message.reply_text(f"❌ {result['message']}")
