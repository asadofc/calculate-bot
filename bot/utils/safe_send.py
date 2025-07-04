import asyncio
from telegram.constants import ChatAction
from .logger import logger

semaphore = asyncio.Semaphore(20)

async def safe_send_message(bot, chat_id, text, reply_to=None):
    async with semaphore:
        try:
            asyncio.create_task(bot.send_chat_action(chat_id, ChatAction.TYPING))
            if reply_to:
                asyncio.create_task(bot.send_message(chat_id, text, reply_to_message_id=reply_to))
            else:
                asyncio.create_task(bot.send_message(chat_id, text))
            logger.info(f"✅ Queued message to {chat_id}")
        except Exception as e:
            logger.error(f"❌ Error in safe_send_message: {e}")
