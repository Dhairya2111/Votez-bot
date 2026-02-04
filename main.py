import telebot
import os
import time
import logging
from telebot.apihelper import ApiTelegramException

# Configure logging to see errors clearly
logging.basicConfig(level=logging.INFO)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token from @BotFather
BOT_TOKEN = os.environ.get('BOT_TOKEN', 'YOUR_BOT_TOKEN')

# Initialize the bot instance
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Bot is active.")

if __name__ == "__main__":
    print("Bot is starting...")
    
    # 1. Clear any existing webhooks which often cause 409 conflicts
    try:
        bot.remove_webhook()
        # 2. Small delay to allow Telegram servers to process the session closure
        time.sleep(1)
        print("Webhook removed and session cleared.")
    except Exception as e:
        print(f"Initial cleanup error: {e}")

    # 3. Use infinity_polling with skip_pending=True to avoid backlog processing
    # and built-in error handling for 409 conflicts.
    try:
        print("Bot is now polling...")
        bot.infinity_polling(
            timeout=20, 
            long_polling_timeout=10, 
            logger_level=logging.ERROR,
            skip_pending=True
        )
    except Exception as e:
        print(f"Critical failure: {e}")