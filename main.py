import telebot
import os

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
    print("Bot is running...")
    # Using infinity_polling to keep the bot alive
    bot.infinity_polling()