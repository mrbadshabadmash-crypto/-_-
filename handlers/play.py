from telegram import Update
from telegram.ext import ContextTypes
from modules.player import play_audio, play_video

async def play_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "❌ Please provide a song name or URL!\n\n"
            "Example: `/play shape of you`\n"
            "Example: `/play https://youtube.com/watch?v=...`"
        )
        return
    
    query = " ".join(context.args)
    chat_id = update.effective_chat.id
    
    msg = await update.message.reply_text(f"🎵 Searching: `{query}`...", parse_mode='Markdown')
    
    result = await play_audio(chat_id, query)
    
    if result["success"]:
        await msg.edit_text(f"✅ Now playing: **{result['title']}**", parse_mode='Markdown')
    else:
        await msg.edit_text(f"❌ Error: {result['error']}")

async def vplay_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "❌ Please provide a video name or URL!\n\n"
            "Example: `/vplay shape of you`"
        )
        return
    
    query = " ".join(context.args)
    chat_id = update.effective_chat.id
    
    msg = await update.message.reply_text(f"🎬 Searching video: `{query}`...", parse_mode='Markdown')
    
    result = await play_video(chat_id, query)
    
    if result["success"]:
        await msg.edit_text(f"✅ Now playing video: **{result['title']}**", parse_mode='Markdown')
    else:
        await msg.edit_text(f"❌ Error: {result['error']}")
