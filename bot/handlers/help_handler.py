from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes
from bot.utils.extractor import extract_user_info
from bot.utils.logger import logger

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ui = extract_user_info(update)
    await context.bot.send_chat_action(chat_id=ui['chat_id'], action=ChatAction.TYPING)
    await update.message.reply_text(
        "💌 How to use me:\n\n"
        "Send me math like:\n"
        "➤ 4+4\n"
        "➤ 8-2\n"
        "➤ 5×5\n"
        "➤ 9÷3\n\n"
        "I will solve it for you!"
    )