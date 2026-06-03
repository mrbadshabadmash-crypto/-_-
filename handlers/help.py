from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
📖 **TG Music Bot - Complete Guide**

**🎵 Playback Commands:**
• `/play <song/url>` - Play audio in voice chat
• `/vplay <song/url>` - Play video in voice chat
• `/pause` - Pause current playback
• `/resume` - Resume playback
• `/skip` - Skip to next song
• `/stop` - Stop and clear queue

**🔊 Voice Chat Commands:**
• `/join` - Bot join your voice chat
• `/leave` - Bot leave voice chat

**📋 Queue Management:**
• `/queue` - Show current queue
• `/volume 1-200` - Adjust volume

**Supported Sources:**
• YouTube links
• YouTube search (song name)
• Audio/Video URLs

**Note:** First use /join to add bot in voice chat!
    """
    await update.message.reply_text(help_text)
