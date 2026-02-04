import telebot
import os
import time
import logging
from telebot.apihelper import ApiTelegramException

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token from @BotFather
BOT_TOKEN = os.environ.get('BOT_TOKEN', 'YOUR_BOT_TOKEN')

# Initialize the bot instance
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Bot is active.")

def start_bot():
    print("Bot is starting...")
    
    # 1. Clear any existing webhooks
    try:
        bot.remove_webhook()
        # 2. Increased delay to ensure Telegram registers the disconnection
        time.sleep(2)
        print("Webhook removed and session cleared.")
    except Exception as e:
        print(f"Initial cleanup error: {e}")

    # 3. Robust polling loop to handle 409 conflicts during deployment restarts
    retry_delay = 5
    while True:
        try:
            print("Bot is now polling...")
            # skip_pending=True is crucial to avoid 409 on old updates
            bot.infinity_polling(
                timeout=60, 
                long_polling_timeout=20, 
                logger_level=logging.ERROR,
                skip_pending=True
            )
        except ApiTelegramException as e:
            if e.error_code == 409:
                print(f"Conflict (409) detected. Retrying in {retry_delay} seconds... (Error: {e})")
                time.sleep(retry_delay)
            else:
                print(f"Telegram API Error: {e}")
                time.sleep(retry_delay)
        except Exception as e:
            print(f"Unexpected error: {e}")
            time.sleep(retry_delay)

if __name__ == "__main__":
    start_bot()