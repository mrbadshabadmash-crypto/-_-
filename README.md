# 🎵 RonaldoXMusic_Bot

A powerful Telegram bot that plays **audio** and **video** in voice chats!

## ✨ Features

- 🎵 Play audio from YouTube
- 🎬 Play video in voice chat  
- 📋 Queue management
- 🔊 Volume control (1-200%)
- ⏸️ Pause, resume, skip, stop
- 🔍 YouTube search support

## 📋 Requirements

- Python 3.9+
- FFmpeg
- Telegram API credentials

## 🔧 Setup

### 1. Get Credentials

1. Go to [my.telegram.org](https://my.telegram.org)
2. Create app → Get `API_ID` and `API_HASH`
3. Get `STRING_SESSION` from [Replit](https://replit.com/@AdityaHalder/GenerateStringSession)

### 2. Create Bot

Message [@BotFather](https://t.me/BotFather) on Telegram: 
/newbot
-> Get Token 

### 3. Install FFmpeg

**Ubuntu/Debian:**
```bash
sudo apt install ffmpeg -y

# 4. RUN BOT
git clone https://github.com/YOUR_USERNAME/TG-MUSIC-BOT.git
cd TG-MUSIC-BOT
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your credentials
python main.py

🕸️COMMANDS

Command Description
/play <song> Play audio
/vplay <song> Play video
/join Join voice chat
/leave Leave voice chat
/pause Pause
/resume Resume
/skip Skip track
/stop Stop
/queue Show queue
/volume 1-200 Set volume

🕸️LICENSE
MIT LICENSE


---

## 🎯 **Sirf Itna Change Karo:**

| Line | Purana | Naya |
|------|--------|------|
| Line 1 | `# 🎵 TG Music Bot` | `# 🎵 RonaldoXMusic_Bot` |

**Baaki sab kuch WAISA HI rakho!** ✅

---

## 📌 **Optional - Bot Ke Start Message Mein Bhi Change Kar Sakte Ho:**

Agar chahte ho ki bot `/start` command par apna naam dikhaye, toh `handlers/start.py` mein bhi change karo:

**`handlers/start.py` mein line 5 change karo:**

```python
await update.message.reply_text(
    "🎵 **Welcome to RonaldoXMusic_Bot!**\n\n"  # ← ye line change karo
    "I can play music and videos in voice chats!\n\n"
    ...
)
