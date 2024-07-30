import logging

from telegram import Update
from telegram.ext import CallbackContext
from llama.utils import predict

# Store conversation history
conversation_history = {}

async def handle_message(update: Update, context: CallbackContext) -> None:
    message = update.message or update.business_message
    user_message = message.text
    chat_id = message.chat_id
    logging.info(f"Message from {update.effective_user.name}: {message.text}")
    
    # Retrieve chat history or initialize it
    if chat_id not in conversation_history:
        conversation_history[chat_id] = []

    # Get the prediction from the llama model
    response = predict(user_message, conversation_history[chat_id])

    # Update conversation history
    conversation_history[chat_id].append((user_message, response))

    # Send the response back to the user
    logging.info(f"Bot answer to {update.effective_user.name}: {response}")
    await message.reply_text(response)


