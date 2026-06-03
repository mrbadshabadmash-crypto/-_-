from telegram import Update
from telegram.ext import ContextTypes
from modules.queue_manager import get_queue, get_current_track

async def queue_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    queue = get_queue(chat_id)
    current = get_current_track(chat_id)
    
    if not current and not queue:
        await update.message.reply_text("📋 Queue is empty!")
        return
    
    queue_text = "**📋 Current Queue:**\n\n"
    
    if current:
        queue_text += f"**Now Playing:** {current['title']}\n\n"
    
    if queue:
        queue_text += "**Up Next:**\n"
        for i, track in enumerate(queue[:10], 1):
            queue_text += f"{i}. {track['title']}\n"
        
        if len(queue) > 10:
            queue_text += f"\nAnd {len(queue) - 10} more..."
    
    await update.message.reply_text(queue_text, parse_mode='Markdown')
