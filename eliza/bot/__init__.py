from telegram.ext import Updater, MessageHandler, filters
from bot.handlers import handle_message
from bot.config import TOKEN


def run() -> None:

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Register message handler
    dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, # text and not command
                                          handle_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()
