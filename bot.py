import os
import telebot
from flask import Flask
from threading import Thread

# Initialize Bot
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# Flask App for Render Port Binding
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# Bot Handlers
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ Votez Bot is active and running on Render!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "I am online! Send me a command.")

if __name__ == "__main__":
    # Start Web Server Thread
    t = Thread(target=run_web)
    t.start()
    
    # Start Bot Polling
    print("Bot is starting...")
    bot.infinity_polling()