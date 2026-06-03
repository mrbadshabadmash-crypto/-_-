from telegram import Update
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 **Welcome to TG Music Bot!**\n\n"
        "I can play music and videos in voice chats!\n\n"
        "**Commands:**\n"
        "• `/play <song>` - Play audio\n"
        "• `/vplay <song>` - Play video\n"
        "• `/join` - Join voice chat\n"
        "• `/leave` - Leave voice chat\n"
        "• `/pause` - Pause\n"
        "• `/resume` - Resume\n"
        "• `/skip` - Skip track\n"
        "• `/stop` - Stop playback\n"
        "• `/queue` - Show queue\n"
        "• `/volume 1-200` - Set volume\n"
        "• `/help` - All commands\n\n"
        "**Example:** `/play shape of you`",
        parse_mode='Markdown'
    )
