from main import call
from modules.downloader import download_audio, download_video
from modules.queue_manager import add_to_queue, remove_current_track, get_current_track
import asyncio

active_players = {}

async def play_audio(chat_id, query):
    try:
        file_path = await download_audio(query)
        title = query.split('/')[-1] if '/' in query else query
        
        track_info = {
            "title": title[:50],
            "path": file_path,
            "type": "audio"
        }
        
        if chat_id in active_players:
            add_to_queue(chat_id, track_info)
            return {"success": True, "title": title, "queued": True}
        else:
            await call.play(chat_id, file_path)
            active_players[chat_id] = True
            return {"success": True, "title": title}
            
    except Exception as e:
        return {"success": False, "error": str(e)}

async def play_video(chat_id, query):
    try:
        file_path = await download_video(query)
        title = query.split('/')[-1] if '/' in query else query
        
        track_info = {
            "title": title[:50],
            "path": file_path,
            "type": "video"
        }
        
        if chat_id in active_players:
            add_to_queue(chat_id, track_info)
            return {"success": True, "title": title, "queued": True}
        else:
            await call.play(chat_id, file_path)
            active_players[chat_id] = True
            return {"success": True, "title": title}
            
    except Exception as e:
        return {"success": False, "error": str(e)}

async def pause_track(chat_id):
    try:
        await call.pause_stream(chat_id)
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}

async def resume_track(chat_id):
    try:
        await call.resume_stream(chat_id)
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}

async def skip_track(chat_id):
    try:
        await call.change_stream(chat_id, None)
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}

async def stop_playback(chat_id):
    try:
        await call.stop_stream(chat_id)
        if chat_id in active_players:
            del active_players[chat_id]
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}

async def set_volume(chat_id, volume):
    try:
        await call.set_my_volume(volume, chat_id=chat_id)
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}
