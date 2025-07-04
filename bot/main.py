import threading
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from bot.config import BOT_TOKEN
from bot.server import start_server
from bot.handlers.start_handler import start_command
from bot.handlers.help_handler import help_command
from bot.handlers.calculate_handler import calculate_expression
from bot.utils.logger import logger

def main():
    logger.info("🚀 Calculator Bot is launching...")

    if not BOT_TOKEN:
        logger.critical("❌ BOT_TOKEN is not set. Exiting.")
        return

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate_expression))

    async def post_init(application):
        await application.bot.set_my_commands([
            ("start", "Welcome message"),
            ("help", "How to use me")
        ])
        logger.info("📋 Commands registered")

    app.post_init = post_init

    threading.Thread(target=start_server, daemon=True).start()
    app.run_polling()

if __name__ == "__main__":
    main()
