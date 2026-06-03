queues = {}

def add_to_queue(chat_id, track):
    if chat_id not in queues:
        queues[chat_id] = []
    queues[chat_id].append(track)

def get_queue(chat_id):
    return queues.get(chat_id, [])

def get_current_track(chat_id):
    return None

def remove_current_track(chat_id):
    if chat_id in queues and queues[chat_id]:
        queues[chat_id].pop(0)

def clear_queue(chat_id):
    if chat_id in queues:
        queues[chat_id] = []
