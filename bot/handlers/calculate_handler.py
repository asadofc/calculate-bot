import re
import time
import random
import asyncio
from simpleeval import simple_eval, InvalidExpression
from telegram import Update
from telegram.constants import ChatType, ChatAction
from telegram.ext import ContextTypes
from bot.utils.extractor import extract_user_info
from bot.utils.safe_send import safe_send_message
from bot.utils.logger import logger

# Fixed regex pattern
MATH_PATTERN = re.compile(r'([-+]?\d[\d.\s]*(?:[+\-*/×÷%]\s*[\d.\s]+)+)')

async def calculate_expression(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ui = extract_user_info(update)
    text = update.message.text or ""
    matches = MATH_PATTERN.findall(text)
    is_private = update.effective_chat.type == ChatType.PRIVATE
    is_reply_to_bot = (
        update.message.reply_to_message
        and update.message.reply_to_message.from_user.id == context.bot.id
    )

    if not matches:
        if is_private or is_reply_to_bot:
            await context.bot.send_chat_action(chat_id=ui['chat_id'], action=ChatAction.TYPING)
            await update.message.reply_text("🤖 I'm a calculator bot. Send me a math expression like 2+2 or 3×4!")
        return

    for expr in matches:
        original = expr.strip().replace(" ", "")
        safe = original.replace("×", "*").replace("÷", "/").replace("%", "*0.01")
        try:
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(None, lambda: simple_eval(safe))
            if isinstance(result, float):
                result = round(result, 2)
            reply = f"{original} = {result}"
            await safe_send_message(
                context.bot,
                ui['chat_id'],
                reply,
                reply_to=update.message.message_id if not is_private else None
            )
        except InvalidExpression:
            logger.warning(f"Invalid expression: {original}")
        except Exception as e:
            logger.error(f"Error processing {original}: {e}")