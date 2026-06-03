from telegram import Update
from telegram.ext import ContextTypes
from modules.voice_chat import join_voice_chat

async def join_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    
    result = await join_voice_chat(chat_id, user_id)
    
    if result["success"]:
        await update.message.reply_text(f"✅ {result['message']}")
    else:
        await update.message.reply_text(f"❌ {result['message']}")
