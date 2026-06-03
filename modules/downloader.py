import yt_dlp
import os
import re
from config import DOWNLOAD_DIR

def is_youtube_url(url):
    patterns = [
        r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/',
        r'^https?://youtu\.be/',
        r'^https?://www\.youtube\.com/watch\?v='
    ]
    return any(re.match(pattern, url) for pattern in patterns)

async def download_audio(query):
    if not is_youtube_url(query):
        search_query = f"ytsearch:{query}"
    else:
        search_query = query
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
        'quiet': True,
        'no_warnings': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(search_query, download=True)
        if 'entries' in info:
            info = info['entries'][0]
        
        base = ydl.prepare_filename(info)
        mp3_file = base.rsplit('.', 1)[0] + '.mp3'
        
        if os.path.exists(mp3_file):
            return mp3_file
        
        for ext in ['.m4a', '.webm', '.opus']:
            alt = base.rsplit('.', 1)[0] + ext
            if os.path.exists(alt):
                return alt
        
        raise Exception("No audio file found")

async def download_video(query):
    if not is_youtube_url(query):
        search_query = f"ytsearch:{query}"
    else:
        search_query = query
    
    ydl_opts = {
        'format': 'best[height<=480]',
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
        'quiet': True,
        'no_warnings': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(search_query, download=True)
        if 'entries' in info:
            info = info['entries'][0]
        return ydl.prepare_filename(info)
