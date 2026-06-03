from telegram import Update
from telegram.ext import ContextTypes
from modules.player import set_volume

async def volume_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Please provide volume level!\n\nExample: `/volume 50` (1-200)")
        return
    
    try:
        volume = int(context.args[0])
        if volume < 1 or volume > 200:
            await update.message.reply_text("❌ Volume must be between 1 and 200!")
            return
        
        chat_id = update.effective_chat.id
        result = await set_volume(chat_id, volume)
        
        if result["success"]:
            await update.message.reply_text(f"🔊 Volume set to {volume}%")
        else:
            await update.message.reply_text(f"❌ {result['error']}")
            
    except ValueError:
        await update.message.reply_text("❌ Please provide a valid number!")
