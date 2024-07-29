# src/bot/handlers.py

from telegram import Update
from telegram.ext import CallbackContext
from llama.utils import predict

# Store conversation history
conversation_history = {}

async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    chat_id = update.message.chat_id
    
    # Retrieve chat history or initialize it
    if chat_id not in conversation_history:
        conversation_history[chat_id] = []

    # Get the prediction from the llama model
    response = predict(user_message, conversation_history[chat_id])

    # Update conversation history
    conversation_history[chat_id].append((user_message, response))

    # Send the response back to the user
    await update.message.reply_text(response)
