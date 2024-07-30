from telegram.ext import ApplicationBuilder, MessageHandler, BusinessConnectionHandler, filters
from bot.handlers import handle_message
from bot.config import TOKEN


def run():
    application = ApplicationBuilder().token(TOKEN).build()

    # Register message handler
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, # text and not command
        handle_message
    ))

    application.add_handler(BusinessConnectionHandler(
        handle_message
    ))

    # Start the Bot
    application.run_polling()
