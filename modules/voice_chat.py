from main import call
import asyncio

active_chats = {}

async def join_voice_chat(chat_id, user_id):
    try:
        await call.join_group_call(chat_id, None)
        active_chats[chat_id] = True
        return {"success": True, "message": "Joined voice chat!"}
    except Exception as e:
        return {"success": False, "message": f"Failed to join: {str(e)}"}

async def leave_voice_chat(chat_id):
    try:
        await call.leave_group_call(chat_id)
        if chat_id in active_chats:
            del active_chats[chat_id]
        return {"success": True, "message": "Left voice chat"}
    except Exception as e:
        return {"success": False, "message": f"Failed to leave: {str(e)}"}
