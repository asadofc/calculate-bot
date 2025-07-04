from telegram import Update
from telegram.constants import ChatType
from .logger import logger

def extract_user_info(update: Update):
    user = update.effective_user
    chat = update.effective_chat
    info = {
        "user_id": user.id,
        "username": user.username,
        "full_name": user.full_name,
        "chat_id": chat.id,
        "chat_type": chat.type,
        "chat_title": chat.title or chat.first_name or "",
        "chat_username": f"@{chat.username}" if chat.username else "No Username",
        "chat_link": f"https://t.me/{chat.username}" if chat.username else "No Link",
    }
    logger.info(
        f"ℹ️ User info: {info['full_name']} (@{info['username']}) in {info['chat_title']} [{info['chat_id']}] {info['chat_link']}"
    )
    return info
