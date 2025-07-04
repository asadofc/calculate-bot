from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ChatType, ChatAction
from telegram.ext import ContextTypes
from bot.config import CHANNEL_LINK, GROUP_LINK, ADD_ME_LINK
from bot.utils.extractor import extract_user_info
from bot.utils.logger import logger

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type != ChatType.PRIVATE:
        return
    ui = extract_user_info(update)
    kb = [
        [InlineKeyboardButton("Updates", url=CHANNEL_LINK), InlineKeyboardButton("Support", url=GROUP_LINK)],
        [InlineKeyboardButton("Add Me To Your Group", url=ADD_ME_LINK)],
    ]
    await context.bot.send_chat_action(chat_id=ui['chat_id'], action=ChatAction.TYPING)
    await update.message.reply_text(
        "👋 Hi! I am Calculator Bot.\n\n"
        "Just send me any math question like 5×5 or 20+30 and I will give you the answer.",
        reply_markup=InlineKeyboardMarkup(kb),
    )
