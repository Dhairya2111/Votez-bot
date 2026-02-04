import telebot
import os
import time
from telebot.apihelper import ApiTelegramException

# Replace 'YOUR_BOT_TOKEN' with your actual bot token from @BotFather
# Or set it as an environment variable for security
BOT_TOKEN = os.environ.get('BOT_TOKEN', 'YOUR_BOT_TOKEN')

# Initialize the bot instance
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start']) # 1. Message detect hota hai
def send_welcome(message):
    bot.reply_to(message, "Hello!")      # 2. Bot reply bhejta hai

# Start the bot
if __name__ == "__main__":
    print("Bot is starting...")
    
    # Fix for Error 409: Conflict
    # Remove any existing webhooks before starting polling
    try:
        bot.remove_webhook()
        print("Webhook removed successfully.")
    except Exception as e:
        print(f"Error removing webhook: {e}")

    # Using infinity_polling with error handling to manage conflicts
    while True:
        try:
            print("Bot is running...")
            bot.infinity_polling(timeout=10, long_polling_timeout=5)
        except ApiTelegramException as e:
            if e.error_code == 409:
                print("Conflict detected (409). Another instance might be running. Retrying in 5 seconds...")
                time.sleep(5)
            else:
                raise e
        except Exception as e:
            print(f"Unexpected error: {e}")
            time.sleep(5)